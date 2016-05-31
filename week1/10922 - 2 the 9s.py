#Flawless Nipponese Programing

def soma(n,m):
	s = 0
	if(int(n) %9  == 0 and int(n) != 0):
		for i in n:
			s += int(i)
		if(s == 9):
			return m+1
		else:
			return soma(str(s),m+1)
	else:
		return -1

def printOut(n,m):
	if(m == -1):
		print("%s is not a multiple of 9." % (n))
	else:
		print("%s is a multiple of 9 and has 9-degree %d." % (n,m))

def main():
	entrada = input()
	while(entrada != '0'):
		printOut(entrada,soma(entrada,0))
		entrada = input()

main()