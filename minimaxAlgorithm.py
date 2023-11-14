def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])
def evaluate(board):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    else:
        return 0
def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0
    if is_maximizing:
        max_eval = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
        return min_eval
def find_best_move(board):
    best_eval = -float("inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                eval = minimax(board, 0, False)
                board[row][col] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        best_move = find_best_move(board)
        if best_move:
            board[best_move[0]][best_move[1]] = "X"
            print_board(board)
            if check_winner(board, "X"):
                print("Computer wins!")
                break
            if is_board_full(board):
                print("It's a draw!")
                break
if __name__ == "__main__":
    main()
