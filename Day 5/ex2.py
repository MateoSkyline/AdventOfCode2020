file = open("input.txt", "r")

seats = []

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

def missingID(IDs):
    missing = []
    for ID in IDs:
        if (ID-1) not in IDs or (ID+1) not in IDs:
            missing.append(ID)
    return int(missing[1])+1

for line in file:
    seats.append(getID(getRow(line), getCol(line)))

seats.sort()
print("My seat ID is " + str(missingID(seats)))