with open("Day_9_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

count = 0
index = 0

def rinse(instructions):
    global index
    global count
    preamble = []
    valid = 0
    count += 1
    while (len(preamble) != 25):
        num = instructions[index]
        preamble.append(num)
        index += 1
    numsum = int(instructions[index])
    for i in (preamble):
        if (valid == 1):
            break
        for j in (preamble):
            if (int(i) + int(j) == numsum):
                valid += 1
                break
    index = count
    if (valid == 0):
        return numsum
    return rinse(inputData)

print(rinse(inputData))
