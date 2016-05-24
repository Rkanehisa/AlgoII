#Flawless Nipponese Programing

def main():
    s = input()
    stack = []
    total = 0
    for i in range(0,len(s)):
        if(s[i] == "\\"):
            stack.append(i)
        if(s[i] == "/"):
            if(len(stack) > 0):
                total += (i-stack.pop())
    print(total)

nTimes = input()
for i in range(0,int(nTimes)):
    main()
