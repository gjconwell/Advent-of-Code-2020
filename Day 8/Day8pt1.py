with open("Day_8_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

accumulator = 0
index = 0
indexlist = []

while (index not in indexlist):
    indexlist.append(index)
    chars = ((inputData[index])[:3])
    value = ((inputData[index])[4:])
    if (chars == "acc"):
        if (value[0] == "+"):
            accumulator += int(value[1:])
            index += 1
        if (value[0] == "-"):
            accumulator -= int(value[1:])
            index += 1
    if (chars == "nop"):
        index += 1
    if (chars == "jmp"):
        if (value[0] == "+"):
            index += int(value[1:])
        if (value[0] == "-"):
            index -= int(value[1:])
print(accumulator)
