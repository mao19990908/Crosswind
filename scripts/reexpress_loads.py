"""SI load re-expression with explicit normalization, proper rotation and origins.

Analyst-derived geometry/algebra; does not recover any author's missing frame map.
Run --self-check for synthetic cases, or --input FILE --output FILE for a JSON case.
Required JSON keys: units="SI", source/target={rho,speed,area,length}, force_coeff,
moment_coeff, rotation (source to target), origin_shift_m (new minus old in target
axes), provenance. All vector components must already follow right-handed axes.
"""
import argparse
import csv
import json
import math
from pathlib import Path


def vector(v):
    if not isinstance(v, list) or len(v) != 3:
        raise ValueError('Expected three-component vector')
    if any(isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x) for x in v):
        raise ValueError('Vector must contain finite numbers')
    return v


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def mv(r, v):
    return [dot(row, v) for row in r]


def scales(spec):
    values = [spec[k] for k in ('rho', 'speed', 'area', 'length')]
    if any(isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x) or x <= 0 for x in values):
        raise ValueError('rho/speed/area/length must be finite and positive')
    rho, speed, area, length = values
    force = 0.5 * rho * speed**2 * area
    return force, force * length


def convert(case):
    if case['units'] != 'SI' or not isinstance(case['provenance'], str) or not case['provenance'].strip():
        raise ValueError('Explicit SI units and provenance required')
    r = case['rotation']
    if not isinstance(r, list) or len(r) != 3:
        raise ValueError('Expected 3x3 rotation')
    for row in r:
        vector(row)
    if any(not math.isclose(dot(r[i], r[j]), float(i == j), abs_tol=1e-10) for i in range(3) for j in range(3)):
        raise ValueError('Rotation must be orthonormal')
    if not math.isclose(dot(r[0], cross(r[1], r[2])), 1, abs_tol=1e-10):
        raise ValueError('Reflection/handedness change requires a separate verified convention')
    fs, ms = scales(case['source'])
    ft, mt = scales(case['target'])
    f = mv(r, [fs*x for x in vector(case['force_coeff'])])
    old_m = mv(r, [ms*x for x in vector(case['moment_coeff'])])
    arm = cross(vector(case['origin_shift_m']), f)
    new_m = [a-b for a, b in zip(old_m, arm)]
    result = dict(force_N=f, moment_Nm=new_m, force_coeff=[x/ft for x in f],
                  moment_coeff=[x/mt for x in new_m], provenance=case['provenance'],
                  status='ANALYST_INFERENCE; supplied conventions not independently verified')
    if not all(math.isfinite(x) for key in ('force_N', 'moment_Nm', 'force_coeff', 'moment_coeff') for x in result[key]):
        raise ValueError('Non-finite load result')
    return result


def self_check():
    identity = [[1,0,0],[0,1,0],[0,0,1]]
    spec = dict(rho=2, speed=1, area=1, length=1)
    base = dict(units='SI', source=spec, target=spec, force_coeff=[100,200,0],
                moment_coeff=[10,20,30], rotation=identity, origin_shift_m=[0,0,0],
                provenance='SYNTHETIC; not measured vehicle data')
    rows = []
    def check(name, actual, expected):
        assert len(actual) == len(expected)
        assert all(math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-9) for a,b in zip(actual,expected)), name
        rows.append([name, json.dumps(actual), json.dumps(expected), 'pass', 'SYNTHETIC'])
    check('identity', convert(base)['moment_Nm'], [10,20,30])
    shifted = dict(base, origin_shift_m=[1,0,0])
    out = convert(shifted)
    check('positive_x_origin_shift', out['moment_Nm'], [10,20,-170])
    rot = [[0,-1,0],[1,0,0],[0,0,1]]
    turn = convert(dict(base, rotation=rot))
    check('proper_90deg_rotation', turn['force_N'], [-200,100,0])
    check('proper_rotation_cross_product', cross(mv(rot,[1,2,3]),mv(rot,[4,5,6])), mv(rot,cross([1,2,3],[4,5,6])))
    dest = dict(rho=1.2,speed=20,area=2,length=4)
    forward = convert(dict(shifted, rotation=rot, target=dest))
    transpose = [list(v) for v in zip(*rot)]
    reverse = dict(base, source=dest, force_coeff=forward['force_coeff'], moment_coeff=forward['moment_coeff'],
                   rotation=transpose, origin_shift_m=mv(transpose,[-1,0,0]))
    back = convert(reverse)
    check('rotate_translate_scale_roundtrip_force', back['force_coeff'], base['force_coeff'])
    check('rotate_translate_scale_roundtrip_moment', back['moment_coeff'], base['moment_coeff'])
    check('double_reference_length_halves_Cm', convert(dict(base,target=dict(spec,length=2)))['moment_coeff'],[5,10,15])
    check('axial_to_resultant_equal_area_45deg',convert(dict(base,target=dict(spec,speed=math.sqrt(2))))['force_coeff'],[50,100,0])
    check('pure_couple_origin_independent',convert(dict(shifted,force_coeff=[0,0,0]))['moment_Nm'],[10,20,30])
    velocity, omega, d = [3,4,5], [0.1,0.2,0.3], [1,-2,3]
    shifted_rotated = convert(dict(base, rotation=rot, origin_shift_m=d))
    w_target = mv(rot, omega)
    v_target = [a+b for a,b in zip(mv(rot,velocity), cross(w_target,d))]
    check('rigid_body_power_invariance',
          [dot(shifted_rotated['force_N'],v_target)+dot(shifted_rotated['moment_Nm'],w_target)],
          [dot(base['force_coeff'],velocity)+dot(base['moment_coeff'],omega)])
    bad_cases=[dict(base,rotation=[[1,0,0],[0,1,0],[0,0,-1]]),dict(base,source=dict(spec,speed=0)),
               dict(base,origin_shift_m=[float('nan'),0,0]),dict(base,rotation=[[2,0,0],[0,1,0],[0,0,1]]),
               dict(base,units='unknown'),dict(base,provenance='')]
    for i, case in enumerate(bad_cases):
        try:
            convert(case)
        except ValueError:
            rows.append([f'reject_invalid_case_{i+1}', 'ValueError', 'ValueError', 'pass', 'SYNTHETIC'])
        else:
            raise AssertionError('Invalid metadata accepted')
    outpath = Path(__file__).resolve().parents[1]/'learning/audits/load_reexpression_checks.csv'
    with outpath.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.writer(stream)
        writer.writerow(['check','actual','expected','result','data_status'])
        writer.writerows(rows)
    print(f'Load re-expression: {len(rows)} synthetic checks passed; no author data replay.')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-check',action='store_true')
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.self_check:
        self_check()
    elif args.input and args.output:
        args.output.write_text(json.dumps(convert(json.loads(args.input.read_text(encoding='utf-8-sig'))),indent=2)+'\n',encoding='utf-8')
    else:
        parser.error('Provide --self-check or both --input and --output')
