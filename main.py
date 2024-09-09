#!/usr/bin/python3


def is_position_valid(position):
    if (position < 0) or (position > 8):
        print("Out of range. Enter position 1-9.")
        return False

    if board[position] != empty_cell:
        print(f"Position {position+1} is already set!")
        return False

    return True


def is_win(current_player):
    # check horizontals
    i = 0
    while i < len(board):
        if board[i] == board[i + 1] == board[i + 2] == current_player:
            return True
        i = i + 3

    # check verticals
    i = 0
    while i < 3:
        if board[i] == board[i + 3] == board[i + 6] == current_player:
            return True
        i = i + 1

    # check diagonals

    if board[0] == board[4] == board[8] == current_player:
        return True

    if board[2] == board[4] == board[6] == current_player:
        return True

    return False


def play_game():
    global current_player

    position = int(input(f"\nPlayer '{current_player}' enter position [1-9]: ")) - 1

    if not is_position_valid(position):
        return

    board[position] = current_player

    i = 0
    while i < len(board):
        print(f"{board[i]} {board[i+1]} {board[i+2]}")
        i = i + 3

    if is_win(current_player):
        print(f"\nWinner: {current_player}")
        exit(0)

    current_player = opposite_player[current_player]

    for i in board:
        if i == empty_cell:
            return

    print("Game over! No one is win :(")
    exit(0)


if __name__ == "__main__":
    empty_cell = "."
    current_player = "x"
    opposite_player = {"x": "o", "o": "x"}

    print("Game started!")

    global board
    board = [empty_cell for i in range(int(9))]

    print(f"{board[0]} {board[1]} {board[2]}")
    print(f"{board[3]} {board[4]} {board[5]}")
    print(f"{board[6]} {board[7]} {board[8]}")

    while True:
        play_game()
