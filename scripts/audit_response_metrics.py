"""Analyst counterexample: equal spectral magnitude does not identify time response.

All parameters and signals below are SYNTHETIC, not measured gust/vehicle data.
H0(s)=1/(1+T*s); Hd(s)=exp(-delay*s)*H0(s), T>0 and delay>=0.
Default plotting requires matplotlib; --no-plot runs standard-library checks/CSVs.
"""
import argparse
import cmath
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'learning/audits'
T, DELAY = 0.1, 0.2  # seconds, analyst choices only


def transfer(frequency):
    w = 2 * math.pi * frequency
    h0 = 1 / (1 + 1j*w*T)
    return h0, cmath.exp(-1j*w*DELAY)*h0


def step(t, delay=0):
    return 0.0 if t < delay else -math.expm1(-(t-delay)/T)


def main(plot=True):
    rows = []
    for frequency in [0, 0.25, 0.5, 1, 2, 4, 8]:
        h0, hd = transfer(frequency)
        assert math.isclose(abs(h0), abs(hd), rel_tol=1e-12)
        assert math.isclose(abs(h0)**2, abs(hd)**2, rel_tol=1e-12)
        # Phase difference is unwrapped here; complex ratios avoid branch ambiguity.
        assert abs(hd/h0-cmath.exp(-2j*math.pi*frequency*DELAY)) < 1e-12
        rows.append([frequency,abs(h0),abs(hd),abs(h0)**2,abs(hd)**2,
                     math.degrees(cmath.phase(h0)),-360*frequency*DELAY,'SYNTHETIC'])
    with (OUT/'response_magnitude_counterexample.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        w.writerow(['frequency_Hz','H0_magnitude','Hdelay_magnitude','H0_power','Hdelay_power',
                    'H0_phase_deg','added_unwrapped_phase_deg','data_status'])
        w.writerows(rows)
    assert step(DELAY/2) > 0.6 and step(DELAY/2,DELAY) == 0
    assert math.isclose(step(0.7,DELAY),step(0.5),rel_tol=1e-12)
    times=[-0.2+i*0.005 for i in range(341)]
    ts=[]
    h0,hd=transfer(1)
    for t in times:
        z=cmath.exp(2j*math.pi*t)
        ts.append([t,step(t),step(t,DELAY),(h0*z).imag,(hd*z).imag,'SYNTHETIC'])
    with (OUT/'response_time_counterexample.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        w.writerow(['time_s','H0_step','Hdelay_step','H0_steady_sine_1Hz','Hdelay_steady_sine_1Hz','data_status'])
        w.writerows(ts)
    if not plot:
        print('7 frequency/phase cases and causal-step checks passed; 341 synthetic time rows; plotting skipped.')
        return
    # Static scientific figure; all signals and labels explicitly synthetic.
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams['svg.hashsalt']='crosswind-response-counterexample'
    fig,axs=plt.subplots(1,3,figsize=(12,3.3),constrained_layout=True)
    fs=[i/20 for i in range(161)]
    axs[0].plot(fs,[abs(transfer(f)[0]) for f in fs],label='H0')
    axs[0].plot(fs,[abs(transfer(f)[1]) for f in fs],'--',label='Hdelay')
    axs[0].set(xlabel='Frequency [Hz]',ylabel='Magnitude',title='Identical magnitude')
    for ax,column_a,column_b,title in [(axs[1],1,2,'Different step histories'),(axs[2],3,4,'Different phase at 1 Hz')]:
        ax.plot(times,[r[column_a] for r in ts],label='H0')
        ax.plot(times,[r[column_b] for r in ts],'--',label='Hdelay')
        ax.set(xlabel='Time [s]',ylabel='Normalized output',title=title)
    for ax in axs:
        ax.grid(alpha=0.25);ax.legend()
    fig.suptitle('SYNTHETIC analyst example: T=0.1 s, delay=0.2 s; no author data')
    fig.savefig(OUT/'response_magnitude_counterexample.svg',metadata={'Date':None})
    fig.savefig(Path('C:/Users/17984/AppData/Local/Temp/crosswind-response-2026-10-16.png'),dpi=140)
    plt.close(fig)
    print('7 frequency cases: equal magnitude/power, verified phase factor; distinct causal step responses; 341 labelled synthetic time rows.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-plot',action='store_true')
    main(plot=not parser.parse_args().no_plot)
