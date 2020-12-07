file = open("input.txt", "r").read()

groups = [x.replace("\n", "") for x in file.split("\n\n")]
pts = 0

for group in groups:
    pts += len(set(group))

print("Points in total: " + str(pts))