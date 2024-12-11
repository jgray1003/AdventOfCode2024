import importlib

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
        8: (1, 1)
    }

    for day_num, puzzle_tup in puzzles_to_run.items():
        if puzzle_tup[0] == 0 and puzzle_tup[1] == 0:
            continue
        day_module = importlib.import_module(f'Day.day_{day_num}')
        day_puzzle = day_module.day_puzzles()

        if puzzle_tup[0] == 1:
            print(f'Day {day_num} Puzzle 1 Output: {day_puzzle.puzzle_1()}')
        if puzzle_tup[1] == 1:
            print(f'Day {day_num} Puzzle 2 Output: {day_puzzle.puzzle_2()}')





