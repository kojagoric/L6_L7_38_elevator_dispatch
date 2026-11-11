
from hypothesis import given, strategies as st

from elevator_dispatch import (
    parse_request,
    total_travel,
    load_percent
)


@given(st.text() | st.none())
def test_parse_request_no_crash(value):
    result = parse_request(value)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
    )


@given(st.text() | st.none())
def test_total_travel_no_crash(value):
    result = total_travel(value)
    assert result is None or (
        isinstance(result, int) and result >= 0
    )


@given(st.text() | st.none())
def test_load_percent_no_crash(value):
    result = load_percent(value)
    assert result is None or (
        isinstance(result, int) and 0 <= result <= 100
    )


@given(
    st.integers(min_value=0, max_value=1000),
    st.integers(min_value=0, max_value=1000)
)
def test_parse_request_valid(start, end):
    result = parse_request(f"{start}->{end}")
    assert result == (start, end)


@given(st.lists(
    st.integers(min_value=0, max_value=1000),
    min_size=1,
    max_size=20
))
def test_total_travel_valid(floors):
    value = ",".join(map(str, floors))
    result = total_travel(value)

    expected = sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )

    assert result == expected


@given(
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=1, max_value=100000)
)
def test_load_percent_valid(load, capacity):
    if load <= capacity:
        result = load_percent(f"{load} of {capacity}")
        assert result == load * 100 // capacity


def test_invalid_inputs():
    assert parse_request("invalid") is None
    assert parse_request(None) is None

    assert total_travel("") is None
    assert total_travel("1,,3") is None

    assert load_percent("invalid") is None
    assert load_percent("100 of 0") is None
    assert load_percent("200 of 100") is None
