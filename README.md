 Tic Tac Toe Game

This is a simple command-line implementation of the classic Tic Tac Toe game in Python. Two players can take turns to play the game on a 3x3 board.

## How to Play

1. **Set up the environment:**
   - Make sure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

2. **Download the game:**
   - Copy the `tictactoe.py` file to your local machine.

3. **Run the game:**
   - Open your command line interface (CLI).
   - Navigate to the directory where you saved `tictactoe.py`.
   - Run the script using Python:
     ```sh
     python tictactoe.py
     ```

4. **Game Instructions:**
   - The game will prompt Player X to enter their move.
   - Enter the row and column numbers separated by a space. For example, `0 1` places your mark in the first row, second column.
   - Player O will then be prompted to enter their move.
   - The game will display the updated board after each move.
   - The game checks for a winner after each move and announces the winner or declares a draw when appropriate.

## Game Rules

- The game is played on a 3x3 grid.
- Players take turns to place their mark (X or O) in an empty cell.
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
- If all cells are filled and no player has three marks in a row, the game is a draw.
