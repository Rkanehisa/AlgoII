import sys

while True:
    inputStr = sys.stdin.readline()
    if inputStr == '':
        break
    inputStr = inputStr.strip("\n")
    jogada = inputStr.split(" ")
    if((jogada[0] == jogada[1]) and (jogada[1] == jogada[2])):
       print("*")
    if((jogada[0] != jogada[1]) and (jogada[0] != jogada[2]) and (jogada[1] == jogada[2])):
        print("A")
    if((jogada[1] != jogada[0]) and (jogada[1] != jogada[2]) and (jogada[0] == jogada[2])):
        print("B")
    if((jogada[2] != jogada[1]) and (jogada[0] != jogada[2]) and (jogada[0] == jogada[1])):
        print("C")
pass
