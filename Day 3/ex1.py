file = open("input.txt", "r")

trees = 0
maxY = 30

moveRight = 3
moveDown = 1

actualX = 0
actualY = 0

iteration = 0

for line in file:
    if iteration == actualY:
        check = line[actualX]
        if check == "#":
            trees += 1
    actualY += moveDown
    if actualX + moveRight <= maxY:
        actualX += moveRight
    else:
        actualX = (actualX + moveRight) - maxY - 1
    iteration += 1

print("Total number of trees: " + str(trees))