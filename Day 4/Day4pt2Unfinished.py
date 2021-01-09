with open("Day_4_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

total = 0
valid = 0
for i in inputData:
    if (len(i.strip()) == 0):
        valid = 0
    if ("hcl:" in i):
        local = i.find("hcl:")
        chars = i[local + 4:local + 11]
        valid2 = 0
        if "#" in chars:
            for j in chars[1:]:
                if ("0" <= j <= "9") or ("a" <= j <= "f"):
                    valid2 += 1
        if (valid2 == 6):
            valid += 1 # 183 are valid
    if ("ecl:" in i):
        local = i.find("ecl:")
        chars = i[local + 4:local + 7]
        if (chars == "amb" or (chars == "blu" or (chars == "brn" or (chars == "gry" or (chars == "grn" or (chars == "hzl" or chars == "oth")))))):
            valid += 1 # 169 correct
    if ("hgt:" in i):
        local = i.find("hgt:")
        if (i[local + 7:local + 9] == "cm"):
            chars = int(i[local + 4:local + 7])
            if (150 <= chars <= 193):
                valid += 1
        if (i[local + 6:local + 8] == "in"):
            chars = int(i[local + 4:local + 6])
            if (59 <= chars <= 76):
                valid += 1
                # 163 correct
    if ("byr:" in i):
        local = i.find("byr:")
        chars = int(i[local + 4:local + 8])
        if (1920 <= chars <= 2002):
            valid +=1
            # 158 correct
    if ("pid:" in i):
        local = i.find("pid:")
        chars = i[local + 4:local + 13]
        valid2 = 0
        for k in chars:
            if ("0" <= k <= "9"):
                valid2 += 1
            if (valid2 == 9):
                valid +=1
            # 155 correct
    if ("iyr:" in i):
        local = i.find("iyr:")
        chars = int(i[local + 4:local + 8])
        if (2010 <= chars <= 2020):
            valid +=1
            # 153 correct
    if ("eyr:" in i):
        local = i.find("eyr:")
        chars = int(i[local + 4:local + 8])
        if (2020 <= chars <= 2030):
            valid +=1
            # 151 correct
    if (valid == 7):
        total += 1
        valid = 0
print(total)
