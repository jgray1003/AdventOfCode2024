import math
from Common import common_functions

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_1.txt'
        self.input_lines = common_functions.read_file(self.input_file_name)
        self.historian_lists = []
        self.__construct_historian_lists()

    def __construct_historian_lists(self):
        self.historian_lists.append([])
        self.historian_lists.append([])

        for line in self.input_lines:
            list_1_location_id, list_2_location_id = line.split()
            self.historian_lists[0].append(int(list_1_location_id))
            self.historian_lists[1].append(int(list_2_location_id))


    def puzzle_1(self):
        diff_sum = 0

        historian_list_1_sort = sorted(self.historian_lists[0])
        historian_list_2_sort = sorted(self.historian_lists[1])

        for i in range(len(historian_list_1_sort)):
            diff_sum += math.fabs(historian_list_1_sort[i] - historian_list_2_sort[i])

        return int(diff_sum)

    def puzzle_2(self):
        similarity_score = 0
        historian_list_2_distinct_counts = dict((x, self.historian_lists[1].count(x)) for x in self.historian_lists[1])

        for item in self.historian_lists[0]:
            if item in historian_list_2_distinct_counts:
                similarity_score += item * historian_list_2_distinct_counts[item]

        return similarity_score
