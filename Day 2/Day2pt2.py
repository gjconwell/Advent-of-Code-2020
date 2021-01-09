

with open("Day_2_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

valid = 0
count = 0
key = 0
rangetop = 0
rangebot = 0
pw = 0

for i in inputData:
    local = i.find("-")
    local2 = i.find(" ")
    local3 = i.find(":")
    rangebot = int(i[:local])
    rangetop = int(i[local + 1:local2])
    key = i[local3 - 1]
    pw = i[local3 + 2:]
    for j in pw:
        count += 1
        if (j == key and count == rangebot):
            count2 = 0
            for k in pw:
                count2 += 1
                if (k == key and count2 == rangetop):
                    valid -= 1
            count2 = 0
        if (j == key and count == rangebot):
            valid += 1
            break
        if (j == key and count == rangetop):
            valid += 1
    count = 0
print(valid)
