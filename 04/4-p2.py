import sys
import re


def is_valid_passport(passport):
    fields = {}
    validation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in passport.strip().split(" "):
        kv_pair = field.split(":")
        fields[kv_pair[0]] = kv_pair[1]
    for field in validation:
        if field not in fields:
            return False
    for k, v in fields.items():
        if k == "byr":
            v = int(v)
            if v < 1920 or v > 2002:
                return False
        if k == "iyr":
            v = int(v)
            if v < 2010 or v > 2020:
                return False
        if k == "eyr":
            v = int(v)
            if v < 2020 or v > 2030:
                return False
        if k == "hgt":
            num = int(v[:-2])
            if v[-2:] == "cm":
                if num < 150 or num > 193:
                    return False
            elif v[-2:] == "in":
                if num < 59 or num > 76:
                    return False
            else:
                return False
        if k == "hcl":
            regex = re.compile("^#[0-9a-f]{6}$")
            if not regex.match(v):
                return False
        if k == "ecl":
            colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            if v not in colors:
                return False
        if k == "pid":
            regex = re.compile("^\d{9}$")
            if not regex.match(v):
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
