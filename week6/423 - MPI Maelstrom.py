from math import inf

n = int(input())

graph = {(x,y):0 for x in range(n) for y in range(n)}

M = [input().split() for x in range(n-1)]
p = 1
for i in range(n-1):
	for j in range(p):
		inp = M[i][j]
		val = int(inp) if inp != "x" else inf
		graph[i+1, j] = val
		graph[j, i+1] = val
	p += 1

for i in range(n):
	for j in range(n):
		for k in range(n):
			graph[j, k] = min(graph[j,k], graph[i,k] + graph[j,i])

result = 0
for i in range(n):
	result = max(result, graph[0, i])
print(result)