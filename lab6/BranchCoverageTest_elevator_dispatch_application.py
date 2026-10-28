from elevator_dispatch import next_direction, door_action, pick_elevator


def test_direction_branches():
    assert next_direction(3, "up", [5]) == "up"
    assert next_direction(3, "up", [1]) == "down"
    assert next_direction(3, "up", []) == "idle"
    assert next_direction(3, "down", [1]) == "down"
    assert next_direction(3, "down", [5]) == "up"
    assert next_direction(3, "down", []) == "idle"
    assert next_direction(3, "idle", [5]) == "up"
    assert next_direction(3, "idle", [1]) == "down"
    assert next_direction(3, "idle", []) == "idle"


def test_door_branches():
    assert door_action(500, False, True) == "hold_open"
    assert door_action(631, False, False) == "overload"
    assert door_action(500, True, False) == "reopen"
    assert door_action(500, False, False) == "close"


def test_elevator_selection_branches():
    assert pick_elevator([], 3) is None
    assert pick_elevator([("A", 1, True)], 2) == "A"
    assert pick_elevator([("A", 3, False), ("B", 7, True)], 2) == "B"
    assert pick_elevator([("A", 2, True), ("B", 4, True)], 3) == "A"