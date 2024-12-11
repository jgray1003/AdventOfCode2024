import math
from Common import common_functions as cf

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_8.txt'
        self.map = cf.read_file_to_2D_array(self.input_file_name, example_file=False)
        self.antenna_freq_locations = {}
        self.__construct_antenna_frequency_locations()

    def __construct_antenna_frequency_locations(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                char = self.map[x][y]
                if char == '.':
                    continue
                if char not in self.antenna_freq_locations.keys():
                    self.antenna_freq_locations[char] = [(x, y)]
                else:
                    self.antenna_freq_locations[char].append((x, y))
        pass

    # Euclidean distance between two points, diff. in y over diff. in x
    def __get_distance(self, antenna_one: tuple, antenna_two: tuple):
        return math.fabs((antenna_two[1] - antenna_one[1]) / (antenna_two[0] - antenna_one[0]))

    # Rise over run, rise being row. +/- for up/down
    def __get_slope(self, antenna_one: tuple, antenna_two: tuple):
        return antenna_two[0] - antenna_one[0], antenna_two[1] - antenna_one[1]

    def __in_grid(self, antibody: tuple):
        x_max = len(self.map[0])
        y_max = len(self.map)

        return 0 <= antibody[0] < y_max and 0 <= antibody[1] < x_max

    def puzzle_1(self):
        antinode_locations = []

        for antenna_freq, locations in self.antenna_freq_locations.items():
            for i in range(len(locations) - 1):
                j = i + 1
                while j < len(locations):
                    slope_delta_y, slope_delta_x = self.__get_slope(locations[i], locations[j])

                    antibody_locs = [(locations[i][0] - slope_delta_y, locations[i][1] - slope_delta_x),
                                     (locations[j][0] + slope_delta_y, locations[j][1] + slope_delta_x)]

                    for antibody_loc in antibody_locs:
                        if antibody_loc not in antinode_locations and self.__in_grid(antibody_loc):
                            antinode_locations.append(antibody_loc)

                    j += 1
        return len(antinode_locations)

    def puzzle_2(self):
        antinode_locations = []

        for antenna_freq, locations in self.antenna_freq_locations.items():
            for i in range(len(locations) - 1):
                j = i + 1
                while j < len(locations):
                    slope_delta_y, slope_delta_x = self.__get_slope(locations[i], locations[j])
                    antenna_antinode_locs = [locations[i], locations[j]]

                    first_antinode = True
                    for loc in antenna_antinode_locs:
                        if loc not in antinode_locations:
                            antinode_locations.append(loc)
                        if first_antinode:
                            antinode_span = (loc[0] - slope_delta_y, loc[1] - slope_delta_x)
                            while self.__in_grid(antinode_span):
                                if antinode_span not in antinode_locations:
                                    antinode_locations.append(antinode_span)
                                antinode_span = (antinode_span[0] - slope_delta_y, antinode_span[1] - slope_delta_x)
                            first_antinode = False
                        else:
                            antinode_span = (loc[0] + slope_delta_y, loc[1] + slope_delta_x)

                            while self.__in_grid(antinode_span):
                                if antinode_span not in antinode_locations:
                                    antinode_locations.append(antinode_span)
                                antinode_span = (antinode_span[0] + slope_delta_y, antinode_span[1] + slope_delta_x)

                    j += 1

        return len(antinode_locations)
