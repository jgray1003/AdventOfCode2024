import math
from Common import common_functions

class day_2_puzzles:
    def __init__(self):
        self.input_file_name = 'day_2.txt'
        self.input_lines = common_functions.read_file(self.input_file_name, example_file=False)
        self.reports_list = self.__construct_report_lists()
        self.safe_reports = 0

    def __construct_report_lists(self):
        reports_list = []

        for line in self.input_lines:
            reports_list.append(common_functions.convert_strs_to_ints(line.split()))

        return reports_list

    def puzzle_1(self):
        self.safe_reports = 0
        for levels in self.reports_list:
            self.safe_reports += self.__test_report(levels)

        return self.safe_reports

    def puzzle_2(self):
        print(self.__test_report([11, 12, 13, 11, 10], True))
        self.safe_reports = 0

        #for levels in self.reports_list:
        #    self.safe_reports += self.__test_report(levels, allow_mistake=True)

        return self.safe_reports

    def __test_report(self, levels, allow_mistake=False):
        prev_increasing = None

        for i in range(0, len(levels) - 1):
            seq_1 = levels[i]
            seq_2 = levels[i + 1]
            increasing = seq_2 > seq_1

            if prev_increasing is None:
                prev_increasing = increasing

            if prev_increasing != increasing or seq_1 == seq_2 or math.fabs(seq_1 - seq_2) > 3:
                if allow_mistake is False:
                    return 0

                remove_first = self.__test_report(levels[:i] + levels[i + 1:], allow_mistake=False)
                if remove_first == 1:
                    return 1

                remove_second = self.__test_report(levels[:i + 1] + levels[i + 2:], allow_mistake=False)
                if remove_second == 1:
                    return 1

                if not remove_first and not remove_second:
                    return 0

            prev_increasing = increasing

        return 1


