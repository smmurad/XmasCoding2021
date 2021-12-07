def getNewBoard():
    return [[0 for x in range(5)] for i in range(5)]

def boardHasWon(board, board_ix):
    # isolate board
    board = board[25*board_ix:board_ix*25+25]

    hor_win = False
    # check horizontal
    for y in range(5):
        hor_win = True
        for x in range(5):
            if board[5*y+x] != "0":
                hor_win = False
                break
        if hor_win:
            break

    if hor_win:
        return True

    vert_win = False
    # check vertical
    for x in range(5):
        vert_win = True
        for y in range(5):
            if board[5 * y + x] != "0":
                vert_win = False
                break
        if vert_win:
            break

    return vert_win

def solve1():
    with open("input/numbers4.txt", "r") as fh:
        bingo_numbers = fh.read().split(",")

    with open("input/input4.txt", "r") as fh:
        boards = fh.read().split()
    numBoards = int(len(boards)/(5*5))

    # Mark matched nums
    for num in bingo_numbers:
        for b_ix in range(len(boards)):
            bNum = boards[b_ix]
            if bNum == num:
                boards[b_ix] = '0'
        # Check if any board has a full line
        for board_ix in range(numBoards):
            if boardHasWon(boards, board_ix):
                sum = 0
                for i in boards[board_ix * 25:board_ix * 25 + 25]:
                    sum += int(i)
                return sum * int(num)
    return 0


def solve2():
    with open("input/numbers4.txt", "r") as fh:
        bingo_numbers = fh.read().split(",")

    with open("input/input4.txt", "r") as fh:
        boards = fh.read().split()
    numBoards = int(len(boards)/(5*5))
    boardWin = [False for i in range(numBoards)]
    boardsWon = 0
    # Mark matched nums
    for num in bingo_numbers:
        for b_ix in range(len(boards)):
            bNum = boards[b_ix]
            if bNum == num:
                boards[b_ix] = '0'
        # Check if any board has a full line
        for board_ix in range(numBoards):
            if boardWin[board_ix]:
                continue
            if boardHasWon(boards, board_ix):
                boardsWon += 1
                boardWin[board_ix] = True
                if boardsWon == numBoards:
                    sum = 0
                    for i in boards[board_ix * 25:board_ix * 25 + 25]:
                        sum += int(i)
                    return sum * int(num)
