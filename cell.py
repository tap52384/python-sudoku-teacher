from constants import MIN_NUMBER, MAX_NUMBER
from termcolor import colored

class Cell:
    """
    Represents a cell in a sudoku board.
    """
    def __init__(self, row=0, column=0, original_value=0):
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        self._row = row

        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        self._column = column

        if original_value < 0 or original_value > MAX_NUMBER:
            raise ValueError(f"Original value must be between {MIN_NUMBER} and {MAX_NUMBER}")

        # Using the row and column, set the house number
        # The double slash is the floor division operator; it performs division and rounds down to
        # the nearest whole number
        # https://docs.python.org/3/library/operator.html
        self._house = Cell.getHouseNumber(row, column)

        # Create a set to store the possible values for the cell
        self.possible_values = set(range(MIN_NUMBER, MAX_NUMBER + 1))

        # Create a variable to store house notes for the cell as a set
        self.house_notes = set()

        # Create a variable to store cell notes for the cell as a set
        self.cell_notes = set()

        # Create a variable to store the value of the cell
        # If the value is 0, the cell is empty
        self._value = original_value

        # Determine the index of the cell in the board
        self._index = Cell.get_index(row, column)

        # Create a variable to store the original value of the cell
        # This is used to check if the cell is part of the original puzzle
        self._original_value = original_value

        # For the current cell, get the indexes of the cells in the same row, column, and house
        # These indexes will never change, so getting them on object creation may be more efficient.
        self.row_indexes = set(Cell.get_indexesOfRow(row))
        self.row_indexes.discard(self.index)

        self.column_indexes = set(Cell.get_indexesOfColumn(column))
        self.column_indexes.discard(self.index)

        self.house_indexes = set(Cell.get_indexesOfHouse(self.house))
        self.house_indexes.discard(self.index)

    def __str__(self):
        # If the cell is empty, return an underscore
        # If the cell is part of the original puzzle, return the value in blue
        # If the cell is not part of the original puzzle, return the value in green

        if self.value == 0:
            return "_"

        if self.original_value > 0:
            return colored(self.value, "blue")

        return colored(self.value, "green")

    def __repr__(self):
        return f"Cell({self._row}, {self._column})"

    def __eq__(self, other):
        return isinstance(other, Cell) and \
            self.row == other.row and \
            self.column == other.column

    @staticmethod
    def get_index(row, column):
        """
        Get the 0-based index of a cell in the board (0-80). The board (or grid) will store
        all Cell objects as a simple 80-element list.
        """
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        return ((row - 1) * MAX_NUMBER + column) - 1

    @staticmethod
    def getHouseNumber(row, column):
        """
        Get the house number of a cell
        """
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")
        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        return (row - 1) // 3 * 3 + (column - 1) // 3 + 1

    @staticmethod
    def get_indexesOfHouse(house):
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
                indexes.append(Cell.get_index(row + i, column + j))

        return indexes

    @staticmethod
    def get_indexesOfRow(row):
        """
        Get the indexes of the cells in a row
        """
        if row < MIN_NUMBER or row > MAX_NUMBER:
            raise ValueError(f"Row number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        # Create a list to store the indexes of the cells in the row
        indexes = []
        for i in range(MAX_NUMBER):
            indexes.append(Cell.get_index(row, i + 1))

        return indexes

    @staticmethod
    def get_indexesOfColumn(column):
        """
        Get the indexes of the cells in a column
        """
        if column < MIN_NUMBER or column > MAX_NUMBER:
            raise ValueError(f"Column number must be between {MIN_NUMBER} and {MAX_NUMBER}")

        # Create a list to store the indexes of the cells in the column
        indexes = []
        for i in range(MAX_NUMBER):
            indexes.append(Cell.get_index(i + 1, column))

        return indexes

    @staticmethod
    def getAllSeenIndexes(row, column):
        """
        Get the indexes of all the cells that can be seen by a given cell
        """
        indexes = set(Cell.get_indexesOfRow(row))
        indexes.update(Cell.get_indexesOfColumn(column))
        indexes.update(Cell.get_indexesOfHouse(Cell.getHouseNumber(row, column)))

        # Remove the index of the given cell
        indexes.discard(Cell.get_index(row, column))

        return list(indexes)

    @property
    def rowIndexes(self):
        """
        Indexes of the cells in the same row as the current cell
        """
        return self.row_indexes

    @property
    def columnIndexes(self):
        """
        Indexes of the cells in the same column as the current cell
        """
        return self.column_indexes

    @property
    def houseIndexes(self):
        """
        Indexes of the cells in the same house as the current cell
        """
        return self.house_indexes

    @property
    def seenIndexes(self):
        """
        Indexes of the cells that can be seen by the current cell
        """
        # https://docs.python.org/3/library/stdtypes.html#frozenset.union
        indexes = self.row_indexes.union(self.column_indexes)
        indexes = indexes.union(self.house_indexes)
        indexes.discard(self.index)

        return indexes

    @property
    def row(self):
        """
        Returns the 1-based row number of the cell
        """
        return self._row

    @property
    def column(self):
        """
        Returns the 1-based column number of the cell
        """
        return self._column

    @property
    def house(self):
        """
        Returns the house number of the cell.
        """
        return self._house

    @property
    def value(self):
        """
        Returns the value of the cell.
        """
        return self._value

    @property
    def index(self):
        """
        Returns the 0-based index of the cell
        """
        return self._index

    @property
    def friendly_index(self):
        """
        Returns the 1-based index of the cell
        """
        return self._index + 1

    @property
    def original_value(self):
        """
        Returns the original value of the cell, if applicable.
        """
        return self._original_value

    def has_same_house(self, other):
        """
        Returns True if this cell is in the same house as the other cell.
        """
        return isinstance(other,Cell) and \
            self.house == other.house

    def hasSameRow(self, other):
        """
        Returns True if this cell is in the same row as the other cell.
        """
        return isinstance(other,Cell) and \
            self.row == other.row

    def hasSameColumn(self, other):
        return isinstance(other,Cell) and \
            self.column == other.column

    def canSee(self, other):
        return isinstance(other,Cell) and \
            self.hasSameRow(other) or \
            self.hasSameColumn(other) or \
            self.has_same_house(other)

    def updatePossibleValuesSeen(self, grid):
        for index in self.seenIndexes:
            cell = grid.cells[index]
            if cell.value in self.possible_values:
                self.possible_values.remove(cell.value)

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
