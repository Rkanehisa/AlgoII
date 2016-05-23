#Flawless Nipponese Programing
import re

elementos = {'C': 12.01,'H': 1.008,'O': 16.00,'N':14.01}

def getFormula(string):
    formula = re.findall(r"([A-Z][0-9]*)", string)
    return formula
pass

def calculaMassa(formula):
    massa = 0
    for i in formula:
        if(len(i) == 1):
            massa+=(elementos[i])
        else:
            massa+=(elementos[i[:1]]*float(i[1:]))
    return massa
pass

def main():
    nCases = int(input())
    
    for i in range(0,nCases):
        tmp = input()
        formula = getFormula(tmp)
        print("%.3f" % (calculaMassa(formula)))
        
pass
string = input()
formula = re.findall(r"([A-Z][0-9]*)", string)
print(formula)
#main()
