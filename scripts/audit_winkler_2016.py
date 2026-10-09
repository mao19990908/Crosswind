"""Offline source-equation checks; NOT CFD/controller/trajectory reproduction.

Numbers derived here are ANALYST_INFERENCE from the accepted manuscript.
No network, original force histories, controller code or measured signals used.
"""
import csv
import math
from pathlib import Path


def main():
    mass, cf, cr, f, b, speed, preview = 13650, 250000, 450000, 3.7, 2.2, 25, 25
    wheelbase = f + b
    kus = mass / wheelbase * (b / cf - f / cr)
    B = wheelbase + kus * speed**2
    ky, kpsi = 2 * B / preview**2, 2 * B / preview
    # Independently substitute derived steady-turn values into printed Eqs4-5.
    radius = 1000.0  # synthetic check, not a paper manoeuvre
    rate = speed / radius
    delta = B / radius
    vy = (mass * speed * rate - (cr*b-cf*f)*rate/speed - cf*delta) * (-speed/(cf+cr))
    force_residual = -(cf+cr)*vy/speed + (cr*b-cf*f)*rate/speed + cf*delta - mass*speed*rate
    moment_residual = (cr*b-cf*f)*vy/speed - (cf*f*f+cr*b*b)*rate/speed + f*cf*delta
    assert abs(force_residual) < 1e-8 and abs(moment_residual) < 1e-8
    assert round(math.degrees(ky), 1) == 1.2
    assert round(math.degrees(kpsi), 1) == 30.9
    # Eq8-10 circle residual at four synthetic signed states, independent of Eq12.
    max_relative_circle_residual = 0.0
    for y, psi in [(1., .01), (-1., -.01), (.3, -.04), (-.3, .04)]:
        curvature = -2*(preview*math.sin(psi)+y*math.cos(psi))/(preview**2+y*y)
        R = 1/curvature
        xc, yc, xt, yt = 0., y, preview, 0.
        x0, y0 = xc-R*math.sin(psi), yc+R*math.cos(psi)
        resid = abs((x0-xc)**2+(yc-y0)**2 - ((xt-x0)**2+(yt-y0)**2))/R**2
        max_relative_circle_residual = max(max_relative_circle_residual, resid)
    assert max_relative_circle_residual < 1e-12
    # Positive y, zero psi requires negative curvature under the printed definitions.
    assert -2/(preview**2+1) < 0 < ky
    length_ratio, velocity_ratio = 8., 25/91.6  # full/model
    time_ratio = length_ratio/velocity_ratio
    dt_model = 6e-5
    dt_full = dt_model*time_ratio
    st_model = (12.2/8)/(91.6*dt_model)
    st_full = 12.2/(25*dt_full)
    assert math.isclose(st_model, st_full, rel_tol=1e-12)
    # Coefficient invariance at synthetic unit model force and moment; equal density.
    force_ratio = velocity_ratio**2 * length_ratio**2
    moment_ratio = force_ratio * length_ratio
    assert math.isclose(force_ratio/(25**2*64), 1/(91.6**2), rel_tol=1e-12)
    assert math.isclose(moment_ratio/(25**2*64*8), 1/(91.6**2), rel_tol=1e-12)
    values = [
        ('Kus_rad_per_m_s2', kus, 'steady-turn reduction of Eqs4-5;linear tyres;zero aero;Table1'),
        ('ky_rad_per_m', ky, 'Eq14 magnitude;not deployed controller gain'),
        ('kpsi_rad_per_rad', kpsi, 'Eq13 magnitude;not deployed controller gain'),
        ('ky_deg_per_m', math.degrees(ky), 'conditional degree-output conversion;rounds to Table2 1.2'),
        ('kpsi_deg_per_rad', math.degrees(kpsi), 'conditional degree-output/radian-input conversion;rounds to Table2 30.9'),
        ('full_over_model_time', time_ratio, 'Eq3 St invariance;Lratio8;Uratio25/91.6'),
        ('fullscale_step_s', dt_full, 'derived not reported implemented step'),
        ('full_over_model_force_equal_density', force_ratio, 'equal Cs;geometrically similar area;equal density'),
        ('full_over_model_moment_equal_density', moment_ratio, 'equal Cyaw;corresponding reference point required'),
        ('fullscale_2500_steps_s', 2500*dt_full, 'uses approximate reported step count;not exact event duration'),
        ('nominal_fullscale_ramp_s', 1.5*12.2/25, '1.5L/25m/s;not gust origin proof'),
        ('nominal_half_ramp_s', .75*12.2/25, 'near reported0.37s;only consistency clue'),
        ('nominal_CG_forward_shift_63_to_43_m', .20*5.9, 'rounded percent positions;body-axis transform still needed'),
        ('nominal_CG_forward_shift_63_to_23_m', .40*5.9, 'rounded percent positions;not new measured geometry'),
        ('max_relative_circle_residual', max_relative_circle_residual, 'four synthetic signed geometric states;not experimental validation'),
    ]
    out = Path(__file__).resolve().parents[1] / 'learning/audits/winkler_2016_arithmetic.csv'
    with out.open('w', encoding='utf-8', newline='') as stream:
        writer=csv.writer(stream)
        writer.writerow(['quantity','derived_value','provenance_and_limit'])
        for name,value,note in values: writer.writerow([name,f'{value:.12g}','ANALYST_INFERENCE: '+note])
    print(f'{len(values)} derived rows; steady-bicycle residual, circle geometry and scale invariance checks passed.')


if __name__ == '__main__':
    main()
