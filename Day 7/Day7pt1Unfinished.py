with open("Day_7_Input.txt") as input:
    inputData = input.read().split("\n")[:-1]

goldbag = []
baglevelist = []
baglevel = "shiny gold"
bigbag = "shiny gold"

def baglayer(bigbag):
    multi = 0
    space = ""
    for j in inputData:
        local = j.find(baglevel)
        localbag = j.find("bag", local)
        if local > 0:
            multi += 1
            space += " "
            chars = j[local:localbag - 1]
            baglevelist.append(baglevel)
# local = j.find("s contain")
# bigbag = j[:local]
            print(local, baglevel)
    if (multi == 0):
        space += " "
        return exit()
    print(baglevelist)
    return exit()

for i in inputData:
    baglayer(bigbag)

    print(baglevel)
print(len(goldbag))

#just practicing for git x2
