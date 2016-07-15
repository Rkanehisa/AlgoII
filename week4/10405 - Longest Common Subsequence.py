def lcs(s1, s2):
	# Longest Common Subsequence
	lengths = dict()
	get = lengths.get
	for i, c1 in enumerate(s1):
		for j, c2 in enumerate(s2):
			if c1 == c2:
				lengths[i+1, j+1] = get((i,j), 0) + 1
			else:
				lengths[i+1, j+1] = max(get((i+1,j), 0), get((i,j+1), 0))

	result = []
	x, y = len(s1), len(s2)
	while x != 0 and y != 0:
		if get((x,y), 0) == get((x-1,y), 0):
			x -= 1
		elif lengths[x, y] == get((x,y-1), 0):
			y -= 1
		else:
			result = [s1[x-1]] + result
			x -= 1
			y -= 1
	return result

def main():
	while True:
		try:
			s1 = input()
			s2 = input()
		except EOFError:
			break
		L = lcs(s1, s2)
		print(len(L))
main()