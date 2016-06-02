from math import factorial

def perm_with_repetition(string):
	rep = dict()	# stores (value:number of reps)
	for i in string:
		rep[i] = rep.get(i,0) + 1
	denom = 1
	for i in rep:
		denom *= factorial(rep[i])
	return factorial(len(string))//denom	# n!/prod(k_i!)

def rec_(string, num):
	if len(string) == 1:	# it's time to stop this madness!
		return num + 1
	less = dict()			# stores chars less than string[0]
	pos = 0
	for i in string:
		if ord(i) < ord(string[0]) and i not in less:
			less[i] = pos
		pos += 1
	total = num
	for i in less:
		total += perm_with_repetition(string[:less[i]]+string[less[i]+1:])
	return rec_(string[1:], total)	# removes first char and continues

def main():
	while True:
		inp = input()
		if inp == '#':
			break
		print('%10d' % rec_(inp,0))
	exit(0)
main()