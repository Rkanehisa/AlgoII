#Flawless Nipponese Programing

def printOutput(nCase,nHigh,nLow):
    print("Case %d: %d %d" % (nCase,nHigh,nLow))
pass

def getAltura():
    tmp = input()
    tmp = tmp.split(" ")
    tmp = [int(i) for i in tmp]
    return tmp
pass

def getResult(towers):
    low = 0
    high = 0
    for i in range(0,len(towers)-1):
        if(towers[i] > towers[i+1]):
            low += 1
        if(towers[i] < towers[i+1]):
            high += 1
    return high,low
pass

def main():
    nCases = int(input())
    for i in range(0,nCases):
        ntowers = input()
        towers = getAltura()
        nHigh,nLow = getResult(towers)
        printOutput(i+1,nHigh,nLow)
    pass
pass


main()
