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
        self.safe_reports = 0

        for levels in self.reports_list:
            safe = self.__test_report(levels)
            self.safe_reports += safe

            if not safe:
                for i in range(len(levels)):
                    tmp_levels = levels.copy()
                    tmp_levels.pop(i)
                    tmp_safe = self.__test_report(tmp_levels)
                    if tmp_safe:
                        self.safe_reports += tmp_safe
                        break


        return self.safe_reports

    def __test_report(self, levels):
        prev_increasing = None

        for i in range(0, len(levels) - 1):
            seq_1 = levels[i]
            seq_2 = levels[i + 1]
            increasing = seq_2 > seq_1

            if prev_increasing is None:
                prev_increasing = increasing

            if prev_increasing != increasing or seq_1 == seq_2 or math.fabs(seq_1 - seq_2) > 3:
                return 0

            prev_increasing = increasing

        return 1


