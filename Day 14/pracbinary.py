x = 0
test = 0
while test < value:
    test = 2**x
    x += 1
    
def countbinary(x, test, value):
    printout = ""
    printout = printout + "1"
    n = 2
    test = value - (2**(x - n))
    if value == 0:
        printout = '0'
    else:
        while test >= 1:
            n += 1
            if 2**(x - n) > test:
                printout = printout + "0"
            else:
                printout = printout + "1"
                test = test - (2**(x - n))
    return printout
