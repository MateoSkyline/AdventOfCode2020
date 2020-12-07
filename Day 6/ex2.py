file = open("input.txt", "r").read()

groups = [x.replace("\n", ";") for x in file.split("\n\n")]
pts = 0

def checkLetters(people):
    in_pts = 0
    for x in range(97, 123): #a
        flag = True
        for person in people:
            if chr(x) not in person:
                flag = False
        if flag:
            in_pts += 1
    return in_pts

for group in groups:
    ppl = [x for x in group.split(";")]
    pts += checkLetters(ppl)

print("Sum of everyone-answered questions is " + str(pts))