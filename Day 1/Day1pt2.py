with open("Day_1_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

inputData = list(map(int, inputData)) #map adds int to every element of inputData, list() turns map into a list

# print(inputData)

for i in inputData:
    for j in inputData:
        for k in inputData:
            if (i + j + k  == 2020):
                print(i * j * k)
                exit() #stops program immediately
