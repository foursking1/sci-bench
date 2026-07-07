from repro_eval.assertions import evaluate_condition


def test_evaluate_condition_supports_actual_and_target_aliases():
    assert evaluate_condition("actual > target", actual=132.1, target=100.0, tolerance_abs=0.0, tolerance_pct=0.0)
    assert not evaluate_condition("actual < target", actual=132.1, target=100.0, tolerance_abs=0.0, tolerance_pct=0.0)

