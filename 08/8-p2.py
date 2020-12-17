import sys


def test_mem(memory, location, jmp=False, nop=False):
    memsize = len(memory)
    # swap mem
    if nop:
        memory[location][0] = "jmp"
    elif jmp:
        memory[location][0] = "nop"

    globalval = 0
    ipointer = 0

    seen_instr = set()
    while ipointer not in seen_instr:
        if ipointer == memsize:
            return True, globalval
        seen_instr.add(ipointer)
        if memory[ipointer][0] == "jmp":
            ipointer += memory[ipointer][1]
            continue
        elif memory[ipointer][0] == "acc":
            globalval += memory[ipointer][1]

        ipointer += 1

    # revert change
    if nop:
        memory[location][0] = "nop"
    elif jmp:
        memory[location][0] = "jmp"
    return False, -1


memory = {}
nop_locations = []
jmp_locations = []

f = open(sys.argv[1])

loadcounter = 0
for line in f.readlines():
    stripped = line.strip()
    split = stripped.split(" ")
    if split[0] == "jmp":
        jmp_locations.append(loadcounter)
    if split[0] == "nop":
        nop_locations.append(loadcounter)
    memory[loadcounter] = [split[0], int(split[1])]
    loadcounter += 1

for location in nop_locations:
    retstatus, val = test_mem(memory, location, nop=True)
    if retstatus:
        print(location, val)
for location in jmp_locations:
    retstatus, val = test_mem(memory, location, jmp=True)
    if retstatus:
        print(location, val)
