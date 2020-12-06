file = open("input.txt", "r")

highest = 0

def getRow(boardpass):
    board_row = boardpass[0:7]
    board_row = board_row.replace("F", "0")
    board_row = board_row.replace("B", "1")
    return int(board_row, 2)

def getCol(boardpass):
    board_col = boardpass[7:10]
    board_col = board_col.replace("L", "0")
    board_col = board_col.replace("R", "1")
    return int(board_col, 2)

def getID(row, col):
    return (row * 8) + col

for line in file:
    seat = getID(getRow(line), getCol(line))
    if seat > highest:
        highest = seat

print("Highest seat ID on boarding pass is " + str(highest))