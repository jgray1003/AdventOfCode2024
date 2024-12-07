import importlib

if __name__ == "__main__":
    # day to bool tuple, 0-index first puzzle and respective second
    puzzles_to_run = {
        1: (1, 1),
        3: (1, 0)
    }

    for day_num, puzzle_tup in puzzles_to_run.items():
        if puzzle_tup[0] == 0 and puzzle_tup[1] == 0:
            continue
        day_module = importlib.import_module(f'Day.day_{day_num}')
        day_puzzle = day_module.day_puzzles()

        if puzzle_tup[0] == 1:
            result = day_puzzle.puzzle_1()
            print(f'Output: {result}')
        if puzzle_tup[1] == 1:
            result = day_puzzle.puzzle_2()
            print(f'Output: {result}')





