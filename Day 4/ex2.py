file = open("input.txt", "r").read()

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = [x.replace("\n", " ") for x in file.split("\n\n")]

valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

valid_passports = 0

def validate(passport):
    passport.sort(key=lambda x: x[0])
    byr = passport[0][1]
    ecl = passport[1][1]
    eyr = passport[2][1]
    hcl = passport[3][1]
    hgt = passport[4][1]
    iyr = passport[5][1]
    pid = passport[6][1]
    #BYR
    if int(byr) < 1920 or int(byr) > 2002:
        return False
    #ECL
    if str(ecl) not in valid_ecls:
        return False
    #EYR
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False
    #HCL
    if not hcl.startswith("#"):
        return False
    try:
        int(hcl.replace("#", ""), 16)
    except:
        return False
    #HGT
    try:
        if hgt.endswith("cm"):
            if int(hgt[0:3]) < 150 or int(hgt[0:3]) > 193:
                return False
        elif hgt.endswith("in"):
            if int(hgt[0:2]) < 59 or int(hgt[0:2]) > 76:
                return False
        else:
            return False
    except:
        return False
    #IYR
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False
    #PID
    if not pid.isdigit() or len(pid) != 9:
        return False
    print(passport)
    return True

for passport in passports:
    fields = passport.split(" ")
    fields_ok = []
    passport_ok = []
    for field in fields:
        field = field.split(":")
        fields_ok.append(field[0])
        if field[0] in required:
            passport_ok.append(field)
    if all(element in fields_ok for element in required):
        if validate(passport_ok):
            valid_passports += 1

print("Valid passports: " + str(valid_passports))