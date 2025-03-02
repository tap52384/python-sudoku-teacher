from constants import MIN_NUMBER, MAX_NUMBER, VALID_INPUT_VALUES

class Grid:
    """
    Represents the playing grid of a sudoku board.
    """
    def __init__(self, grid_string=None):
        """
        Initializes a new grid with the given string.
        """
        self._cells = [None] * (MAX_NUMBER * MAX_NUMBER)

        # If a grid string is provided, we need to validate it and raise an
        # exception if it is invalid
        if grid_string:
            self._validate_grid_string(grid_string)
            self._initialize_grid(grid_string)

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

        # Remove all whitespace from the ends of the string
        grid_string = grid_string.strip()

        # Check if the grid string is the correct length
        if len(grid_string) != (MAX_NUMBER * MAX_NUMBER):
            raise ValueError("Invalid grid string length")

        # Check if the grid string contains only valid characters
        if not all(char in VALID_INPUT_VALUES for char in grid_string):
            raise ValueError("Invalid characters in grid string")

        self._grid_string = grid_string
