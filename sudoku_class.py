import pygame
from copy import deepcopy


class Sudoku:
    """
    Contains a 2D - array where the numbers are placed and some methods to check
    the validity of the current state of the sudoku.
    """

    def __init__(self):
        """
        Initializes a 9x9 sudoku matrix with all values set to 0
        If the number in any location is not between 1 and 9 inclusive, then
        no value is actually there (perhaps is a placeholder).
        """

        # Create sudo_matrix
        self.sudoku_matrix = [[0 for j in range(9)] for i in range(9)]
        self.num_cols = 9
        self.num_rows = 9
        self.solved_sudoku_matrix = [[0 for j in range(9)] for i in range(9)]

    def __repr__(self):
        """
        Prints the sudoku_matrix

        Returns:
            An empty string
        """
        for row in self.sudoku_matrix:
            print(row)

        return ""

    def set_sudoku_matrix(self, new_sudoku_matrix: list):
        """
        Sets new_sudoku_matrix as the new sudoku matrix
        Ensures the dimensions of both matrices are the same

        Args:
            new_sudoku_matrix (list): the new 2d array representing the sudoku
        """
        # Check row size
        assert self.num_rows == len(new_sudoku_matrix),\
            "set_sudoku_matrix Error: Matrices row sizes are not the same!"

        # Check col size
        for row_index in range(len(self.sudoku_matrix)):
            if self.num_cols != len(new_sudoku_matrix[row_index]):
                raise ValueError("set_sudoku_matrix Error: Matrices row sizes\
                     are not the same!")

        # Set the new matrix as a copy
        self.sudoku_matrix = deepcopy(new_sudoku_matrix)

    def check_row_validity(self) -> bool:
        """
        Checks that each row has only one instance of the numbers from 1 to 9
        """
        for row_index in range(self.num_rows):
            last_seen = set()

            for col_index in range(self.num_cols):
                item = self.sudoku_matrix[row_index][col_index]

                # Only work take into account the numbers from 1 to 9
                if (item in [1, 2, 3, 4, 5, 6, 7, 8, 9]):

                    if (item in last_seen):
                        # print("###############################")
                        # print(f"A row contains at least two: {item}'s")
                        # print("###############################")
                        return False

                    else:
                        last_seen.add(item)

        return True

    def check_col_validity(self):
        """Check that each col has only one instance of the numbers from 1 to 9."""
        for col_index in range(self.num_cols):
            last_seen = set()

            for row_index in range(self.num_rows):
                item = self.sudoku_matrix[row_index][col_index]

                # Only work take into account the numbers from 1 to 9
                if (item in [1, 2, 3, 4, 5, 6, 7, 8, 9]):

                    if (item in last_seen):
                        # print("###############################")
                        # print(f"A col contains at least two: {item}'s")
                        # print("###############################")
                        return False

                    else:
                        last_seen.add(item)

        return True

    def check_square_validity(self) -> bool:
        """
        The sudoku matrix is made of 9 3x3 squares.
        This method ensures each of these squares must have at most all the
        numbers from 1 to 9.
        """
        valid = True
        for row in range(3):
            row *= 3
            for col in range(3):
                col *= 3
                valid = valid and self.check_square_validity_helper(row, col)

        return valid

    def check_square_validity_helper(self, row_start: int, col_start: int) -> bool:
        """Check_square_validity_helper."""

        last_seen = set()

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                number = self.sudoku_matrix[row][col]

                if (number in [1, 2, 3, 4, 5, 6, 7, 8, 9]):

                    if (not number in last_seen):
                        last_seen.add(number)
                    else:
                        # print(f"A 3x3 square contains at least two: {number}'s")
                        return False

        return True

    def check_validity(self):
        """Check current sudo board validty."""

        # If one the the validation flags are false, then the whole result is
        # also false

        validity = True
        validity = validity and self.check_row_validity()
        validity = validity and self.check_col_validity()
        validity = validity and self.check_square_validity()

        return validity

    def solve(self):
        """
        Solves the current sudoku.

        Uses backtracking to find all the possible combinations of sudoku matrix
        starting from the current one. There might be more than 1 solution to a
        soduku matrix, the algorithm gives one of them
        """

        if (not self.check_validity()):
            print("Solve error: Matrix can't be solved!")
            return False


        # Solves the matrix in self.sudoku_matrix
        solved = self.solve_helper()

        if (not self.check_validity()):
            print(
                "There is no possible solution to the given soduku :(")
            return False

        return solved

    def solve_helper(self, row=0, col=0) -> bool:
        """
        Contains the actual backtracking algorithm to solve the sudoku
        """
        # Ensure the row and col give a proper location in the grid
        if (col >= self.num_cols):
            row += 1
            col = 0
        # print(f"row:{row}, col:{col}, ")
        # current_item = self.sudoku_matrix[row][col]
        # Current board is no longer valid
        if (not self.check_validity()):
            return False

        # if the current location location in the grid is the next after the
        # last one, then the sudoku has been successfully solved.
        # The 'next position after the last position' is the next row + 1,
        # which is the number of total rows of the matrix and the first col
        if (row == self.num_rows and col == 0):
            print("A solution has been found!")
            self.__repr__()
            return True

        # Check if the number in the current row and col is not placed
        # so that the algorithm can start placing numbers to find a solution
        elif (self.sudoku_matrix[row][col] in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
            return self.solve_helper(row, col + 1)

        # The current row and col has no number, therefore we can put numbers
        # and try if it is valid
        else:
            for item in range(1, 10):
                # Choose
                chosen = item
                self.sudoku_matrix[row][col] = chosen

                # Explore
                if (self.solve_helper(row, col + 1)):
                    return True

                # Backtrack
                self.sudoku_matrix[row][col] = 0

        return False
