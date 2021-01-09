with open("Day_3_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

xaxis = 0
hit = 0

for i in inputData:
    if (xaxis >= 31):
        xaxis = xaxis -31
    if (i[xaxis] == "#"):
        hit += 1
    xaxis += 3
print(hit)
