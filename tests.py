import os

from distance_checker import DistanceChecker

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


def test_gun_distance():
    test_distance_away = 1
    distance_checker = DistanceChecker(file_path=test_file_path, minimum_gun_distance_away=test_distance_away)
    assert True is distance_checker.gun_is_too_close(test_distance_away - 1)
    assert True is distance_checker.gun_is_too_close(test_distance_away)
    assert False is distance_checker.gun_is_too_close(test_distance_away + 1)
