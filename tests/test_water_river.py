import pytest
from render import water_river as mod

CASES = [
    ("speed_half", "m.flow_speed(2.0, 0.5) == approx(1.0)"),
    ("speed_start", "m.flow_speed(2.0, 0.0) == approx(2.0)"),
    ("width_grow", "m.river_width(2.0, 0.5) == approx(3.0)"),
    ("width_zero", "m.river_width(2.0, 0.0) == approx(2.0)"),
    ("foam_grow", "m.foam_density(2.0) > m.foam_density(1.0)"),
    ("buoy_count", "m.buoyancy_points([(0, 0), (1, 1)]) == 2"),
    ("underwater_true", "m.cull_underwater(1.0) is True"),
    ("underwater_false", "m.cull_underwater(-1.0) is False"),
    ("tangent_keep", "m.flow_tangent((1.0, 0.0), (0.0, 1.0)) == (1.0, 0.0)"),
    ("shallow_value", "m.shallow_depth(2.0) == approx(2.0)"),
    ("shore_inner", "m.shoreline_blend(0.0, 2.0) == approx(1.0)"),
    ("shore_outer", "m.shoreline_blend(2.0, 2.0) == approx(0.0)"),
    ("lod_mid", "m.lod_seam(1.0, 3.0, 0.5) == approx(2.0)"),
    ("flow_equal", "m.flow_conservation(2.0, 2.0) == approx(0.0)"),
    ("flow_diff", "m.flow_conservation(2.0, 3.0) == approx(1.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
