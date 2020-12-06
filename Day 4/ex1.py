file = open("input.txt", "r").read()

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passports = [x.replace("\n", " ") for x in file.split("\n\n")]

valid_passports = 0

for passport in passports:
    fields = passport.split(" ")
    fields_ok = []
    for field in fields:
        field = field.split(":")
        fields_ok.append(field[0])
    if all(element in fields_ok for element in required):
        valid_passports += 1

print("Valid passports: " + str(valid_passports))