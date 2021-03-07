with open("Day_12_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

y = 0
x = 0
direction1 = 3 #North = 4, East = 3, South = 2, West = 1
direction2 = 4 #North = 4, East = 3, South = 2, West = 1
unit1 = 10
unit2 = 1

def move(local):
    global y
    global x
    if direction1 == 4:
        y += (local * unit1)
    if direction1 == 3:
        x += (local * unit1)
    if direction1 == 2:
        y -= (local * unit1)
    if direction1 == 1:
        x -= (local * unit1)
    if direction2 == 4:
        y += (local * unit2)
    if direction2 == 3:
        x += (local * unit2)
    if direction2 == 2:
        y -= (local * unit2)
    if direction2 == 1:
        x -= (local * unit2)

for i in inputData:
    if i[0] == "F":
        local = int(i[1:])
        move(local)
    if i[0] == "N":
        local = int(i[1:])
        if direction1 == 4:
            unit1 += local
        if direction2 == 4:
            unit2 += local
        if direction1 == 2:
            unit1 -= local
        if direction2 == 2:
            unit2 -= local
    if i[0] == "S":
        local = int(i[1:])
        if direction1 == 2:
            unit1 += local
        if direction2 == 2:
            unit2 += local
        if direction1 == 4:
            unit1 -= local
        if direction2 == 4:
            unit2 -= local
    if i[0] == "E":
        local = int(i[1:])
        if direction1 == 3:
            unit1 += local
        if direction2 == 3:
            unit2 += local
        if direction1 == 1:
            unit1 -= local
        if direction2 == 1:
            unit2 -= local
    if i[0] == "W":
        local = int(i[1:])
        if direction1 == 1:
            unit1 += local
        if direction2 == 1:
            unit2 += local
        if direction1 == 3:
            unit1 -= local
        if direction2 == 3:
            unit2 -= local
    if i[0] == "R":
        local = int(i[1:])
        if local == 90:
            direction1 -= 1
            if (direction1 < 1):
                direction1 = direction1 + 4
            direction2 -= 1
            if (direction2 < 1):
                direction2 = direction2 + 4
        if local == 180:
            direction1 -= 2
            if (direction1 < 1):
                direction1 = direction1 + 4
            direction2 -= 2
            if (direction2 < 1):
                direction2 = direction2 + 4
        if local == 270:
            direction1 -= 3
            if (direction1 < 1):
                direction1 = direction1 + 4
            direction2 -= 3
            if (direction2 < 1):
                direction2 = direction2 + 4
    if i[0] == "L":
        local = int(i[1:])
        if local == 90:
            direction1 += 1
            if (direction1 > 4):
                direction1 = direction1 - 4
            direction2 += 1
            if (direction2 > 4):
                direction2 = direction2 - 4
        if local == 180:
            direction1 += 2
            if (direction1 > 4):
                direction1 = direction1 - 4
            direction2 += 2
            if (direction2 > 4):
                direction2 = direction2 - 4
        if local == 270:
            direction1 += 3
            if (direction1 > 4):
                direction1 = direction1 - 4
            direction2 += 3
            if (direction2 > 4):
                direction2 = direction2 - 4
print(abs(x) + abs(y))
