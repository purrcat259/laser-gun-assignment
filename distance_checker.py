import json
import argparse

speed_of_light = 299792458  # metres per second
default_minimum_gun_distance = 112000


class DistanceChecker:
    def __init__(self, file_path, minimum_gun_distance_away=default_minimum_gun_distance):
        self.file_path = file_path
        self.minimum_gun_distance_away = minimum_gun_distance_away
        self.data = []

    def run(self):
        print('Loading in data')
        self.load_data()
        print('Calculating valid guns from {} guns at least {} metres away'.format(len(self.data), self.minimum_gun_distance_away))
        valid_guns = self.get_valid_guns()
        if len(valid_guns) > 0:
            print('Valid guns:')
            for gun in valid_guns:
                print('> Gun: {} is {} metres away'.format(gun['name'], gun['distance']))
        else:
            print('> No guns were within the valid range')

    def load_data(self):
        with open(self.file_path, 'r') as data_file:
            for line in data_file:
                # remove the new line
                data_line = line.replace('\n', '')
                # parse the JSON object into a key-value map
                self.data.append(json.loads(data_line))

    def gun_is_too_close(self, distance):
        return distance <= self.minimum_gun_distance_away

    # Assumes both timestamps are in nanoseconds
    def calculate_gun_distance(self, start_timestamp, end_timestamp):
        turnaround_time = end_timestamp - start_timestamp
        # turnaround time involves both the time taken to travel to the reflector and back
        # since we assume that the speed of light remains constant, the time to the reflector and the time back can be
        # safely assumed to be equal
        time_to_reflector = turnaround_time / 2
        # time to reflector is in nanoseconds and needs to be converted to seconds
        # for the distance calculation to be in metres
        time_to_reflector /= 1000000000
        distance_to_reflector = speed_of_light * time_to_reflector
        return distance_to_reflector

    def get_valid_guns(self):
        valid_guns = []
        for gun in self.data:
            distance = self.calculate_gun_distance(
                start_timestamp=gun['t0'],
                end_timestamp=gun['t1']
            )
            # add in the distance for printing later
            gun['distance'] = distance
            if not self.gun_is_too_close(distance=distance):
                valid_guns.append(gun)
        return valid_guns


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Laser Gun Assignment. Find all guns over a specified distance'
    )
    parser.add_argument(
        '-file-path',
        action='store',
        dest='file_path',
        required=True,
        help='The path to the file specifying the guns to be checked'
    )
    parser.add_argument(
        '-minimum-distance',
        action='store',
        default=default_minimum_gun_distance,
        dest='minimum_distance',
        type=int,
        help='The minimum distance a gun has to be away from the reflector')
    args = parser.parse_args()
    distance_checker = DistanceChecker(file_path=args.file_path, minimum_gun_distance_away=args.minimum_distance)
    distance_checker.run()
