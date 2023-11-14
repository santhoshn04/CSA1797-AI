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

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        player = players[current_player]
        print(f"\nPlayer {player}'s turn:")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        print_board(board)
        if check_winner(board, player):
            print(f"\nPlayer {player} wins!")
            break
        if is_board_full(board) and not check_winner(board, player):
            print("\nIt's a draw!")
            break
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
