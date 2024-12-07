import math
import re
from Common import common_functions

class day_3_puzzles:
    def __init__(self):
        self.input_file_name = 'day_3.txt'
        self.input = common_functions.read_file(self.input_file_name, line_by_line=False, example_file=False)

    def puzzle_1(self):
        mul_summation = 0
        three_digit_re = r'[\d]{1,3}'
        line_re = rf'mul\({three_digit_re},{three_digit_re}\)'
        matches = re.finditer(line_re, self.input)

        for match in matches:
            digit_matches = re.findall(three_digit_re, match.group(0))
            mul_summation += int(digit_matches[0]) * int(digit_matches[1])

        return mul_summation

    def puzzle_2(self):
        mul_summation = 0
        three_digit_re = r'[\d]{1,3}'
        line_re = rf'mul\({three_digit_re},{three_digit_re}\)'

        mul_matches = dict([(m.start(), m.group(0)) for m in re.finditer(line_re, self.input)])
        mul_match_indexes = [m.start() for m in re.finditer(line_re, self.input)]
        mul_enabled_indexes = [m.end() for m in re.finditer(r'do\(\)', self.input)]
        mul_disabled_indexes = [m.end() for m in re.finditer(r'don\'t\(\)', self.input)]

        mul_enabled = True
        for running_index in range(len(self.input)):
            if running_index in mul_disabled_indexes:
                mul_enabled = False
            elif running_index in mul_enabled_indexes:
                mul_enabled = True

            if mul_enabled and running_index in mul_match_indexes:
                match = mul_matches[running_index]
                digit_matches = re.findall(three_digit_re, match)
                mul_summation += int(digit_matches[0]) * int(digit_matches[1])

        return mul_summation
