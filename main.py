from Day import day_1
from Day import day_2


def run_puzzles(puzzles):
    for puzzle_function in puzzles:
        result = puzzle_function()
        print(f'Output: {result}')

if __name__ == "__main__":
    #day_1_puzzles = day_1.day_1_puzzles()
    day_2_puzzles = day_2.day_2_puzzles()
    puzzles_to_run = [day_2_puzzles.puzzle_1, day_2_puzzles.puzzle_2]
    run_puzzles(puzzles_to_run)




