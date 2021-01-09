with open("Day_8_Input2.txt") as input:
    inputData = input.read().split("\n")[:-1]

def didExecute(instructions): # true if executes, false if not

    accumulator = 0 # Total
    index = 0 # Index of current instruction
    indexlist = [] # Indexes of instructions that have been run

    while (index not in indexlist):

        if (index == len(instructions)): # Len instructions is 1 greater than the index
            return True, accumulator

        indexlist.append(index)
        chars = instructions[index][:3]
        value = instructions[index][4:]

        if (chars == "acc"):
            accumulator += int(value)
            index += 1
        elif (chars == "nop"):
            index += 1
        elif (chars == "jmp"):
            index += int(value)

    return False, accumulator

print(didExecute(inputData))
