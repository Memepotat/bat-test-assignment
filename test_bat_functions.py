# test_bat_functions.py

import pytest
import bat_functions

# Exercise 1: Basic Tests and Parametrization

def test_calculate_bat_power_basic():
    assert bat_functions.calculate_bat_power(1) == 42
    assert bat_functions.calculate_bat_power(0) == 0
    assert bat_functions.calculate_bat_power(5) == 210
    assert bat_functions.calculate_bat_power(-1) == -42

@pytest.mark.parametrize(
    "distance,expected_strength",
    [
        (0, 100),
        (5, 50),
        (10, 0),
        (12, 0),  # Should not go below 0
        (7.5, 25),
    ]
)
def test_signal_strength_parametrized(distance, expected_strength):
    assert bat_functions.signal_strength(distance) == expected_strength

# Exercise 2: Using Fixtures

@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    for name, specs in bat_vehicles.items():
        assert bat_functions.get_bat_vehicle(name) == specs

def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError) as excinfo:
        bat_functions.get_bat_vehicle("Batboat")
    assert "Unknown vehicle" in str(excinfo.value)

# Exercise 3: Mocking External Dependencies

def test_fetch_joker_info_mock(monkeypatch):
    mock_data = {'mischief_level': 0, 'location': 'captured'}

    def mock_fetch():
        return mock_data

    monkeypatch.setattr(bat_functions, "fetch_joker_info", mock_fetch)
    assert bat_functions.fetch_joker_info() == mock_data
