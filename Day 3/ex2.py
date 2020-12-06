file = open("input.txt", "r")

count = 0

for line in file:
    item = line.split(" ")
    char = item[1].replace(":", "")
    pwd = item[2].replace("\n", "")
    num = item[0].split("-")

    if pwd[int(num[0])-1] == char:
        if pwd[int(num[1])-1] == char:
            pass
        else:
            count += 1
    else:
        if pwd[int(num[1])-1] == char:
            count += 1
        

print(count)
