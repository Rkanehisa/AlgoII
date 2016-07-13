def lcs(s1, s2):
	# Longest Common Subsequence
	lengths = dict()
	for i, c1 in enumerate(s1):
		for j, c2 in enumerate(s2):
			if c1 == c2:
				lengths[i+1, j+1] = lengths.get((i,j), 0) + 1
			else:
				lengths[i+1, j+1] = max(lengths.get((i+1,j), 0), lengths.get((i,j+1), 0))

	result = []
	x, y = len(s1), len(s2)
	while x != 0 and y != 0:
		if lengths.get((x,y), 0) == lengths.get((x-1,y), 0):
			x -= 1
		elif lengths[x, y] == lengths.get((x,y-1), 0):
			y -= 1
		else:
			result = [s1[x-1]] + result
			x -= 1
			y -= 1
	return result

def main():
    inp = input().split()
    i = 1
    while inp[0] != '0' and inp[1] != '0':
        tower1 = input().split()
        tower2 = input().split()
        L = lcs(tower1, tower2)
        print("Twin Towers #%d\nNumber of Tiles : %d\n" %(i, len(L)))
        i += 1
        inp = input().split()
main()