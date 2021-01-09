with open("Day_6_Input.txt") as input:
    inputData = input.read().split("\n")

chars = []
dupechars =[]
count = 0
total = 0
group = 0

for i in inputData:
    if (len(i.strip()) != 0):
        group += 1
    if (len(i.strip()) == 0):
        for j in dupechars:
            grpcount = chars.count(j)
            if (grpcount == group):
                count += 1
        total += count
        chars = []
        dupechars = []
        group = 0
        count = 0
    for j in i:
        chars.append(j)
    for j in i:
        if (j not in dupechars):
            dupechars.append(j)
print(total)
