import math
import re
from Common import common_functions as cf
from Common import orthogonality as orth

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_4.txt'
        self.word_search = cf.read_file_to_2D_array(self.input_file_name, example_file=False)
        self.word_search_row_len = len(self.word_search)
        self.word_search_col_len = len(self.word_search[0])

    def __search_direction(self, row, col, word, direction):
        meets_len_requirement = False
        word_len = len(word)

        match direction:
            case orth.Orthogonality.UP:
                meets_len_requirement = row + 1 >= word_len
            case orth.Orthogonality.UPRIGHT:
                meets_len_requirement = row + 1 >= word_len and self.word_search_col_len - col >= word_len
            case orth.Orthogonality.RIGHT:
                meets_len_requirement = self.word_search_col_len - col >= word_len
            case orth.Orthogonality.DOWNRIGHT:
                meets_len_requirement = self.word_search_row_len - row >= word_len and self.word_search_col_len - col >= word_len
            case orth.Orthogonality.DOWN:
                meets_len_requirement = self.word_search_row_len - row >= word_len
            case orth.Orthogonality.DOWNLEFT:
                meets_len_requirement = self.word_search_row_len - row >= word_len and col + 1 >= word_len
            case orth.Orthogonality.LEFT:
                meets_len_requirement = col + 1 >= word_len
            case orth.Orthogonality.UPLEFT:
                meets_len_requirement = row + 1 >= word_len and col + 1 >= word_len

        if not meets_len_requirement:
            return 0

        for i in range(word_len):
            if self.word_search[row][col] == word[i]:
                if i == word_len - 1:
                    break
                match direction:
                    case orth.Orthogonality.UP:
                        row -= 1
                    case orth.Orthogonality.UPRIGHT:
                        row -= 1
                        col += 1
                    case orth.Orthogonality.RIGHT:
                        col += 1
                    case orth.Orthogonality.DOWNRIGHT:
                        row += 1
                        col += 1
                    case orth.Orthogonality.DOWN:
                        row += 1
                    case orth.Orthogonality.DOWNLEFT:
                        row += 1
                        col -= 1
                    case orth.Orthogonality.LEFT:
                        col -= 1
                    case orth.Orthogonality.UPLEFT:
                        row -= 1
                        col -= 1
            else:
                return 0

        return 1

    def __search(self, words_to_find, directions):
        word_counts_found = dict([(word, 0) for word in words_to_find])

        for word in words_to_find:
            for row_i in range(self.word_search_row_len):
                for col_i in range(self.word_search_col_len):
                    for direction in directions:
                        word_counts_found[word] += self.__search_direction(row_i, col_i, word, direction)

        return word_counts_found

    def puzzle_1(self):
        words_to_find = ['XMAS']

        directions = [orth.Orthogonality.UP,
                      orth.Orthogonality.UPRIGHT,
                      orth.Orthogonality.RIGHT,
                      orth.Orthogonality.DOWNRIGHT,
                      orth.Orthogonality.DOWN,
                      orth.Orthogonality.DOWNLEFT,
                      orth.Orthogonality.LEFT,
                      orth.Orthogonality.UPLEFT]

        word_counts_found = self.__search(words_to_find, directions)
        return word_counts_found

    def puzzle_2(self):
        x_mas_count = 0
        ms = ['M', 'S']
        for row_i in range(1, self.word_search_row_len - 1):
            for col_i in range(1, self.word_search_col_len - 1):
                if self.word_search[row_i][col_i] != 'A':
                    continue
                top_left_corner = self.word_search[row_i - 1][col_i - 1]
                top_right_corner = self.word_search[row_i - 1][col_i + 1]
                bottom_right_corner = self.word_search[row_i + 1][col_i + 1]
                bottom_left_corner = self.word_search[row_i + 1][col_i - 1]

                first_diag_legitimate = top_left_corner in ms and bottom_right_corner in ms \
                    and top_left_corner != bottom_right_corner
                second_diag_legitimate = top_right_corner in ms and bottom_left_corner in ms \
                    and top_right_corner != bottom_left_corner

                if first_diag_legitimate and second_diag_legitimate:
                    x_mas_count += 1

        return x_mas_count
