from datetime import datetime

from simple_agents import add_numbers, current_utc_time


def test_add_numbers() -> None:
    assert add_numbers(2, 3) == 5
    assert add_numbers(1.5, 2.25) == 3.75


def test_current_utc_time() -> None:
    value = current_utc_time()

    parsed = datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC")
    assert parsed.year >= 2025
