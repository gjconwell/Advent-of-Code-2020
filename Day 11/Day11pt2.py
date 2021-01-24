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
    global error
    valid = 0
    try:
        row = instructions[indexvert + valuevert] #row selection
        if (indexvert + valuevert) < 0:
            valid += 1
    except:
        error = True
    try:
        column = row[indexhor + valuehor] # column selection
        if (indexhor + valuehor) < 0:
            if column == "L":
                error = True #
            if column == "#":
                valid += 1
                error = True
    except:
        error = True
    if (valid == 2):
        count += 1

def reset(): #resets variable for next adjacent/Line of Sight test
    global valuehor
    global valuevert
    global error
    valuehor = 0
    valuevert = 0
    error = False

while flip != []: #runs until flip has nothing added thus no seats are change, meaning seating is static
    indexvert = -len(inputData)
    flip = []
    while indexvert != 0:
        row = inputData[indexvert]
        indexhor = -len(row)
        while indexhor != 0:
            count = 0
            column = row[indexhor]
            if column != ".": # Detects all 8( or -) adjacent characters
                reset()
                while error != True: #Light of Sight: right
                    valuehor += 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: left
                    valuehor -= 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: up
                    valuevert -= 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: down
                    valuevert += 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: down right
                    valuehor += 1
                    valuevert += 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: down left
                    valuehor -= 1
                    valuevert += 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: up right
                    valuehor += 1
                    valuevert -= 1
                    adjacent(inputData)
                reset()
                while error != True: #Light of Sight: up left
                    valuehor -= 1
                    valuevert -= 1
                    adjacent(inputData)
                if count == 0 and column == "L":
                    flip.append("%" + str(indexvert) + "/" + str(indexhor)) #if there are no #'s then this coordinate is added to flip
                if count >= 5 and column == "#":
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
