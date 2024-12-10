import math
from Common import common_functions as cf

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_5.txt'
        self.input = cf.read_file(self.input_file_name, example_file=False)
        self.page_ordering_rules = []
        self.updates = []
        self.__parse_input()

    def __parse_input(self):
        ordering_rules = True
        for line in self.input:
            if line == '\n':
                ordering_rules = False
                continue

            if ordering_rules:
                self.page_ordering_rules.append((int(line.split('|')[0]), int(line.split('|')[1])))
            else:
                self.updates.append([int(page_num) for page_num in line.split(',')])

    def __valid_update(self, update):
        page_list_len = len(update)

        for page_list_i in range(page_list_len):
            page = update[page_list_i]
            subsequent_i = page_list_i + 1

            while subsequent_i < page_list_len:
                posterior_page = update[subsequent_i]

                for rule in self.page_ordering_rules:
                    if rule[0] == posterior_page and rule[1] == page:
                        return False
                subsequent_i += 1
        return True

    def puzzle_1(self):
        correctly_orders_updates = []
        middle_index_sum = 0

        for update in self.updates:
            if self.__valid_update(update):
                correctly_orders_updates.append(update)

        for update in correctly_orders_updates:
            middle_index_sum += update[math.floor(len(update) / 2)]

        return middle_index_sum

    def puzzle_2(self):
        middle_index_sum = 0

        for update in self.updates:
            if not self.__valid_update(update):
                ordered_update = update
                while not self.__valid_update(ordered_update):
                    for i in range(len(ordered_update)):
                        page = ordered_update[i]
                        subsequent_i = i + 1
                        swap = False
                        while subsequent_i < len(ordered_update) and not swap:

                            posterior_page = ordered_update[subsequent_i]
                            for rule in self.page_ordering_rules:
                                if rule[0] == posterior_page and rule[1] == page:
                                    ordered_update[i] = posterior_page
                                    ordered_update[subsequent_i] = page
                                    swap = True
                                elif rule[0] == page and rule[1] == posterior_page:
                                    break
                            subsequent_i += 1

                middle_index_sum += update[math.floor(len(ordered_update) / 2)]

        return middle_index_sum

