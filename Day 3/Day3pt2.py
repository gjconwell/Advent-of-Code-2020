with open("Day_3_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]
with open("Day_3_Input2.txt") as input:
    inputData2 = input.read().split("\n")[:-1]
total = 1
hits = []
for j in inputData2:
    run = int(j[0])
    rise = int(j[2])
    xaxis = 0
    hit = 0
    for i in inputData:
        if (rise > 1):
            break
        if (xaxis >= 31):
            xaxis = xaxis - 31
        if (i[xaxis] == "#"):
            hit += 1
        xaxis += run
    if (rise > 1):
        xaxis = 0
        inputlist = list(inputData)
        for k in range (0, 322, rise):
            inputlisting = inputlist[k]
            if (xaxis >= 31):
                    xaxis = xaxis - 31
            if (inputlisting[xaxis] == "#"):
                    hit += 1
            xaxis += run
    hits.append(hit)
for l in hits:
    total *= l
print(total)
