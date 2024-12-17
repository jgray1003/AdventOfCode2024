import math
from Common import common_functions as cf
from Common import orthogonality as orth


class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_10.txt'
        self.topographic_map = cf.read_file_to_2D_array(self.input_file_name, example_file=False)
        self.topographic_map = cf.convert_strs_to_ints_2D(self.topographic_map)
        self.trailhead_markers = [0]
        self.trail_terminals = [9]
        self.valid_directions = [orth.Orthogonality.UP,
                                 orth.Orthogonality.RIGHT,
                                 orth.Orthogonality.DOWN,
                                 orth.Orthogonality.LEFT]

    def __recurse_directions(self, running_index:tuple[int,int], current_top_val:int, counted_terminals:list[tuple[int,int]], score:bool):
        if self.topographic_map[running_index[0]][running_index[1]] in self.trail_terminals \
                and current_top_val in self.trail_terminals:
            if (running_index not in counted_terminals and score) or not score:
                counted_terminals.append(running_index)

        #if running_index[0] == 3 and running_index[1] == 0:
        #    a = 55
        for direction in self.valid_directions:
            match direction:
                case orth.Orthogonality.UP:
                    if running_index[0] > 0:
                        new_index = (running_index[0] - 1, running_index[1])
                        if self.topographic_map[new_index[0]][new_index[1]] == current_top_val + 1:
                            self.__recurse_directions(new_index, current_top_val + 1, counted_terminals, score)
                case orth.Orthogonality.RIGHT:
                    if running_index[1] < len(self.topographic_map[0]) - 1:
                        new_index = (running_index[0], running_index[1] + 1)
                        if self.topographic_map[new_index[0]][new_index[1]] == current_top_val + 1:
                            self.__recurse_directions(new_index, current_top_val + 1, counted_terminals, score)
                case orth.Orthogonality.DOWN:
                    if running_index[0] < len(self.topographic_map) - 1:
                        new_index = (running_index[0] + 1, running_index[1])
                        if self.topographic_map[new_index[0]][new_index[1]] == current_top_val + 1:
                            self.__recurse_directions(new_index, current_top_val + 1, counted_terminals, score)
                case orth.Orthogonality.LEFT:
                    if running_index[1] > 0:
                        new_index = (running_index[0], running_index[1] - 1)
                        if self.topographic_map[new_index[0]][new_index[1]] == current_top_val + 1:
                            self.__recurse_directions(new_index, current_top_val + 1, counted_terminals,score)
        return counted_terminals

    def __get_trailhead_indices(self):
        trailhead_indices = []
        for row in range(len(self.topographic_map)):
            for col in range(len(self.topographic_map[row])):
                if self.topographic_map[row][col] in self.trailhead_markers:
                    trailhead_indices.append((row, col))
        return trailhead_indices

    def puzzle_1(self):
        total_trailhead_score = 0
        trailhead_indices = self.__get_trailhead_indices()

        for trailhead_i in trailhead_indices:
            hiking_trails = self.__recurse_directions(trailhead_i, 0, [], True)
            total_trailhead_score += len(hiking_trails)

        return total_trailhead_score

    def puzzle_2(self):
        total_trailhead_ranking = 0
        trailhead_indices = self.__get_trailhead_indices()

        for trailhead_i in trailhead_indices:
            hiking_trails_distinct = self.__recurse_directions(trailhead_i, 0, [], False)
            total_trailhead_ranking += len(hiking_trails_distinct)

        return total_trailhead_ranking
