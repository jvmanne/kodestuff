def introduction():
    print("welcome to this awesome game, choose a game from a file or EXIT")


def start_board():
    while True:
        try:
            filename = input("filename: ")
            if filename == "EXIT":
                return "EXIT", "EXIT"
            file = open(filename, "r")

            if check_file(file):
                file.close()
                print("invalid file\n")
                continue
            file.close()
            file = open(filename, "r")

            break
        except:
            print("invalid\n")
    startboard = []
    board = []
    line_count = 0
    for line in file:
        if line_count >= 9:
            board += [line.split()]
        else:
            startboard += [line.split()]
        line_count += 1
    if line_count <= 9:
        for line in range(9):
            board += [[]]
            board[line] += startboard[line]
    file.close()
    for row in range(9):
        for col in range(9):
            startboard[row][col] = int(startboard[row][col])
            board[row][col] = int(board[row][col])
    return startboard, board


def check_file(file):
    str_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    line_count = 0
    for line in file:
        row = []
        row += line.split()
        if len(row) != 9:
            return True
        for col in row:
            if col not in str_numbers:
                return True
        line_count += 1
    if line_count != 9 and line_count != 18:
        return True
    return False


def print_board(board):
    print("\n\n    0 1 2   3 4 5   6 7 8")
    print("  +-------+-------+-------+", end="")
    for x in range(3):
        for y in range(3):
            print("{}{}".format("\n", 3 * x + y), end=" ")
            print("|", end="")
            for a in range(3):
                for b in range(3):
                    print(" {}".format(board[y + x * 3][b + 3 * a]), end="")
                print(" |", end="")
        print("\n  +-------+-------+-------+", end="")


def game_over(board):
    copy_board = []
    copy_board += board
    for x in copy_board:
        if 0 in x:
            return True
    if check_board(copy_board):
        return True
    print("you made it")
    return False


def check_board(board):
    for x in range(9):
        for y in range(9):
            n = 0
            if (y + 1) not in board[x]:
                return True
            for z in range(9):
                if board[z][y] == (x + 1):
                    n += 1
                if n > 1:
                    return True
    for x in range(3):
        for y in range(3):
            for z in range(1, 10):
                if z not in board[x * 3][y * 3:y * 3 + 3] and z not in board[1 + x * 3][y * 3:y * 3 + 3] and z not in \
                        board[2 + x * 3][y * 3:y * 3 + 3]:
                    return True
    return False


def move(startboard, board):
    while True:
        try:
            print("\n[row,column,number]/[clear]/[wipe]/[save]/[load]/[instruction]/[EXIT]")
            place = input(">>> ").split(",")
            while check_move(place, startboard):
                print("invalid\n")
                print("[row,column,number]/[clear]/[wipe]/[save]/[load]/[instruction]/[EXIT]")
                place = input(">>> ").split(",")
            break
        except:
            print("invalid\n")
    if place == ["instruction"]:
        instruction()
    if place == ["save"]:
        save_board(startboard, board)
    if place == ["load"]:
        startboard, board = start_board()
    if place == ["wipe"]:
        board = []
        for x in range(9):
            board += [[]]
            board[x] += startboard[x]
    if place == ["clear"]:
        print_board(startboard)
    if place == ["EXIT"]:
        return "EXIT", "EXIT"
    if len(place) == 3:
        board[int(place[0])][int(place[1])] = int(place[2])
    return startboard, board


def check_move(place, startboard):
    if place in [["clear"], ["wipe"], ["save"], ["load"], ["instruction"], ["EXIT"]]:
        return False
    if len(place) == 3:
        try:
            if int(place[0]) in range(9) and int(place[1]) in range(9) and int(place[2]) in range(10):
                if startboard[int(place[0])][int(place[1])] != 0:
                    return True
                return False
        except:
            pass
    return True


def save_board(startboard, board):
    str_startboard = []
    str_board = []
    for x in range(9):
        str_startboard += [[]]
        str_startboard[x] += startboard[x]
        str_board += [[]]
        str_board[x] += board[x]
    for x in range(9):
        for y in range(9):
            str_startboard[x][y] = str(startboard[x][y])
            str_board[x][y] = str(board[x][y])
    file = open(input("save as: "), "w")
    for x in str_startboard:
        file.writelines(" ".join(x) + "\n")
    for x in str_board[:8]:
        file.writelines(" ".join(x) + "\n")
    file.writelines(" ".join(str_board[8]))
    file.close()
    print("game has been saved")
    return


def instruction():
    print("\n[row,column,number]:\nwrite row,column,number (2,8,9)\nchoose number 0 to clear place")
    print("\n[clear]:\nshows the original board")
    print("\n[wipe]:\nwipes the board to origianl board")
    print("\n[save]:\nsaves board")
    print("\n[load]:\nopen a saved board")
    print("\n[EXIT]:\n write EXIT to exit game")


def main():
    introduction()
    startboard, board = start_board()
    if startboard == "EXIT":
        return
    while game_over(board):
        print_board(board)
        startboard, board = move(startboard, board)
        if board == "EXIT":
            break


def solve():
    startboard, board = start_board()


main()
