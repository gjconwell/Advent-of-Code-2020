with open("Day_14_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

memory = dict()
for i in inputData:
    if i[1] == "a":
        local = i.find("=")
        mask = list(i[local + 2:])
    if i[1] != "a":
        local = i.find("=")
        value = int(i[local + 2:])
        localmem1 = i.find("[")
        localmem2 = i.find("]")
        mem = i[localmem1 + 1:localmem2]
        input = list((36 - len(bin(value).replace("0b", ""))) * "0" + bin(value).replace("0b", ""))
        index = 0
        for j in mask:
            if j != "X":
                input[index] = j
            index += 1
        collect = ''
        for k in input:
            collect = collect + k
        memory[mem] = collect
summer = 0
print(memory)
for i in memory:
    localrev = memory[i].find("1")
    summer += int(memory[i][localrev:], 2)
print(summer)
