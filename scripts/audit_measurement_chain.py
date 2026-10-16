"""Analyst-only measurement-chain counterexamples, not recovered paper data.

Run from any directory with Python's standard library. Writes a small audit CSV
under learning/audits; no PDFs, network, fitted parameters or author outputs.
All chosen signals, timing, filters and covariance values are SYNTHETIC.
"""

import cmath
import csv
import math
from pathlib import Path


def main():
    rows = []

    def check(name, observed, expected, unit, interpretation, tol=1e-11):
        residual = abs(observed - expected)
        if not math.isfinite(observed) or residual > tol:
            raise AssertionError(f"{name}: {observed} != {expected}")
        rows.append(dict(
            case=name, data_origin="SYNTHETIC_ANALYST_INFERENCE",
            observed=f"{observed:.15g}", expected=f"{expected:.15g}",
            absolute_residual=f"{residual:.4g}", unit=unit, result="pass",
            interpretation=interpretation,
        ))

    # Two patch-force phasors (already pressure-area projected), in N.
    # Re(z*exp(i*omega*t)); x=(+0.5,-0.5)m, both forces along +y.
    z1, z2 = 1 + 0j, 1j
    check("signed_phasor_force_amplitude", abs(z1 + z2), math.sqrt(2), "N",
          "Integrate signed complex signals before taking amplitude;sum amplitudes would be2N")
    samples = 4096
    recovered = sum(
        ((z1 * cmath.exp(2j * math.pi * k / samples)).real
         + (z2 * cmath.exp(2j * math.pi * k / samples)).real)
        * cmath.exp(-2j * math.pi * k / samples)
        for k in range(samples)
    ) * 2 / samples
    check("time_domain_fourier_matches_phasor_sum", abs(recovered - (z1 + z2)),
          0, "N", "Independent time-domain Fourier recovery of complex resultant")

    # True equal in-phase patch forces have zero moment about the midpoint.
    frequency, delay, half_spacing = 5.0, 0.020, 0.5
    delayed = cmath.exp(-2j * math.pi * frequency * delay)
    check("aligned_equal_forces_yaw", abs(half_spacing * (1 - 1)), 0, "N*m",
          "Exact cancellation about specified midpoint")
    check("relative_channel_delay_false_yaw", abs(half_spacing * (1 - delayed)),
          2 * half_spacing * abs(math.sin(math.pi * frequency * delay)), "N*m",
          "Only second channel delayed20ms at5Hz;artifact not aerodynamic yaw")
    check("common_channel_delay_yaw", abs(half_spacing * (delayed - delayed)), 0, "N*m",
          "Common delay changes input-output phase but preserves this spatial cancellation")

    # Chosen first-order low-pass examples, NOT Macklin's or Chadwick's filter.
    h30 = 1 / (1 + 1j * frequency / 30)
    h10 = 1 / (1 + 1j * frequency / 10)
    check("common_lti_filter_commutes_with_fixed_weights",
          abs(h30 * (z1 + z2) - (h30 * z1 + h30 * z2)), 0, "N",
          "Constant weights,common LTI transfer,aligned signals and identical boundary treatment")
    expected_differential = half_spacing * (frequency / 10 - frequency / 30) / (
        math.hypot(1, frequency / 30) * math.hypot(1, frequency / 10))
    check("different_channel_filters_false_yaw", abs(half_spacing * (h30 - h10)),
          expected_differential, "N*m",
          "Unequal chosen channel transfer functions destroy true moment cancellation")

    # Two unit-height Gaussian events with opposite timing offsets. Each event
    # individually peaks at1. A common trigger is not perfect event registration.
    times = [k / 1000 for k in range(-1000, 1001)]
    events = [[math.exp(-0.5 * ((t - center) / 0.05) ** 2) for t in times]
              for center in (-0.2, 0.2)]
    mean_individual_peaks = sum(max(event) for event in events) / 2
    peak_mean_curve = max((a + b) / 2 for a, b in zip(*events))
    check("mean_individual_event_peaks", mean_individual_peaks, 1, "unit_signal",
          "Two shifted unit pulses;not a paper's event population")
    check("peak_phase_average_curve", peak_mean_curve, (1 + math.exp(-32)) / 2,
          "unit_signal", "At sampled centers;peak(mean)about0.5 versus mean(peak)=1")
    assert peak_mean_curve < mean_individual_peaks

    # Exact linear covariance identity at a specified time. Force SD1N each,
    # lever arm0.5m; assumed rho explicitly varied, not estimated from papers.
    # It is NOT uncertainty of a max-selected peak, which is nonlinear.
    for rho in (-0.5, 0.0, 0.9, 1.0):
        covariance = ((1.0, rho), (rho, 1.0))
        weights = (half_spacing, -half_spacing)
        variance = sum(weights[i] * covariance[i][j] * weights[j]
                       for i in range(2) for j in range(2))
        check(f"fixed_time_yaw_variance_rho_{rho:g}", variance,
              2 * half_spacing**2 * (1 - rho), "(N*m)^2",
              "Known geometry,linear reduction;unknown covariance prevents source uncertainty propagation")

    destination = Path(__file__).resolve().parents[1] / "learning/audits/measurement_chain_checks.csv"
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Measurement-chain audit OK: {len(rows)} synthetic checks; {destination.name}")
    print(f"Relative-delay yaw={abs(half_spacing * (1-delayed)):.9f}N*m; "
          f"unequal-filter yaw={expected_differential:.9f}N*m; "
          f"peak(mean)={peak_mean_curve:.9f}, mean(peak)={mean_individual_peaks:.9f}")


if __name__ == "__main__":
    main()
