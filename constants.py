# constants.py

# Constants used for row numbers, column numbers, and valid cell values
MIN_NUMBER = 1
MAX_NUMBER = 9

# Used to determine whether a cell is empty instead of using None
EMPTY = 0

# Used to determine the max 1-based index of a cell
MAX_CELL_INDEX = (MAX_NUMBER * MAX_NUMBER) - 1

# Valid non-empty cell values
VALID_VALUES = set(range(EMPTY, MAX_NUMBER + 1))

# When reading a file or an input string representing a sudoku grid, we need to
# accept 0, '.', '_', and ' ' as empty cells
EMPTY_CELLS = {'0', '.', '_', ' '}

# Valid input values for importing a sudoku grid
VALID_INPUT_VALUES = VALID_VALUES.union(EMPTY_CELLS)
