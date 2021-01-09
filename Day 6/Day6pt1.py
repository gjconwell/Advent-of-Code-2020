with open("Day_6_Input.txt") as input:
    inputData = input.read().split("\n")

chars = []
count = 0
total = 0

for i in inputData:
    if (len(i.strip()) == 0):
        total += count
        chars = []
        count = 0
    for j in i:
        if (j not in chars):
            chars.append(j)
            count += 1
print(total)
