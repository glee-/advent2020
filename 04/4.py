import sys


def is_valid_passport(passport):
    fields = {}
    validation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in passport.strip().split(" "):
        kv_pair = field.split(":")
        fields[kv_pair[0]] = kv_pair[1]
    for field in validation:
        if field not in fields:
            return False
    return True


passports = []
f = open(sys.argv[1])

lines = []
curline = ""
for line in f.readlines():
    stripped = line.strip()
    if stripped == "":
        lines.append(curline)
        curline = ""
    else:
        curline += stripped + " "
lines.append(curline)
valid = 0
for line in lines:
    valid += is_valid_passport(line)
print(valid)
