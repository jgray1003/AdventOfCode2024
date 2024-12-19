import copy
import math
from Common import common_functions as cf
from Common import orthogonality as orth

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_11.txt'
        self.input = cf.read_file(self.input_file_name, line_by_line=False, example_file=False)
        self.stone_line = cf.convert_strs_to_ints(self.input.split(' '))
        self.orig_stone_line = copy.deepcopy(self.stone_line)
        self.num_blink = 0
        self.rule_result_set = [
            (lambda x: x == 0, lambda x: [x + 1]),
            (lambda x: len(str(x)) % 2 == 0,
             lambda x: [int(str(x)[:int(len(str(x)) / 2)]), int(str(x)[int(len(str(x)) / 2):])]),
            (lambda x: True, lambda x: [x * 2024])
        ]
        self.terminal_stone_count = 0
        self.cache = {}

    class Stone:
        def __init__(self, value:int, layer:int, term_count:int):
            self.value = value
            self.val_str = str(self.value)
            self.layer = layer
            self.parent = None
            self.terminal_node_count = term_count

    def __process_stone(self, stone:int):
        #if stone in self.cache:
        #    return self.cache[stone]

        # if stone == 0:
        #     return [1]
        # if len(str(stone)) % 2 == 0:
        #     return [int(str(stone)[:int(len(str(stone)) / 2)]), int(str(stone)[int(len(str(stone)) / 2):])]
        # return [stone * 2024]
        for rule_res in self.rule_result_set:
            if rule_res[0](stone):
                resulting_stones = rule_res[1](stone)
                #self.cache[stone] = resulting_stones
                return resulting_stones

    def __recurse_stone(self, stone:int, layer:int):

        if layer == self.num_blink:
            return 1

        if (stone, layer) in self.cache:
            return self.cache[(stone, layer)]

        resulting_stone_counts = []
        for child in self.__process_stone(stone):
            resulting_stone_counts.append(self.__recurse_stone(child, layer + 1))

        resulting_stone_counts_sum = sum(resulting_stone_counts)

        self.cache[(stone, layer)] = resulting_stone_counts_sum

        return resulting_stone_counts_sum


    def puzzle_1(self):
        self.num_blink = 25

        for i in range(self.num_blink):
            resulting_stone_line = []

            for stone in self.stone_line:
                resulting_stone_line.extend(self.__process_stone(stone))

            self.stone_line = copy.deepcopy(resulting_stone_line)

        return len(self.stone_line)

    def puzzle_2(self):
        self.stone_line = copy.deepcopy(self.orig_stone_line)
        self.num_blink = 75
        terminal_stones_length = 0

        for stone in self.stone_line:
            terminal_stones_length += self.__recurse_stone(stone, 0)

        return terminal_stones_length

