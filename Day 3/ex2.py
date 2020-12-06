maxY = 30

def forest(moveRight, moveDown):
    file = open("input.txt", "r")
    trees = 0
    actualX = 0
    actualY = 0
    iteration = 0
    for line in file:
        if iteration == actualY:
            check = line[actualX]
            if check == "#":
                trees += 1
            if actualX + moveRight <= maxY:
                actualX += moveRight
            else:
                actualX = (actualX + moveRight) - maxY - 1
            actualY += moveDown
        iteration += 1
    return trees

print(forest(1,1) * forest(3,1) * forest(5,1) * forest(7,1) * forest(1,2))


