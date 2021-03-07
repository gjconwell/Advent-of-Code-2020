with open("Day_12_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

y = 0
x = 0
direction = 3 #North = 4, East = 3, South = 2, West = 1

for i in inputData:
    if i[0] == "F":
        local = int(i[1:])
        if direction == 4:
            y += local
        if direction == 3:
            x += local
        if direction == 2:
            y -= local
        if direction == 1:
            x -= local
    if i[0] == "N":
        local = int(i[1:])
        y += local
    if i[0] == "S":
        local = int(i[1:])
        y -= local
    if i[0] == "E":
        local = int(i[1:])
        x += local
    if i[0] == "W":
        local = int(i[1:])
        x -= local
    if i[0] == "R":
        local = int(i[1:])
        if local == 90:
            direction -= 1
            if (direction < 1):
                direction = direction + 4
        if local == 180:
            direction -= 2
            if (direction < 1):
                direction = direction + 4
        if local == 270:
            direction -= 3
            if (direction < 1):
                direction = direction + 4
    if i[0] == "L":
        local = int(i[1:])
        if local == 90:
            direction += 1
            if (direction > 4):
                direction = direction - 4
        if local == 180:
            direction += 2
            if (direction > 4):
                direction = direction - 4
        if local == 270:
            direction += 3
            if (direction > 4):
                direction = direction - 4
print(abs(x) + abs(y))
