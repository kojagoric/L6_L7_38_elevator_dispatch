from elevator_dispatch import next_direction, door_action, pick_elevator


def test_direction_up_with_requests_above():
    assert next_direction(3, "up", [5]) == "up"


def test_direction_up_only_requests_below():
    assert next_direction(3, "up", [1]) == "down"


def test_direction_up_without_requests():
    assert next_direction(3, "up", []) == "idle"


def test_direction_down_with_requests_below():
    assert next_direction(3, "down", [1]) == "down"


def test_direction_down_only_requests_above():
    assert next_direction(3, "down", [5]) == "up"


def test_direction_down_without_requests():
    assert next_direction(3, "down", []) == "idle"


def test_direction_unspecified_with_requests_above():
    assert next_direction(3, "idle", [5]) == "up"


def test_direction_unspecified_with_requests_below():
    assert next_direction(3, "idle", [1]) == "down"


def test_direction_unspecified_without_requests():
    assert next_direction(3, "idle", []) == "idle"


def test_emergency_holds_doors():
    assert door_action(700, True, True) == "hold_open"


def test_overload():
    assert door_action(631, False, False) == "overload"


def test_blocked_door_reopens():
    assert door_action(500, True, False) == "reopen"


def test_normal_door_closes():
    assert door_action(500, False, False) == "close"


def test_pick_nearest_idle_elevator():
    cars = [("A", 1, True), ("B", 8, True)]
    assert pick_elevator(cars, 2) == "A"


def test_moving_elevator_gets_penalty():
    cars = [("A", 3, False), ("B", 7, True)]
    assert pick_elevator(cars, 2) == "B"


def test_first_elevator_wins_equal_gap():
    cars = [("A", 2, True), ("B", 4, True)]
    assert pick_elevator(cars, 3) == "A"


def test_no_elevators():
    assert pick_elevator([], 3) is None