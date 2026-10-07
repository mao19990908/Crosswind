"""Offline arithmetic, not a pressure-integration or experiment reproduction."""
import csv
import math
from pathlib import Path


def main():
    values = [
        ('reported_side_peak_change_percent', (2.0 / 1.70 - 1) * 100,
         'PDF7 rounded reported loads; arithmetic only'),
        ('reported_upper_lift_change_percent', (1.61 / 1.44 - 1) * 100,
         'PDF7 upper surface only; arithmetic only'),
        ('reported_net_yaw_change_percent', (.37 / .39 - 1) * 100,
         'PDF8 approximate values; no statistical-significance inference'),
        ('axial_to_resultant_coefficient_factor_at_30deg', math.cos(math.radians(30)) ** 2,
         'ANALYST_INFERENCE: identical load/area/length/origin; perpendicular flow only'),
        ('aperture_over_drawing_length', 1.5 / .522,
         'ANALYST_INFERENCE: Fig4 522 interpreted in mm; actual normalization length unconfirmed'),
    ]
    assert round(values[0][1]) == 18 and round(values[1][1]) == 12
    assert values[2][1] < 0
    assert math.isclose(values[3][1], .75, abs_tol=1e-12)
    out = Path(__file__).resolve().parents[1] / 'learning/audits/ryan_1998_arithmetic.csv'
    with out.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['quantity', 'derived_value', 'provenance_and_limit'])
        for name, value, note in values:
            w.writerow([name, f'{value:.8f}', note])
    print('5 arithmetic checks written; no measured signal or pressure integration fabricated.')


if __name__ == '__main__':
    main()
