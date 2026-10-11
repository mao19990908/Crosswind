"""Published-parameter arithmetic only; not CFD, driver or road-data replay."""
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = [
    ('cfd_step', 3.5 / 87500, 's', 'p664-665; agrees with reported 4e-5s'),
    ('vehicle_nominal_step', 3.5 / 3500, 's', 'p665 total steps; not communication period'),
    ('nominal_step_ratio', 87500 / 3500, '1', 'not proof of exchange schedule'),
    ('nominal_wind_angle', math.degrees(math.atan2(12.1, 33.3)), 'deg', 'perpendicular constant speeds; not instantaneous body incidence'),
    ('nominal_zone_time', 40 / 33.3, 's', 'Fig7 length/speed; not full vehicle exposure'),
    ('nominal_preview_time', 50 / 33.3, 's', 'Fig15 distance/speed; not driver dead time'),
]
assert math.isclose(rows[0][1], 4e-5, rel_tol=1e-12)
assert math.isclose(rows[1][1] / rows[0][1], rows[2][1])
assert abs(rows[3][1] - 20) < 0.1
assert abs(rows[4][1] - 1.2) < 0.01
with (ROOT / 'learning/audits/nakasato_2017_arithmetic.csv').open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['quantity', 'value', 'unit', 'boundary', 'status'])
    for quantity, value, unit, boundary in rows:
        w.writerow([quantity, format(value, '.12g'), unit, boundary, 'ANALYST_INFERENCE'])
print('Nakasato arithmetic OK: 6 derived rows; no original simulation or trace reproduction.')
