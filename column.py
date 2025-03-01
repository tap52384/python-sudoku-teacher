from constants import MIN_NUMBER, MAX_NUMBER

class Column:
    """
    Represents a column in a sudoku board.
    """
    def __init__(self, number=0):
        if number < MIN_NUMBER or number > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        self.number = number

    def __str__(self):
        return f"Column {self.number}"

    def __repr__(self):
        return f"Column({self.number})"

    def __eq__(self, other):
        return isinstance(other, Column) and \
            self.number == other.number

    @property
    def number(self):
        return self._number
