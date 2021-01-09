

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
    pw = i[local3 + 1:]
    for j in pw:
        if (j == key):
            count += 1
    if (rangebot <= count <= rangetop):
        valid += 1
    count = 0

print(valid)
