#Flawless Nipponese Programing

def main():
    extraPoint = 0
    count = 0
    string = input()
    for i in string:
        if (i == "O"):
            count += 1+extraPoint
            extraPoint += 1
        else:
            extraPoint = 0
    print(count)
pass

nTimes = input()
for i in range(0,int(nTimes)):
    main()
