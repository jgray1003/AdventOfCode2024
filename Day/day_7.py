import math
from Common import common_functions as cf

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_7.txt'
        self.input = cf.read_file(self.input_file_name, example_file=False)
        self.results = []
        self.constants = []
        self.operators = ['+', '*']
        self.operators_extended = ['+', '*', '||']
        self.__parse_input()
        self.current_result = 0
        self.current_constants = []

    def __parse_input(self):
        for line in self.input:
            line = cf.trim_newlines(line)
            parts = line.split(':')
            self.results.append(int(parts[0]))
            self.constants.append(cf.convert_strs_to_ints(parts[1][1:].split(' ')))

    def __recurse_operator_options(self, operators_extended:bool,
                                   running_result:int, index:int, solution_found:bool):
        if index == len(self.current_constants) - 1:
            return False

        constant = running_result
        next_constant = self.current_constants[index + 1]

        if operators_extended:
            operators = self.operators_extended
        else:
            operators = self.operators

        for operator in operators:
            result = 0
            if operator == '+':
                result = constant + next_constant
            elif operator == '*':
                result = constant * next_constant
            elif operator == '||':
                result = int(f'{constant}{next_constant}')

            index += 1
            if result == self.current_result and index == len(self.current_constants) - 1:
                return True
            result = self.__recurse_operator_options(operators_extended, result, index, False)
            if not result:
                index -= 1
            else:
                return True
        return False


    def puzzle_1(self):
        solved_sum = 0
        for i in range(len(self.results)):
            self.current_result = self.results[i]
            self.current_constants = self.constants[i]

            equation_solved = self.__recurse_operator_options(False, self.current_constants[0], 0, False)
            if equation_solved:
                solved_sum += self.current_result
        return solved_sum

    def puzzle_2(self):
        solved_sum = 0
        for i in range(len(self.results)):
            self.current_result = self.results[i]
            self.current_constants = self.constants[i]
            if self.current_result == 156:
                a = 54
            equation_solved = self.__recurse_operator_options(True, self.current_constants[0], 0, False)
            if equation_solved:
                solved_sum += self.current_result
        return solved_sum

