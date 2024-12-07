import math
import re
from Common import common_functions

class day_2_puzzles:
    def __init__(self):
        self.input_file_name = 'day_3.txt'
        self.input_lines = common_functions.read_file(self.input_file_name, example_file=False)

    def puzzle_1(self):
        mul_summation = 0
        three_digit_re = r'[\d]{1,3}'
        line_re = rf'mul\({three_digit_re},{three_digit_re}\)'
        for line in self.input_lines:
            matches = re.finditer(line_re, line)

            for match in matches:
                digit_matches = re.findall(three_digit_re, match.group(0))
                mul_summation += int(digit_matches[0]) * int(digit_matches[1])
        return mul_summation

    def puzzle_2(self):
        mul_summation = 0
        three_digit_re = r'[\d]{1,3}'
        line_re = rf'mul\({three_digit_re},{three_digit_re}\)'
        line_complete = ''

        for line in self.input_lines:
            line_complete += line

        mul_matches = re.finditer(line_re, line_complete)
        mul_enabled_matches = re.finditer(r'do\(\)', line_complete)
        mul_disabled_matches = re.finditer(r'don\'t\(\)', line_complete)
        mul_enabled_indexes = [m.end() for m in mul_enabled_matches]
        mul_disabled_indexes = [m.end() for m in mul_disabled_matches]

        for mul_match in mul_matches:
            mul_start_index = mul_match.start()

            #if mul_start_index < mul_disabled_indexes[0]:
            #    mul_enabled = True
            #else:
            closest_prior_enable = 0
            closest_prior_disable = -1

            for i in mul_enabled_indexes:
                if i < mul_start_index:
                    closest_prior_enable = i
                else:
                    break
            for i in mul_disabled_indexes:
                if i < mul_start_index:
                    closest_prior_disable = i
                else:
                    break
            mul_enabled = (mul_start_index - closest_prior_enable) < (mul_start_index - closest_prior_disable) and closest_prior_disable != -1

            if mul_enabled:
                digit_matches = re.findall(three_digit_re, mul_match.group(0))
                if digit_matches[0] == '469' and digit_matches[1] == '12':
                    a = 5
                #print(digit_matches[0], digit_matches[1])
                mul_summation += int(digit_matches[0]) * int(digit_matches[1])
            else:
                pass
                #print(mul_match.group(0))
        return mul_summation # 94818616 too high, 94817002 too. 58905534 too low. 83581990, 90800770, 87375218 wrong. f