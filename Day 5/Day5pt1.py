with open("Day_5_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

total = 0

for i in inputData:
    numrow = []
    for k in range(128):
        numrow.append(k)
    numcolumn = []
    for x in range(8):
        numcolumn.append(x)
    for j in i:
        if (j == "F"):
            upper = int((len(numrow) / 2))
            del numrow[upper:]
        else:
            lower = int((len(numrow) / 2))
            del numrow[:lower]
        if (j == "L"):
            upper = int((len(numcolumn) / 2))
            del numcolumn[upper:]
        if (j == "R"):
            lower = int((len(numcolumn) / 2))
            del numcolumn[:lower]
    totaltemp = ((numrow[0] * 8) + numcolumn[0])
    if (totaltemp > total):
        total = totaltemp
print(total)
