#  Sudoku-Solver
#### Video Demo:  https://www.youtube.com/watch?v=CG7Gm8i1McE
#### Description:
#### Context:
#### The sudoku has been
#### RULES: A sudoku is a 9x9 grid divided between 9 3x3 boxes leaving 81 squares to place a number if there is no number placed. A square con only have 1 number, there can only be an certain number in a 3x3 square. Each column and row  can only have a number from 1 to 9 once.
#### Implementation:
#### There are 3 files. main.py, sudoku_class.py, and finally graphics.py
#### sudoku_class.py contains the big chunk of code. First it starts off with a class named sudoku which contains a 2D - array where the numbers are placed and have some methods to check the validity of the current state of the sudoku. Particularly, the class has 3 methods to check the validity of a board. These methods are check_row_validity which checks that each row has only one instance of the numbers from 1 to 9. check_col_validity which checks that each col has only one instance of the numbers from 1 to 9. Finally check_square validity which ensures each of these squares must have at most all the numbers from 1 to 9.
#### Supposing that we have a valid board, then we have the backtracking method named solve with its helper. It uses backtracking to place every possible number on every blank space left, always ensuring the board remains valid. If for some reason the board becomes invalid, then the algorithm stops trying that branch. If the algorithms exhausts all possible combinations and no one works, then the board is unsolvable.
#### Main.py contains the initial board of the sudoku, and creates an instance of the class sudoku to solve it.
#### Finally there’s graphics.py but has not been implemented just yet.
