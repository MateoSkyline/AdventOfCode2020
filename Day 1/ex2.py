file = open("input.txt", "r")
list_1 = []
list_2 = []
list_3 = []
for x in file:
    list_1.append(x)
    list_2.append(x)
    list_3.append(x)
    
for x in list_1:
    for y in list_2:
        for z in list_3:
            if (int(x) + int(y) + int(z)) == 2020:
                print(int(x)*int(y)*int(z))

print("End")
