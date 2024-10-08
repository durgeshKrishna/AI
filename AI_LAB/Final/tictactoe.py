import math

def print_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    """
    Checks if the given player has won the game.
    """
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """
    Checks if the board is full.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def get_available_moves(board):
    """
    Returns a list of available moves on the board.
    Each move is represented as a tuple (row, col).
    """
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves

def minimax(board, depth, is_maximizing):
    """
    Implements the Minimax algorithm.
    
    :param board: Current game board.
    :param depth: Current depth in the game tree.
    :param is_maximizing: True if the current move is for the maximizing player (AI).
    :return: A tuple (score, move) where move is a tuple (row, col).
    """
    if is_winner(board, 'X'):
        return (10 - depth, None)  # AI wins
    if is_winner(board, 'O'):
        return (-10 + depth, None)  # Human wins
    if is_board_full(board):
        return (0, None)  # Draw

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'X'  # AI makes a move
            score, _ = minimax(board, depth + 1, False)  # Recurse for the minimizing player
            board[row][col] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)
    else:
        best_score = math.inf
        best_move = None
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'O'  # Human makes a move
            score, _ = minimax(board, depth + 1, True)  # Recurse for the maximizing player
            board[row][col] = ' '  # Undo the move
            if score < best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)

def find_best_move(board):
    """
    Determines the best move for the AI using the Minimax algorithm.
    
    :param board: Current game board.
    :return: The best move as a tuple (row, col).
    """
    score, move = minimax(board, 0, True)
    return move

def play_game():
    """
    Manages the game loop, handling user input and AI moves.
    """
    # Initialize empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                move = input("Enter your move as row and column (e.g., 1 1 for center): ")
                row, col = map(int, move.strip().split())
                if row not in range(3) or col not in range(3):
                    print("Row and column must be between 0 and 2. Try again.")
                    continue
                if board[row][col] != ' ':
                    print("Cell already occupied! Try again.")
                    continue
                board[row][col] = 'O'
                break
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space (e.g., 0 2).")
        
        print_board(board)

        # Check for human win
        if is_winner(board, 'O'):
            print("Congratulations! You win!")
            break

        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'X'
            print_board(board)

            # Check for AI win
            if is_winner(board, 'X'):
                print("AI wins! Better luck next time.")
                break

            # Check for draw
            if is_board_full(board):
                print("It's a draw!")
                break
        else:
            # No moves left
            print("No moves left! It's a draw!")
            break

if __name__ == "__main__":
    play_game()
