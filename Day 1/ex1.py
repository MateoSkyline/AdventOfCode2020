file = open("input.txt", "r")
list_1 = []
list_2 = []
for x in file:
    list_1.append(x)
    list_2.append(x)

    
for x in list_1:
    for y in list_2:
        if (int(x) + int(y)) == 2020:
            print(x)
            print(y)
            print(int(x)*int(y))

print("End")
