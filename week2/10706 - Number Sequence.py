from math import floor, log10

def digits(n):
	return floor(log10(n)) + 1

def genAllSeqsLen(maxRow):
	Seq = dict()
	Seq[1] = 1
	for i in range(2, maxRow + 1):
		Seq[i] = Seq[i-1] + digits(i)
	return Seq

def genAllSeqsSum(maxRow, d):
	Seq = dict()
	Seq[1] = 1
	for i in range(2, maxRow + 1):
		Seq[i] = Seq[i-1] + d[i]
	return Seq

def main():
	#maxR = 46340
	maxR = 31268
	Seq_Ln = genAllSeqsLen(maxR)
	Seq = genAllSeqsSum(maxR, Seq_Ln)
	inp = int(input())
	for i in range(inp):
		n = int(input())
		m = 1
		while Seq[m] < n:
			m += 1
		count = n - Seq[m - 1] if n > 1 else 1
		string = "".join(str(x) for x in range(1,m+1))
		print(string[count - 1])
main()
