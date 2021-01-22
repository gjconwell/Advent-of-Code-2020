with open("Day_11_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

count = 0
flip = [0]

for i in inputData: # turns the string inside inputData into a sub list
    li = list(i)
    inputData[count] = li
    count += 1

def adjacent(instructions):
    global count
    valid = 0
    try:
        row = instructions[indexvert + valuevert] #row selection
        if (indexvert + valuevert) < 0:
            valid += 1
    except:
        pass
    try:
        column = row[indexhor + valuehor] # column selection
        if (indexhor + valuehor) < 0:
            if column == "#":
                valid += 1
    except:
        pass
    if (valid == 2):
        count += 1

while flip != []: #runs until flip has nothing added thus no seats are change, meaning seating is static
    indexvert = -len(inputData)
    flip = [] #which values to flip
    while indexvert != 0:
        row = inputData[indexvert]
        indexhor = -len(row)
        while indexhor != 0:
            count = 0
            column = row[indexhor]
            if column != ".": # Detects all 8( or -) adjacent characters
                valuevert = -1
                valuehor = -1
                adjacent(inputData)
                valuehor += 1
                adjacent(inputData)
                valuehor += 1
                adjacent(inputData)
                valuevert += 1
                adjacent(inputData)
                valuehor -= 2
                adjacent(inputData)
                valuevert += 1
                adjacent(inputData)
                valuehor += 1
                adjacent(inputData)
                valuehor += 1
                adjacent(inputData)
                if count == 0 and column == "L":
                    flip.append("%" + str(indexvert) + "/" + str(indexhor)) #if there are no #'s then this coordinate is added to flip
                if count >= 4 and column == "#":
                    flip.append("%" + str(indexvert) + "/" + str(indexhor)) #if there are 4 or more #'s then this coordinate is added to flip
            indexhor += 1
        indexvert += 1

    for i in flip: #flips all values based on their coordinates
        local = i.find("%") #detecting partitioning key characters
        local2 = i.find("/") #detecting partitioning key characters
        indexvert = i[local + 1:local2]
        indexhor = i[local2 + 1:]
        row = inputData[int(indexvert)]
        if row[int(indexhor)] == "L": #flips to occupied if empty
            row[int(indexhor)] = "#"
            continue
        if row[int(indexhor)] == "#": #flips to empty if occupied
            row[int(indexhor)] = "L"
        column = row[int(indexhor)]

count = 0
for j in inputData: #detects all occupied seats
    for i in j:
        if i == "#":
            count += 1

print(count)
