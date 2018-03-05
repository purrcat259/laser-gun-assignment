import os
import pytest

from distance_checker import DistanceChecker, speed_of_light

current_directory = os.path.dirname(os.path.realpath(__file__))
data_directory = os.path.join(current_directory, 'data')
test_file_path = os.path.join(data_directory, 'test.in')


def test_file_loading():
    distance_checker = DistanceChecker(file_path=test_file_path)
    distance_checker.load_data()
    # the test file should only return 2 dictionaries
    assert 2 == len(distance_checker.data)
    for data in distance_checker.data:
        assert isinstance(data, dict)


def test_minimum_gun_distance_check():
    test_distance_away = 1
    distance_checker = DistanceChecker(file_path=test_file_path, minimum_gun_distance_away=test_distance_away)
    assert True is distance_checker.gun_is_too_close(test_distance_away - 1)
    assert True is distance_checker.gun_is_too_close(test_distance_away)
    assert False is distance_checker.gun_is_too_close(test_distance_away + 1)


@pytest.mark.parametrize('expected_distance', [
    10,
    100,
    1000,
    1000.0,
    100.101
])
def test_gun_distance(expected_distance):
    expected_required_time = expected_distance / speed_of_light  # seconds
    # this time needs to be doubled, since it is a turnaround time and not just the time from the gun to reflector
    expected_required_time *= 2
    expected_required_time *= 1000000000  # nanoseconds
    distance_checker = DistanceChecker(file_path=test_file_path)
    expected_start_time = 0
    expected_end_time = expected_start_time + expected_required_time
    actual_distance = distance_checker.calculate_gun_distance(
        start_timestamp=expected_start_time,
        end_timestamp=expected_end_time
    )
    assert expected_distance == actual_distance
