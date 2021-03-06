def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with 0
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == 0:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (0)


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row  行检查
    row_val = puzzle[row]
    if guess in row_val:
        return False  # we've repeated, then our guess is not valid!

    # now the column
    # col_val = []
    # for i in range(9):
    #     col_val.append(puzzle[i][col])
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False

    # and then the square
    row_start = (row // 3) * 3  # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0  区分左上，上，右上三个方块
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):  # 检查小方块内所有值
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether exits
    # mutates puzzle to be the solution (if solution exists)

    # Step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True

    # Step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        # Step 3: check if this is a valid guess, then place it at that spot on the puzzle
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # Step 4: then we recursively call our solver function!
            if solve_sudoku(puzzle):
                return True

        # step 5: it not valid or if nothing gets returned true, than we need to backtrack and try a new number
        puzzle[row][col] = 0  # reset the guess

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False


if __name__ == '__main__':
    example_board = [
        [8, 0, 5,  0, 0, 9,  3, 0, 0],
        [2, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  6, 0, 0,  0, 0, 9],

        [0, 4, 0,  0, 0, 0,  0, 0, 0],
        [9, 0, 3,  0, 0, 6,  8, 0, 0],
        [0, 0, 0,  0, 1, 0,  0, 7, 0],

        [0, 2, 0,  0, 0, 5,  0, 0, 0],
        [5, 0, 4,  7, 0, 0,  0, 8, 0],
        [0, 6, 0,  0, 0, 0,  4, 0, 0]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
