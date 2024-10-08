import math

def print_board(board):
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i != 2:
            print("---------")

def evaluate(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return 10 if board[condition[0]] == 'X' else -10
    return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    
    # Base cases: check for a winner or if no more moves
    if score != 0: 
        return score - depth  # Subtracting depth to prioritize faster wins
    if ' ' not in board: 
        return 0  # No empty spots, it's a draw
    
    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Simulate X's move
                value = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '  # Undo move
                best = max(best, value)
                alpha = max(alpha, best)
                if beta <= alpha:  # Prune the branch
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # Simulate O's move
                value = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '  # Undo move
                best = min(best, value)
                beta = min(beta, best)
                if beta <= alpha:  # Prune the branch
                    break
        return best

def find_best_move(board):
    best_move, best_val = -1, -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'  # Simulate X's move
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '  # Undo move
            if move_val > best_val:
                best_move, best_val = i, move_val
    return best_move

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return 'Draw' if ' ' not in board else None

def play_game():
    board, player = [' '] * 9, 'O'  # Start with player O
    while True:
        print_board(board)
        if player == 'X':
            move = find_best_move(board)
        else:
            try:
                move = int(input("Enter your move (0-8): "))
                if board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except (IndexError, ValueError):
                print("Invalid input. Enter a number between 0 and 8.")
                continue
        board[move] = 'X' if player == 'X' else 'O'
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!" if winner != 'Draw' else "It's a draw!")
            break
        player = 'X' if player == 'O' else 'O'

play_game()
