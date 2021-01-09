with open("Day_10_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

inputData = list(map(int, inputData)) #map adds int to every element of inputData, list() turns map into a list

index = 0 #the current line being run
prevnum = 0 #track the number on the line before index
jolt1 = 0 #counts total amount of 1 jolt differences
jolt3 = 0 #counts total amount of 3 jolt differences
inputData.sort()

while (len(inputData) != index): #stops index when it reaches the last row
    num = inputData[index] #detects the value on the index line
    if (num - prevnum == 1):
        jolt1 += 1
    if(num - prevnum == 3):
        jolt3 += 1
    prevnum = num
    index += 1
jolt3 += 1 #accounts for extra 3 jort differece at the end

print(jolt1 * jolt3)
