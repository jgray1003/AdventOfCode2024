import importlib
import time

def run_puzzle(day, puzzle_num, puzzle_funct):

    p_start = time.time()
    output = puzzle_funct()
    p_end = time.time()

    elapsed = p_end - p_start
    seconds = int(elapsed)
    milliseconds = int((elapsed - seconds) * 1000)

    print(f'Day {day} Puzzle {puzzle_num} Output: {output} in {seconds} s {milliseconds} ms')


if __name__ == "__main__":
    # day to bool tuple, 0-index first puzzle and respective second

    puzzles_to_run = {
        1: (0, 0),
        2: (0, 0),
        3: (0, 0),
        4: (0, 0),
        5: (0, 0),
        6: (0, 0),
        7: (0, 0),
        8: (0, 0),
        9: (1, 1)
    }

    for day_num, puzzle_tup in puzzles_to_run.items():
        if puzzle_tup[0] == 0 and puzzle_tup[1] == 0:
            continue

        day_module = importlib.import_module(f'Day.day_{day_num}')
        day_puzzle = day_module.day_puzzles()

        t_day_start = time.time()

        if puzzle_tup[0] == 1:
            run_puzzle(day_num, 1, day_puzzle.puzzle_1)
        if puzzle_tup[1] == 1:
            run_puzzle(day_num, 2, day_puzzle.puzzle_2)

        t_day_end = time.time()
        day_elapsed_time = t_day_end - t_day_start
        day_seconds = int(day_elapsed_time)
        day_milliseconds = int((day_elapsed_time - day_seconds) * 1000)

        if puzzle_tup[0] == 1 and puzzle_tup[1] == 1:
            print(f'Day {day_num} Total Elapsed: {day_seconds} s {day_milliseconds} ms')





