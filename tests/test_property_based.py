from hypothesis import given
from hypothesis import strategies as st


@given(st.integers())
def test_abs_always_positive(x):
    assert abs(x) >= 0


@given(st.lists(st.integers()))
def test_sort_is_idempotent(lst):
    sorted_once = sorted(lst)
    sorted_twice = sorted(sorted_once)
    assert sorted_once == sorted_twice


@given(st.text())
def test_string_length(s):
    assert len(s) >= 0
    assert len(s + s) == 2 * len(s)


@given(st.integers(min_value=0), st.integers(min_value=0))
def test_addition_is_commutative(a, b):
    assert a + b == b + a
