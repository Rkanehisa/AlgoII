#Flawless Nipponese Programing

def testaDiagonal(casas):
    return (abs(int(casas[0]) - int(casas[2])) == abs(int(casas[1]) - int(casas[3])))
pass

def main():
    inputString = input()
    while(inputString != "0 0 0 0"):
        inputString = inputString.strip("\n")
        casas = inputString.split(" ")
        if((casas[0] == casas[2]) and (casas[1] == casas[3])):
           print("0")
        elif((casas[0] == casas[2]) or (casas[1] == casas[3]) or testaDiagonal(casas)):
            print("1")
        else:
            print("2")
        inputString = input()
    pass
pass

main()
