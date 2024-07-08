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

def get_available_moves(board):
    
    return [(i,j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def make_move(board, position, player):
    board[position] = player

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def easy_ai_move():
    return random.choice(get_available_moves(board))

def hard_ai_move():
    return get_best_move(board)
    
def tic_tac_toe():
    difficulty=input("select difficylty  0(easy) 1(hard): ")
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
        if difficulty == 0: row, col = easy_ai_move()
        else: row,col = hard_ai_move()
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
        
if __name__ == "__main__":
    tic_tac_toe()
