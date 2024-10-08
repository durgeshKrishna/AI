import math

# Define players
PLAYER_X = "X"  # Human
PLAYER_O = "O"  # AI
EMPTY = " "

# Initialize the board
def create_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(EMPTY)
        board.append(row)
    return board

# Print the board
def print_board(board):
    for row in board:
        row_str = ""
        for i in range(len(row)):
            row_str += row[i]
            if i < len(row) - 1:
                row_str += "|"
        print(row_str)
        print("-----")

# Check if the current player is a winner
def is_winner(board, player):
    # Check rows
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != player:
                win = False
                break
        if win:
            return True

    # Check columns
    for i in range(3):
        win = True
        for j in range(3):
            if board[j][i] != player:
                win = False
                break
        if win:
            return True

    # Check main diagonal
    win = True
    for i in range(3):
        if board[i][i] != player:
            win = False
            break
    if win:
        return True

    # Check anti-diagonal
    win = True
    for i in range(3):
        if board[i][2 - i] != player:
            win = False
            break
    if win:
        return True

    return False

# Check if the board is full
def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

# Get all available moves (empty spots)
def get_available_moves(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_moves.append((i, j))
    return available_moves

# Alpha-Beta Pruning algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, PLAYER_X):
        # Human wins
        return -1
    elif is_winner(board, PLAYER_O):
        # AI wins
        return 1
    elif is_full(board):
        # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        moves = get_available_moves(board)
        for move in moves:
            i, j = move
            board[i][j] = PLAYER_O
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY
            if score > best_score:
                best_score = score
            if best_score > alpha:
                alpha = best_score
            if beta <= alpha:
                break  # Alpha-Beta Pruning
        return best_score
    else:
        best_score = math.inf
        moves = get_available_moves(board)
        for move in moves:
            i, j = move
            board[i][j] = PLAYER_X
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = EMPTY
            if score < best_score:
                best_score = score
            if best_score < beta:
                beta = best_score
            if beta <= alpha:
                break  # Alpha-Beta Pruning
        return best_score

# Get the best move for the AI using Alpha-Beta Pruning
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    moves = get_available_moves(board)
    for move in moves:
        i, j = move
        board[i][j] = PLAYER_O
        score = minimax(board, 0, False, alpha, beta)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Check if the game is over
def is_game_over(board):
    if is_winner(board, PLAYER_X):
        return True
    if is_winner(board, PLAYER_O):
        return True
    if is_full(board):
        return True
    return False

# Main game loop
def play_game():
    board = create_board()
    current_player = PLAYER_X

    while not is_game_over(board):
        print_board(board)
        if current_player == PLAYER_X:
            print("Player X's turn!")
            # Input validation loop
            valid_move = False
            while not valid_move:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                    if row < 0 or row > 2 or col < 0 or col > 2:
                        print("Row and column must be between 0 and 2. Try again.")
                        continue
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_X
                        valid_move = True
                    else:
                        print("Cell is already occupied. Try again.")
                except ValueError:
                    print("Invalid input. Please enter integers between 0 and 2.")
            current_player = PLAYER_O
        else:
            print("AI's turn!")
            move = get_best_move(board)
            if move:
                i, j = move
                board[i][j] = PLAYER_O
                print(f"AI placed an '{PLAYER_O}' in position ({i}, {j})")
                current_player = PLAYER_X
            else:
                # No available moves (shouldn't happen if is_game_over works correctly)
                print("No available moves for AI.")
                break

    print_board(board)
    if is_winner(board, PLAYER_X):
        print("Player X wins!")
    elif is_winner(board, PLAYER_O):
        print("AI wins!")
    else:
        print("It's a tie!")

# Start the game
if __name__ == "__main__":
    play_game()
