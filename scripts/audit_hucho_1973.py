"""Check analyst derivations from SAE 730232 Eqs. 8, 11, 19, 23.

No PDF download, source geometry, measured data or Fig. 11/12 reproduction.
The output contains dimensionless analyst-selected clearance ratios only.
"""
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def simpson(function, lo, hi, panels=1000):
    step = (hi - lo) / panels
    return step / 3 * (
        function(lo) + function(hi)
        + 4 * sum(function(lo + k * step) for k in range(1, panels, 2))
        + 2 * sum(function(lo + k * step) for k in range(2, panels, 2))
    )


def main():
    rows = []
    for ratio in (0.0, 0.1, 0.25, 0.5, 0.75, 1.0):
        theta = math.asin(ratio)
        # z/z1 = sin(theta) removes the integrable roof singularity.
        stationary = simpson(lambda t: 1.0, theta, math.pi / 2) / (math.pi / 2)
        transient = simpson(lambda t: math.cos(t) ** 2, theta, math.pi / 2) / (math.pi / 4)
        closed_s = 1 - 2 / math.pi * theta
        closed_i = 1 - 2 / math.pi * (theta + ratio * math.sqrt(1 - ratio ** 2))
        assert abs(stationary - closed_s) < 1e-11
        assert abs(transient - closed_i) < 1e-11
        assert -1e-12 <= closed_i <= closed_s + 1e-12 <= 1 + 1e-12
        rows.append(dict(clearance_ratio=ratio,phi_s_analytic=closed_s,
                         phi_i_analytic=closed_i,phi_s_quadrature=stationary,
                         phi_i_quadrature=transient,
                         provenance='ANALYST_INFERENCE_from_Eqs8_11_19_not_vehicle_data'))
    # Integral of d(Vc/Vinf)/d(s/sm) over the mixing zone is one.
    assert abs(simpson(lambda u: math.pi / 2 * math.sin(math.pi * u), 0, 1) - 1) < 1e-11
    assert abs((1 - math.cos(math.pi / 2)) / 2 - 0.5) < 1e-14
    output = ROOT / 'learning' / 'audits' / 'hucho_1973_clearance_check.csv'
    output.parent.mkdir(exist_ok=True)
    with output.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print('Hucho audit OK: 6 analyst clearance ratios; closed forms vs quadrature; input-gradient integral.')
    print('At a=0.5: phi_s=%.9f; phi_i=%.9f' % (rows[3]['phi_s_analytic'], rows[3]['phi_i_analytic']))


if __name__ == '__main__':
    main()
