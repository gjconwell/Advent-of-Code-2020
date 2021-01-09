with open("Day_4_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

total = 0
valid = 0
for i in inputData:
    if (len(i.strip()) == 0):
        valid = 0
    if ("hcl:" in i):
        valid += 1
    if ("ecl:" in i):
        valid += 1
    if ("hgt:" in i):
        valid += 1
    if ("byr:" in i):
        valid += 1
    if ("pid:" in i):
        valid += 1
    if ("iyr:" in i):
        valid += 1
    if ("eyr:" in i):
        valid += 1
    if ("cid:" in i):
        pass
    if (valid == 7):
        total += 1
        valid = 0
print(total)
