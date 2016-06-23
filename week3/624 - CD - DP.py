def knapsack(W, n, weigths):
	Matrix = [[0 for w in range(W+1)] for x in range(n+1)]
	for i in range(n+1):
		for j in range(W+1):
			if i == 0 or j == 0:
				Matrix[i][j] = 0
			elif weigths[i-1] <= j:
				Matrix[i][j] = max(weigths[i-1] + Matrix[i-1][j - weigths[i-1]], Matrix[i-1][j])
			else:
				Matrix[i][j] = Matrix[i-1][j]

	path = []
	sub = 0
	for line in range(n):
		if Matrix[n - line][W - sub] != Matrix[n-line-1][W - sub]:
			path = [weigths[n-line-1]] + path
			sub += weigths[n-line-1]
	return Matrix[n][W], path

def main():
	while True:
		try:
			inp = list(map(int, input().split()))
		except EOFError:
			break
		W, n, tracks = inp[0], inp[1], inp[2:]
		solution = knapsack(W, n, tracks)
		#print(solution)#print("\n".join(str(x) for x in solution))
		print(" ".join(str(x) for x in solution[1]) + " sum:" + str(solution[0]))
main()