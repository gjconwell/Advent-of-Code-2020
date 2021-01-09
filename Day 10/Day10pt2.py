with open("Day_10_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

inputData = list(map(int, inputData)) #map adds int to every element of inputData, list() turns map into a list

index = 1 #the current line being run
diff = 0
prevdiff = 0
distict = 0
distictlist = []
inputData.sort()

while (len(inputData) != index): #stops index when it reaches the last row
    num = inputData[index] #detects the value on the index line
    prevnum = inputData[index - 1]
    diff = num - prevnum
    distictlist.append(diff)
    print( prevnum, num)
    prevdiff = diff
    index += 1
# distictlist.append(3)
print(inputData)
print(distictlist)
