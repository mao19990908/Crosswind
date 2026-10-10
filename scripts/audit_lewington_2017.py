"""Offline published-table/kinematic audit, not ADAMS or CFD reproduction."""
import csv
import math
from pathlib import Path


def cumulative_trapezoid(t, values):
    out = [0.0]
    for i in range(1, len(t)):
        out.append(out[-1] + (t[i]-t[i-1])*(values[i]+values[i-1])/2)
    return out


def main():
    rows = []
    # Published Table2 rounded values, no individual runs or CI constructed.
    for vehicle, mean, sd, qs, coupled in [
        ('Everest', .92, .15, .77, .92),
        ('Escort', 1.05, .23, 1.09, 1.19),
        ('B-Max', 1.20, .21, 1.23, 1.21),
    ]:
        for method, pred in [('quasi_steady', qs), ('one_way', coupled)]:
            residual = pred-mean
            sd_units = residual/sd
            assert abs(sd_units) <= 1+1e-12
            rows.append((f'{vehicle}_{method}_signed_residual_m', residual, 'Table2 rounded values;not independent data'))
            rows.append((f'{vehicle}_{method}_signed_residual_in_SD', sd_units, 'Descriptive SD distance;not z-test or 95%CI'))
    # Synthetic kinematics, same time grid/zero IC/constant speed, not measured data.
    t=[i*.02 for i in range(101)]
    speed=25.0
    ay=[.2*math.sin(math.pi*x) for x in t]
    yaw_a=[.04*math.sin(2*math.pi*x) for x in t]
    yaw_b=[-.03*math.cos(math.pi*x) for x in t]
    direct_velocity=cumulative_trapezoid(t, ay)
    direct_path=cumulative_trapezoid(t, direct_velocity)
    paths=[]
    for yaw in [yaw_a,yaw_b]:
        alpha=cumulative_trapezoid(t,yaw)
        beta=cumulative_trapezoid(t,[a/speed-r for a,r in zip(ay,yaw)])
        gamma=cumulative_trapezoid(t,[speed*(a+b) for a,b in zip(alpha,beta)])
        assert max(abs(x-y) for x,y in zip(gamma,direct_path)) < 1e-12
        paths.append(gamma)
    cancellation=max(abs(a-b) for a,b in zip(paths[0],paths[1]))
    assert cancellation < 1e-12
    rows.append(('synthetic_yaw_change_path_difference_m',cancellation,'ANALYST_INFERENCE: Eqs4-6 same-grid constant-speed cancellation only'))
    offset=.01; duration=t[-1]
    drift=cumulative_trapezoid(t,cumulative_trapezoid(t,[offset]*len(t)))[-1]
    assert math.isclose(drift,.5*offset*duration**2,abs_tol=1e-12)
    rows.append(('synthetic_0p01_m_s2_bias_over_2s_drift_m',drift,'ANALYST_INFERENCE: hypothetical constant acceleration bias;not actual sensor error'))
    rows.append(('nominal_measurement_interval_s',1/50,'Reported50Hz;postprocessing/resampling unspecified'))
    rows.append(('measurement_interval_over_CFD_dt',(.02/.00025),'ANALYST_INFERENCE:80;not specified output or MBD step ratio'))
    out=Path(__file__).resolve().parents[1]/'learning/audits/lewington_2017_arithmetic.csv'
    with out.open('w',encoding='utf-8',newline='') as stream:
        w=csv.writer(stream);w.writerow(['quantity','derived_value','provenance_and_limit'])
        for name,value,note in rows:w.writerow([name,f'{value:.12g}',note])
    print(f'{len(rows)} derived rows; Table2 SD distances and synthetic kinematic checks passed; no raw-data replay.')


if __name__ == '__main__':
    main()
