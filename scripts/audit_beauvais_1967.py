"""Offline arithmetic audit of SAE 670608 pp.2222-2224.

Source labels are inputs; derived speeds are NOT recovered experimental runs.
No digitized curves, synthetic loads, or source PDFs are emitted.
"""
import csv
import math
from pathlib import Path


def main():
    rows = []
    for angle in (28, 39, 57, 63, 74):
        # Fig.8 labels total relative V=40 ft/s, not carriage speed Vu.
        u = 40 * math.cos(math.radians(angle))
        v = 40 * math.sin(math.radians(angle))
        assert math.isclose(math.hypot(u, v), 40, abs_tol=1e-12)
        assert math.isclose(math.degrees(math.atan2(v, u)), angle, abs_tol=1e-12)
        rows.append(dict(case=f'Fig8_yaw_{angle}', yaw_deg=f'{angle:.6f}',
                         resultant_ft_s='40.000000', carriage_ft_s=f'{u:.6f}',
                         crosswind_ft_s=f'{v:.6f}',
                         inside_stated_ranges=str(20 <= u <= 40 and 20 <= v <= 80).lower(),
                         provenance='ANALYST_INFERENCE from Fig8 labels and Eqs2-3; not raw data'))
    # Fig.7: printed 18 and 70 ft/s, approximate 75 degrees, .390 s.
    angle = math.degrees(math.atan2(70, 18))
    transit = 7 / 18
    assert abs(transit - .390) < .002
    rows.append(dict(case='Fig7_printed_speeds', yaw_deg=f'{angle:.6f}',
                     resultant_ft_s=f'{math.hypot(18,70):.6f}', carriage_ft_s='18.000000',
                     crosswind_ft_s='70.000000', inside_stated_ranges='false',
                     provenance='ANALYST_INFERENCE; 7ft/18ft_s agrees with .390s within .002s'))
    out = Path(__file__).resolve().parents[1] / 'learning/audits/beauvais_1967_speed_check.csv'
    with out.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f'6 labelled cases checked; Fig7 yaw={angle:.6f} deg, transit={transit:.6f} s')
    print('Stated rectangle envelope only (not actual run coverage):',
          f'yaw={math.degrees(math.atan2(20,40)):.6f}..{math.degrees(math.atan2(80,20)):.6f} deg')
    print('Area and balance-arm dimensions remain unknown; no load reconstruction performed.')


if __name__ == '__main__':
    main()
