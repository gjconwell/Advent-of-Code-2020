inputData = []
# Opens the input file
with open("Day_1_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

var1 = "string" #string
var2 = 'string' #string
var3 = [1, 2, 3] #list
var4 = 12 #int
var5 = 3.14 #float
var6 = {"key": "value"} #dict
var7 = {"key": [1, 3, 4]}
var8 = [1, 2, [3, 4]] #list inside a list

# print(int("1234"))

print(int("1234"))

counter = 0

counter += 1 #change counter by 1
counter -= 1 #change counter by -1
counter *= 1 #change counter by multiplying it by 1

someNum = 3

if ((someNum > 1 and someNum < 4) or someNum == 3): # basic if statement
    pass

# wait until someNum < 0

while (someNum > 0): #repeat until false
    print("yes")
    someNum -= 1

for _ in range(10): #repeat i == a number and range is 0 through 9
    pass

var9 = var1 + var4 #joining characters

var3.append(4) #adding to a list

var3[0] = 5 #selecting an item in a list and changing it

var8[2][0] #selecting an item in a list inside a list

list = [1, 2, 3, 4]

list[:2] # everything in front 2 (does not include 2 and 3 and 4)
list[2:] #everything behind 4 (does not include 1 and 2)

print(num1)

class Cat(name):
    def pet():
        print("Petted the cat")

hodge = Cat("Hodge")

print(hodge) # cat object at 0x021391023910237819

hodge.pet()

var1.split("n") #breaks a string based on a character
var1.replace("str", "yes") #find and replace

var10 = "hodge"

var10[1:] #everything besides the first character (ie odge)

var11 = []

var12 = (1, 2) #a fixed list, cannot be changed
var12[0] #selcets first item of the list

# 3! 3 * 2 * 1

# factorial(3) returns 6

def countFactorial(num):
    count = num
    num *= count
    count -= 1
    return num

def recursiveFactorial(num):

    if (num == 1 or num == 0) {
        return 1
    }

    return num * recursiveFactorial(num - 1)

numbers = [1, 2, 3, 4]

isinstance(numbers, list) # return true

# recurFact(3)
