from Common import common_functions as cf
from Common import orthogonality as orth
import copy

class day_puzzles:
    def __init__(self):
        self.input_file_name = 'day_6.txt'
        self.room_map = cf.read_file_to_2D_array(self.input_file_name, example_file=False)
        self.original_room_map = copy.deepcopy(self.room_map)
        self.guard_pos = self.__init_guard_pos()
        self.visited_spots = [self.guard_pos]
        self.orthogonality = orth.Orthogonality.UP
        self.running_visited_pos = []

    def __init_guard_pos(self):
        for row_i in range(len(self.room_map)):
            for col_i in range(len(self.room_map[row_i])):
                if self.room_map[row_i][col_i] == '^':
                    return row_i, col_i
        return 0, 0

    def __reinit_guard(self):
        self.guard_pos = self.__init_guard_pos()
        self.orthogonality = orth.Orthogonality.UP

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

    def __iterate_candidate_obstacle_guard(self):
        visited_pos = copy.deepcopy(self.running_visited_pos)

        guard_inbounds = True

        while guard_inbounds:
            self.__move_guard()

            if self.guard_pos == (-1, -1):
                return False
            if (self.guard_pos, self.orthogonality) not in visited_pos:
                visited_pos.append((self.guard_pos, self.orthogonality))
            else:
                for pos, direction in visited_pos:
                    if (pos, direction) not in self.running_visited_pos:
                        self.running_visited_pos.append((pos, direction))
                return True
        return False

    def __place_obstacle(self, loc_data:tuple[tuple,orth.Orthogonality]):
        direction = loc_data[1]
        pos = loc_data[0]

        next_pos = (-1, -1)

        # No need to check if next_pos is obstacle as it is in a pre-run navigable path.
        if direction == orth.Orthogonality.UP and pos[0] > 0:
            next_pos = (pos[0] - 1, pos[1])
            self.room_map[next_pos[0]][next_pos[1]] = '#'
        elif direction == orth.Orthogonality.RIGHT and pos[1] < len(self.room_map[0]) - 1:
            next_pos = (pos[0], pos[1] + 1)
            self.room_map[next_pos[0]][next_pos[1]] = '#'
        elif direction == orth.Orthogonality.DOWN and pos[0] < len(self.room_map) - 1:
            next_pos = (pos[0] + 1, pos[1])
            self.room_map[next_pos[0]][next_pos[1]] = '#'
        elif direction == orth.Orthogonality.LEFT and pos[1] > 0:
            next_pos = (pos[0], pos[1] - 1)
            self.room_map[next_pos[0]][next_pos[1]] = '#'

        return next_pos

    def __detect_loop(self, visited:tuple[tuple,orth.Orthogonality]):
        for i in range(len(visited)):
            j = i + 1
            while j < len(visited):
                if cf.tuples_equal(visited[i], visited[j]):
                    return True
                j += 1

        return False


    def puzzle_1(self):
        guard_inbounds = True

        while guard_inbounds:
            self.__move_guard()

            if self.guard_pos == (-1, -1):
                guard_inbounds = False
                continue
            if self.guard_pos not in self.visited_spots:
                self.visited_spots.append(self.guard_pos)

        return len(self.visited_spots)

    # def puzzle_2(self):
    #     # reset globals changed in puzzle_1
    #     self.__reinit_guard()
    #     self.visited_spots = [(self.guard_pos, self.orthogonality)]
    #     loop_count = 0
    #     # get original guard path
    #     guard_inbounds = True
    #     while guard_inbounds:
    #         self.__move_guard()
    #
    #         if self.guard_pos == (-1, -1):
    #             guard_inbounds = False
    #             continue
    #         if self.guard_pos not in self.visited_spots:
    #             self.visited_spots.append((self.guard_pos, self.orthogonality))
    #
    #     new_obstacle_locations = []
    #     # place obstacles along original path and trace outcomes
    #     for spot in self.visited_spots:
    #         if spot[0] == (6,4):
    #             a =55
    #         self.room_map = copy.deepcopy(self.original_room_map)
    #         self.__reinit_guard()
    #         obstacle_placed_at = self.__place_obstacle(spot)
    #         iteration_visited_spots = []
    #
    #         # Off map
    #         if obstacle_placed_at == (-1, -1):
    #             break
    #
    #         guard_inbounds = True
    #         while guard_inbounds:
    #             self.__move_guard()
    #
    #             if self.guard_pos == (-1, -1):
    #                 guard_inbounds = False
    #                 continue
    #             if (self.guard_pos, self.orthogonality) not in iteration_visited_spots:
    #                 iteration_visited_spots.append((self.guard_pos, self.orthogonality))
    #             else:
    #                 if obstacle_placed_at not in new_obstacle_locations:
    #                     new_obstacle_locations.append(obstacle_placed_at)
    #                     loop_count += 1
    #                     print(loop_count)
    #                 break
    #             # if self.__detect_loop(iteration_visited_spots):
    #             #     if obstacle_placed_at not in new_obstacle_locations:
    #             #         new_obstacle_locations.append(obstacle_placed_at)
    #             #         loop_count += 1
    #             #     break
    #
    #     #print( new_obstacle_locations)
    #     return loop_count
    #
    #
    # def puzzle_2_old(self):
    #     self.guard_pos = self.__init_guard_pos()
    #     self.orthogonality = orth.Orthogonality.UP
    #     self.visited_spots = [(self.guard_pos, self.orthogonality)]
    #     loop_count = 0
    #     guard_inbounds = True
    #
    #     while guard_inbounds:
    #         self.__move_guard()
    #
    #         if self.guard_pos == (-1, -1):
    #             guard_inbounds = False
    #             continue
    #         if (self.guard_pos, self.orthogonality) not in self.visited_spots:
    #             self.visited_spots.append((self.guard_pos, self.orthogonality))
    #
    #     loop_obstacle_locs = []
    #
    #     for pos, direction in self.visited_spots:
    #         orig_map = copy.deepcopy(self.room_map)
    #         next_pos = (0, 0)
    #
    #         if direction == orth.Orthogonality.UP and pos[0] > 0:
    #             next_pos = (pos[0] - 1, pos[1])
    #             if self.room_map[next_pos[0]][next_pos[1]] == '#':
    #                 continue
    #             self.room_map[next_pos[0]][next_pos[1]] = '#'
    #         elif direction == orth.Orthogonality.RIGHT and pos[1] < len(self.room_map[0]) - 1:
    #             next_pos = (pos[0], pos[1] + 1)
    #             if self.room_map[next_pos[0]][next_pos[1]] == '#':
    #                 continue
    #             self.room_map[next_pos[0]][next_pos[1]] = '#'
    #         elif direction == orth.Orthogonality.DOWN and pos[0] < len(self.room_map) - 1:
    #             next_pos = (pos[0] + 1, pos[1])
    #             if self.room_map[next_pos[0]][next_pos[1]] == '#':
    #                 continue
    #             self.room_map[next_pos[0]][next_pos[1]] = '#'
    #         elif direction == orth.Orthogonality.LEFT and pos[1] > 0:
    #             next_pos = (pos[0], pos[1] - 1)
    #             if self.room_map[next_pos[0]][next_pos[1]] == '#':
    #                 continue
    #             self.room_map[next_pos[0]][next_pos[1]] = '#'
    #
    #         self.guard_pos = pos
    #         self.orthogonality = direction
    #         loop_detected = self.__iterate_candidate_obstacle_guard()
    #         self.room_map = orig_map
    #         if loop_detected and next_pos not in loop_obstacle_locs:
    #             loop_obstacle_locs.append(next_pos)
    #             loop_count += 1
    #             self.room_map = orig_map
    #     return loop_count

    def puzzle_2(self):
        self.__init_guard_pos()

        init_guard_pos = self.guard_pos
        loop_count = 0
        positions_that_lead_to_loops = []

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


