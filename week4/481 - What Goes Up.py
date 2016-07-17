from math import ceil

def lis(A):
	# nlogn alg. From Wikipedia
	n = len(A)
	P = [0]*n
	M = [0]*(n+1)
	L = 0
	for i in range(n):
		lo = 1
		hi = L
		while lo <= hi:
			mid = ceil((lo+hi)/2)
			if A[M[mid]] < A[i]:
				lo = mid + 1
			else:
				hi = mid - 1
		newL = lo

		P[i] = M[newL - 1]
		M[newL] = i

		if newL > L:
			L = newL
	S = [0]*L
	k = M[L]
	for i in range(L-1,-1, -1):
		S[i] = A[k]
		k = P[k]

	return S

def main():
	L = []
	while True:
		try:
			elm = int(input())
		except:
			break
		L.append(elm)
	M = lis(L)
	print(str(len(M)) + "\n-\n" + "\n".join(str(x) for x in M))
main()	