with open("Day_13_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]


local = 0
diff = 100
buslist = []
target = int(inputData[0])
ids = inputData[1].split(",")
for i in range(ids.count("x")):
    ids.remove("x")

while local != len(ids):
    bus = int(ids[local])
    time = 0
    while time < target + bus:
        time += bus
        testdiff = time - target
        if testdiff > -1:
            if diff > testdiff:
                diff = testdiff
                buslist.append(bus)
            print(buslist)
    local += 1
print(buslist[-1]*diff)
