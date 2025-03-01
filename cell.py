from constants import MIN_NUMBER, MAX_NUMBER

class Cell:
    """
    Represents a cell in a sudoku board.
    """
    def __init__(self, row=0, column=0, original_value=0):
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        self.row = row

        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        self.column = column

        # Using the row and column, set the house number
        # The double slash is the floor division operator; it performs division and rounds down to
        # the nearest whole number
        # https://docs.python.org/3/library/operator.html
        self.house = (row - 1) // 3 * 3 + (column - 1) // 3 + 1

        # Create a set to store the possible values for the cell
        self.possible_values = set(range(MIN_NUMBER, MAX_NUMBER + 1))

        # Create a variable to store the value of the cell
        # If the value is 0, the cell is empty
        if original_value < 0 or original_value > MAX_NUMBER:
            raise ValueError(f"Original value must be between {MIN_NUMBER} and {MAX_NUMBER}")
        self.value = original_value

        # Determine the index of the cell in the board
        self.index = Cell.getIndex(row, column)

        # Create a variable to store the original value of the cell
        # This is used to check if the cell is part of the original puzzle
        self.original_value = original_value

    def __str__(self):
        return f"Cell {self.row}, {self.column}"

    def __repr__(self):
        return f"Cell({self.row}, {self.column})"

    def __eq__(self, other):
        return isinstance(other, Cell) and \
            self.row == other.row and \
            self.column == other.column

    @staticmethod
    def getIndex(row, column):
        """
        Get the 1-based index of a cell in the board (1-81)
        """
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        return (row - 1) * MAX_NUMBER + column

    @staticmethod
    def getIndexesOfHouse(house):
        """
        Get the indexes of the cells in a house
        """
        if house < MIN_NUMBER or house > MAX_NUMBER:
            raise ValueError(f"House number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        # Determine the starting row and column of the house
        row = (house - 1) // 3 * 3 + 1
        column = (house - 1) % 3 * 3 + 1

        # Create a list to store the indexes of the cells in the house
        indexes = []
        for i in range(3):
            for j in range(3):
                indexes.append(Cell.getIndex(row + i, column + j))

        return indexes

    @staticmethod
    def getIndexesOfRow(row):
        """
        Get the indexes of the cells in a row
        """
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        # Create a list to store the indexes of the cells in the row
        indexes = []
        for i in range(MAX_NUMBER):
            indexes.append(Cell.getIndex(row, i + 1))

        return indexes

    @staticmethod
    def getIndexesOfColumn(column):
        """
        Get the indexes of the cells in a column
        """
        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        # Create a list to store the indexes of the cells in the column
        indexes = []
        for i in range(MAX_NUMBER):
            indexes.append(Cell.getIndex(i + 1, column))

        return indexes

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    @property
    def house(self):
        return self._house

    @property
    def value(self):
        return self._value

    @property
    def index(self):
        return self._index

    def hasSameHouse(self, other):
        return isinstance(other,Cell) and \
            self.house == other.house

    def hasSameRow(self, other):
        return isinstance(other,Cell) and \
            self.row == other.row

    def hasSameColumn(self, other):
        return isinstance(other,Cell) and \
            self.column == other.column

    def canSee(self, other):
        return isinstance(other,Cell) and \
            self.hasSameRow(other) or \
            self.hasSameColumn(other) or \
            self.hasSameHouse(other)

    def remove_possible_value(self, value):
        self.possible_values.discard(value)

    @value.setter
    def value(self, value):
        # Do not allow setting the value of a cell that is part of the original puzzle
        if self.original_value >= MIN_NUMBER and self.original_value <= MAX_NUMBER:
            # raise ValueError("Cannot set the value of a cell that is part of the original puzzle")
            return

        # If the value is 0, then make the cell empty
        if value == 0:
            self._value = value
            # Reset the possible values to the full set
            self.possible_values = set(range(MIN_NUMBER, MAX_NUMBER + 1))
            return

        if value < MIN_NUMBER or value > MAX_NUMBER:
            raise ValueError(f"Value must be between {MIN_NUMBER} and {MAX_NUMBER}")

        self.value = value
        self.possible_values = set()
