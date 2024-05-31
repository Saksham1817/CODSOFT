import copy

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax_algorithm(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_available_cells(board):
            board[i][j] = 'O'
            score = minimax_algorithm(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_available_cells(board):
            board[i][j] = 'X'
            score = minimax_algorithm(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    optimal_move = None

    for i, j in get_available_cells(board):
        board[i][j] = 'O'
        move_score = minimax_algorithm(board, 0, False)
        board[i][j] = ' '

        if move_score > best_score:
            optimal_move = (i, j)
            best_score = move_score

    return optimal_move

def get_user_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")

    while True:
        display_board(board)

        if current_player == 'X':
            row, col = get_user_move()
            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Cell already occupied. Try again.")
                continue
        else:
            print("AI is making a move...")
            move = find_best_move(copy.deepcopy(board))
            board[move[0]][move[1]] = 'O'

        if check_winner(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            break
        elif is_full(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
