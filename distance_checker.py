import json

speed_of_light = 299792458  # metres per second


class DistanceChecker:
    def __init__(self, file_path, minimum_gun_distance_away=112000):
        self.file_path = file_path
        self.minimum_gun_distance_away = minimum_gun_distance_away
        self.data = []

    def load_data(self):
        with open(self.file_path, 'r') as data_file:
            for line in data_file:
                # remove the new line
                data_line = line.replace('\n', '')
                # parse the JSON object into a key-value map
                self.data.append(json.loads(data_line))

    def gun_is_too_close(self, distance):
        return distance <= self.minimum_gun_distance_away

    def calculate_gun_distance(self, start_timestamp, end_timestamp):
        turnaround_time = end_timestamp - start_timestamp
        # turnaround time involves both the time taken to travel to the reflector and back
        # since we assume that the speed of light remains constant, the time to the reflector and the time back can be
        # safely assumed to be equal
        time_to_reflector = turnaround_time / 2
        

if __name__ == '__main__':
    pass
