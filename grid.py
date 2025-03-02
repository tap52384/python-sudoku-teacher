from constants import MAX_NUMBER, EMPTY_CELLS, VALID_INPUT_VALUES
from cell import Cell

class Grid:
    """
    Represents the playing grid of a sudoku board.
    """
    def __init__(self, grid_string=None):
        """
        Initializes a new grid with the given string.
        """
        # This is a list of cells that will be used to store the Cell objects
        self._cells = [None] * (MAX_NUMBER * MAX_NUMBER)

        # This will store a string representation of the grid and any original values
        self._grid_string = None

        # This will store the indexes of cells that have been solved
        # Maybe we can use a set instead of a list to make lookups faster
        # Cell indexes are 0-based, so this set will store integers from 0 to 80
        self._solved_cell_indexes = set()

        # This will store the indexes of cells that have not been solved
        self._unsolved_cell_indexes = set(range(MAX_NUMBER * MAX_NUMBER))

        # If a grid string is provided, we need to validate it and raise an
        # exception if it is invalid
        self._validate_grid_string(grid_string)

        if self._grid_string:
            self._initialize_grid(self._grid_string)

    def __str__(self):
        output = ""
        for i in range(MAX_NUMBER):
            for j in range(MAX_NUMBER):
                output += f"{self.getCell(i + 1, j + 1)} "
            output += "\n"
        return output

    def _validate_grid_string(self, grid_string):
        """
        Validates the given grid string.
        """

        if grid_string is None:
            raise ValueError("Grid string cannot be None")

        # Remove all whitespace from the ends of the string
        grid_string = f"{grid_string}".strip()

        # Check if the grid string is the correct length
        if len(grid_string) != (MAX_NUMBER * MAX_NUMBER):
            raise ValueError("Invalid grid string length")

        # Check if the grid string contains only valid characters
        if not all(char in VALID_INPUT_VALUES for char in grid_string):
            raise ValueError("Invalid characters in grid string")

        # Replace all empty cell characters with 0 for consistency, making all
        # cell values integers
        for empty_char in EMPTY_CELLS:
            grid_string = grid_string.replace(empty_char, '0')

        self._grid_string = grid_string

    def _initialize_grid(self, grid_string):
        """
        Initializes the grid with the given string.
        """

        # The range function will generate a sequence of numbers from 0 to 9 (MAX_NUMBER)
        for row in range(MAX_NUMBER):
            for column in range(MAX_NUMBER):
                # Get the value of the cell using the grid string
                cell_value = int(grid_string[(row * MAX_NUMBER) + column])

                # Create a new cell object
                cell = Cell(row + 1, column + 1, original_value=cell_value)

                # Store the cell in the grid
                self._cells[cell.index] = cell

                # If the cell is not empty, add it to the solved cell indexes
                if cell.value != 0:
                    self._solved_cell_indexes.add(cell.index)

        # Remove the solved cell indexes from the unsolved cell indexes
        self._unsolved_cell_indexes.difference_update(self._solved_cell_indexes)
