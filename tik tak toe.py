def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + board[i][j] + " |", end="")
        print("\n-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    print_board(board)
    while True:
        print(f"Player {current_player}'s turn.")
        row = int(input("Enter row (1, 2, or 3): ")) - 1
        col = int(input("Enter column (1, 2, or 3): ")) - 1
        if board[row][col] != " ":
            print("That spot is already taken!")
            continue
        board[row][col] = current_player
        print_board(board)
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

tic_tac_toe()
