import copy
import math
from Common import common_functions as cf
from Common import dag

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

    def puzzle_2_old(self):
        incorrectly_orders_updates = []
        middle_index_sum = 0

        rules_dag = dag.DAG()

        for i in range(len(self.page_ordering_rules)):
            # parent is number that must precede child
            parent = self.page_ordering_rules[i][0]
            child = self.page_ordering_rules[i][1]

            parent_node = None
            if not rules_dag.contains_value(parent):
                parent_node = dag.DAG.Node(parent, None)
                rules_dag.add_node(parent_node)

            if not rules_dag.contains_value(child):
                child_node = dag.DAG.Node(child, parent)
                rules_dag.add_node(child_node)
            else:
                # child node has new parent
                child_node = [n for n in rules_dag.nodes if n.val == child][0]
                child_node.set_parent(parent_node)
        rules_dag.print()

        for update in self.updates:
            if not self.__valid_update(update):
                incorrectly_orders_updates.append(update)

        for update in incorrectly_orders_updates:
            update_mid_index = math.floor(len(update) / 2)
            num_pages_prior_mid = update_mid_index
            # find page that is midindex layers deep
            sum = 0
            for node in rules_dag.nodes:
                for page in update:
                    page_depth = 0
                    if node.val == page:
                        tmp_node = copy.deepcopy(node)
                        while tmp_node.parent is not None:
                            if tmp_node.val in update:
                                page_depth += 1
                                tmp_node = copy.deepcopy(tmp_node.parent)
                    if page_depth == update_mid_index:
                        sum += page
            print(sum)
            res = 0

            print(res)


            middle_index_sum += update[math.floor(len(update) / 2)]

        return middle_index_sum
