def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" *10)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Get player input
        row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
        if any([row > 2, row <0, col > 2, col <0]):
            print("invalid location, the rows and column are between 0 and 2 inclusive. Try again.") 
            continue
        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue
         

        board[row][col] = current_player

        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
