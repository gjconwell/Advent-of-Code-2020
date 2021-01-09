with open("Day_1_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

inputData = list(map(int, inputData)) #map adds int to every element of inputData, list() turns map into a list

for i in inputData:
    for j in inputData:
        if (2020 - i == j):
            print(i * j)
            exit() #stops program immediately
