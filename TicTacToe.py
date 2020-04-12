board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
current_player = "X"
winner = []
game_still_going = True


def display_board(board_game):
    print(board_game[0], "|", board_game[1], "|", board_game[2]+"\n"+board_game[3], "|", board_game[4],
          "|", board_game[5]+"\n"+board_game[6], "|", board_game[7], "|", board_game[8])


def player_turn(player):
    display_board(board)
    while game_still_going is True:
        print(f"{player}, It's your turn")
        spot = int(input("Please pick a spot (number between 1-9): "))
        while True:
            if 0 < spot < 10:
                if board[spot-1] == "-":
                    board[spot-1] = player
                    break
                else:
                    print("spot is taken")
                    spot = int(input("Please pick other number (between 1-9): "))
            else:
                print(f"{spot} is not a legal spot. Please pick a number between 1-9.")
                spot = int(input("Please pick a spot (between 1-9): "))

        display_board(board)
        check_if_game_is_over()
        player = flip_player()


def check_if_game_is_over():
    check_for_winner()
    if game_still_going is True:
        check_for_tie()


def check_for_winner():
    global game_still_going
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()
    if row_win is True or column_win is True or diagonal_win is True:
        game_still_going = False
        print(f"The winner is {current_player}!!")
        winner.append(current_player)


def check_rows():
    check = False
    if board[0] == board[1] == board[2]:
        if board[0] != "-":
            check = True
    if board[3] == board[4] == board[5]:
        if board[3] != "-":
            check = True
    if board[6] == board[7] == board[8]:
        if board[6] != "-":
            check = True
    return check


def check_columns():
    check = False
    if board[0] == board[3] == board[6]:
        if board[0] != "-":
            check = True
    if board[1] == board[4] == board[7]:
        if board[1] != "-":
            check = True
    if board[2] == board[5] == board[8]:
        if board[2] != "-":
            check = True
    return check


def check_diagonals():
    check = False
    if board[0] == board[4] == board[8]:
        if board[0] != "-":
            check = True
    if board[2] == board[4] == board[6]:
        if board[2] != "-":
            check = True
    return check


def check_for_tie():
    global game_still_going
    if "-" not in board:
        print("Game is Over with a tie")
        game_still_going = False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return current_player


player_turn(current_player)
