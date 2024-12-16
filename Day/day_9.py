import copy
import math
from Common import common_functions as cf


class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_9.txt'
        self.disk_map = cf.read_file(self.input_file_name, line_by_line=False, example_file=True)
        self.reformatted_disk = []

    def __construct_reformatted_disk(self, append:bool):
        self.reformatted_disk = []
        file_id = 0
        for i in range(len(self.disk_map)):
            disk_items = [str(file_id) if i % 2 == 0
                          else '.' for _ in range(int(self.disk_map[i]))]
            if append:
                self.reformatted_disk.append(disk_items)
            else:
                self.reformatted_disk.extend(disk_items)

            file_id += 1 if i % 2 == 0 else 0
            if len(self.reformatted_disk[-1]) == 0:
                self.reformatted_disk.pop()

    def puzzle_1(self):
        self.__construct_reformatted_disk(False)

        space_index = 0
        file_block_index = len(self.reformatted_disk) - 1

        while file_block_index >= 0:
            if self.reformatted_disk[file_block_index] == '.':
                file_block_index -= 1
                continue

            for i in range(space_index, len(self.reformatted_disk)):
                if self.reformatted_disk[i] == '.':
                    space_index = i
                    break

            self.reformatted_disk[space_index] = self.reformatted_disk[file_block_index]
            self.reformatted_disk[file_block_index] = '.'

            if self.reformatted_disk[space_index:].count('.') == len(self.reformatted_disk) - file_block_index:
                break

            file_block_index -= 1

        checksum = 0
        for i in range(len(self.reformatted_disk)):
            if self.reformatted_disk[i] == '.':
                break

            checksum += i * int(self.reformatted_disk[i])

        return checksum

    def puzzle_2(self):
        self.__construct_reformatted_disk(False)

        file_block_index = len(self.reformatted_disk) - 1

        while file_block_index >= 0:
            if self.reformatted_disk[file_block_index] == '.':
                file_block_index -= 1
                continue

            file_block_index_end = file_block_index

            while self.reformatted_disk[file_block_index] == self.reformatted_disk[file_block_index_end]:
                file_block_index -= 1

            file_block_len = file_block_index_end - file_block_index
            file_block_index += 1

            for i in range(len(self.reformatted_disk)):
                if i > file_block_index_end - file_block_len:
                    break
                if self.reformatted_disk[i] != '.':
                    continue

                space_start = i
                tmp_i = i + 1

                while tmp_i < len(self.reformatted_disk) and self.reformatted_disk[tmp_i] == '.':
                    tmp_i += 1

                space_len = tmp_i - space_start

                if file_block_len <= space_len:
                    for j in range(file_block_len):
                        self.reformatted_disk[space_start] = self.reformatted_disk[file_block_index_end]
                        self.reformatted_disk[file_block_index_end] = '.'
                        file_block_index_end -= 1
                        space_start += 1
                    break

            file_block_index -= 1

        checksum = 0
        for i in range(len(self.reformatted_disk)):
            if self.reformatted_disk[i] == '.':
                continue

            checksum += i * int(self.reformatted_disk[i])

        return checksum
