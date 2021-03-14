"""
Author: David Melendez

This is a Sudoku Game and Solver

Uses backtracking to solve the sudoku

Created 3/11/2021
Commands:
 -

Enjoy it!

"""


import pygame
from copy import deepcopy
from time import time
import sudoku_class



board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 3, 0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]]


sudo = sudoku_class.Sudoku()
sudo.set_sudoku_matrix(board)
validity = sudo.check_validity()

print(sudo)
print("validity: {}".format(validity))

print(sudo.solve())
