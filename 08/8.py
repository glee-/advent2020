import sys


memory = {}


f = open(sys.argv[1])

loadcounter = 0
for line in f.readlines():
    stripped = line.strip()
    split = stripped.split(" ")
    memory[loadcounter] = [split[0], int(split[1])]
    loadcounter += 1

globalval = 0
ipointer = 0

seen_instr = set()
while ipointer not in seen_instr:
    seen_instr.add(ipointer)
    if memory[ipointer][0] == "jmp":
        ipointer += memory[ipointer][1]
        continue
    elif memory[ipointer][0] == "acc":
        globalval += memory[ipointer][1]

    ipointer += 1

print(globalval)
