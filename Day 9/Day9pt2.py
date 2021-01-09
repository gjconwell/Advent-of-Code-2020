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

invalid = rinse(inputData)
index = 0
count = 0

def contiguous(instructions):
    global index
    global count
    preamble = []
    valid = 0
    count += 1
    numsum = 0
    while (numsum < invalid): # builds the preamble until its sum is greater than the invalid value
        num = int(instructions[index])
        preamble.append(num)
        index += 1
        numsum  = sum(preamble)
    index = count
    if (numsum == invalid): # detects to see if the sum equals the invalid value
        preamble.sort()
        return preamble[0] + preamble[(len(preamble) - 1)]
    if (numsum > invalid):
        preamble.pop(0) # removes the first element of the preamble
        numsum  = sum(preamble)
        if (numsum == invalid): # detects to see if the sum equals the invalid value
            preamble.sort()
            return preamble[0] + preamble[(len(preamble) - 1)]
        return contiguous(inputData)

print(contiguous(inputData))
