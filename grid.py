from constants import MIN_NUMBER, MAX_NUMBER

class Grid:
    """
    Represents the playing grid of a sudoku board.
    """
    def __init__(self):
        self._cells = [None] * (MAX_NUMBER * MAX_NUMBER)

    def __str__(self):
        output = ""
        for i in range(MAX_NUMBER):
            for j in range(MAX_NUMBER):
                output += f"{self.getCell(i + 1, j + 1)} "
            output += "\n"
        return output
