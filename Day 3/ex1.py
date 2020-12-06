file = open("input.txt", "r")

count = 0

for line in file:
    item = line.split(" ")
    char = item[1].replace(":", "")
    pwd = item[2].replace("\n", "")
    num = item[0].split("-")

    if pwd.count(char) >= int(num[0]) and pwd.count(char) <= int(num[1]):
        count += 1

print(count)
