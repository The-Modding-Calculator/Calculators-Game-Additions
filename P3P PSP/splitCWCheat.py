import sys

orgCheatPath = sys.argv[1]
newCheatPath = sys.argv[2]

with open(orgCheatPath) as cheatFile:
    orgCheat = cheatFile.read().split("\n")

linesPerCheat = 0
cheatParts = 0
cheatNmae = "_C0 No Cheat Name"
newCheat = "_S ULES-00000\nULUS10512\n"
for line in orgCheat:
    if line[0:2] == "_L":
        #fix line if addres is the incorect size
        splitLine = line.split(" ")
        if len(splitLine[1]) > 10:
            newAdr = splitLine[1][0:3]
            newAdr += splitLine[1][-7:]
            newLine = "{} {} {}".format(splitLine[0], newAdr, " ".join(splitLine[2:]))
        else:
            newLine = line
        #ok back to spliting the cheats
        linesPerCheat += 1
        if linesPerCheat >= 30:
            cheatParts += 1
            linesPerCheat = 0
            newCheat += "{} ({})\n{}\n".format(cheatName, cheatParts, newLine)
        else:
            newCheat += "{}\n".format(newLine)
            
    elif line[0:2] == "_C":
        cheatName = line
        linesPerCheat = 0
        cheatParts = 0
        newCheat += "{} (0)\n".format(line)
    else:
        newCheat += "{}\n".format(line)

with open(newCheatPath, "w") as newCheatFile:
    newCheatFile.write(newCheat)

