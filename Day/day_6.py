from Common import common_functions as cf
from Common import orthogonality as orth
import copy

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_6.txt'
        self.room_map = cf.read_file_to_2D_array(self.input_file_name, example_file=False)
        self.guard_pos = (0, 0)
        self.visited_spots = [self.guard_pos]
        self.orthogonality = orth.Orthogonality.UP

    def __init_guard_pos(self):
        for row_i in range(len(self.room_map)):
            for col_i in range(len(self.room_map[row_i])):
                if self.room_map[row_i][col_i] == '^':
                    self.guard_pos = (row_i, col_i)
                    return

    def __move_guard(self):
        x = self.guard_pos[0]
        y = self.guard_pos[1]
        blockage = '#'

        if self.orthogonality == orth.Orthogonality.UP:
            if x != 0:
                if self.room_map[x - 1][y] == blockage:
                    self.orthogonality = orth.Orthogonality.RIGHT
                    self.__move_guard()
                else:
                    self.guard_pos = (x - 1, y)
            else:
                self.guard_pos = (-1, -1)
        elif self.orthogonality == orth.Orthogonality.RIGHT:
            if y < len(self.room_map[0]) - 1:
                if self.room_map[x][y + 1] == blockage:
                    self.orthogonality = orth.Orthogonality.DOWN
                    self.__move_guard()
                else:
                    self.guard_pos = (x, y + 1)
            else:
                self.guard_pos = (-1, -1)
        elif self.orthogonality == orth.Orthogonality.DOWN:
            if x < len(self.room_map) - 1:
                if self.room_map[x + 1][y] == blockage:
                    self.orthogonality = orth.Orthogonality.LEFT
                    self.__move_guard()
                else:
                    self.guard_pos = (x + 1, y)
            else:
                self.guard_pos = (-1, -1)
        elif self.orthogonality == orth.Orthogonality.LEFT:
            if y != 0:
                if self.room_map[x][y - 1] == blockage:
                    self.orthogonality = orth.Orthogonality.UP
                    self.__move_guard()
                else:
                    self.guard_pos = (x, y - 1)
            else:
                self.guard_pos = (-1, -1)

    def puzzle_1(self):
        self.__init_guard_pos()

        guard_inbounds = True

        while guard_inbounds:
            self.__move_guard()

            if self.guard_pos == (-1, -1):
                guard_inbounds = False
                continue
            if self.guard_pos not in self.visited_spots:
                self.visited_spots.append(self.guard_pos)

        return len(self.visited_spots)

    def puzzle_2(self):
        self.__init_guard_pos()

        init_guard_pos = self.guard_pos
        loop_count = 0
        positions_that_lead_to_loops = []
        #positions_that_do_not_loop = []

        # From Day 1
        guard_inbounds = True

        while guard_inbounds:
            self.__move_guard()

            if self.guard_pos == (-1, -1):
                guard_inbounds = False
                continue
            if self.guard_pos not in self.visited_spots:
                self.visited_spots.append(self.guard_pos)
        main_path_unobstructed = []
        for pos in self.visited_spots:
            main_path_unobstructed.append(pos)

        for x in range(len(self.room_map)):
            for y in range(len(self.room_map[0])):
                print(x,y,loop_count,len(positions_that_lead_to_loops))

                if (x,y) not in main_path_unobstructed:
                    continue

                if cf.tuples_equal(init_guard_pos, (x, y)):
                    continue
                if self.room_map[x][y] == '#':
                    continue

                save_room_map = copy.deepcopy(self.room_map)
                self.room_map[x][y] = '#'

                self.visited_spots = [(init_guard_pos, orth.Orthogonality.UP)]
                guard_inbounds = True
                self.guard_pos = init_guard_pos
                self.orthogonality = orth.Orthogonality.UP

                while guard_inbounds:

                    self.__move_guard()

                    if self.guard_pos == (-1, -1):
                        guard_inbounds = False
                        continue

                    if self.guard_pos in positions_that_lead_to_loops:
                        for visited in self.visited_spots:
                            if visited not in positions_that_lead_to_loops:
                                positions_that_lead_to_loops.append(visited)
                        loop_count += 1
                        break

                    new_location_in_visited = False
                    for visited in self.visited_spots:
                        if self.guard_pos == visited[0] and self.orthogonality == visited[1]:
                            new_location_in_visited = True
                            break
                    if not new_location_in_visited:
                        self.visited_spots.append((self.guard_pos, self.orthogonality))
                    else:
                        for loc in self.visited_spots:
                            if loc not in positions_that_lead_to_loops:
                                positions_that_lead_to_loops.append(loc)

                        loop_count += 1
                        break

                self.room_map = save_room_map

        return loop_count

