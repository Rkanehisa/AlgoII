from queue import Queue

class Edge():
	def __init__(self, src, target, weigth = 1):
		self.edge = (src, target)
		self.weigth = weigth

	def __getitem__(self, key):
		return self.edge[key]

class Graph(dict):
	def __init__(self, isDirected=False):
		self.isDirected = isDirected
		self.Edges = set()

	def addVertex(self, vertex):
		if vertex not in self:
			self[vertex] = dict()

	def addEdge(self, u, v, w=1):
		e = Edge(u, v, w)
		if e not in self.Edges:
			self.addVertex(u)
			self.addVertex(v)
			if not self.isDirected:
				if u not in self[v]:
					self[v][u] = e.weigth
					e_ = Edge(v, u, w)
					self.Edges.add(e_)
			if v not in self[u]:
				self[u][v] = e.weigth
				self.Edges.add(e)

def bfs(G, start, end):
	visited = dict()
	for g in G:
		if g != start:
			visited[g] = ["White", -1, None]
	visited[start] = ["Gray", 0, None]
	Q = Queue(len(G))
	Q.put(start)
	while not Q.empty():
		u = Q.get()
		for v in G[u]:
			if v == end:
				return visited[u][1] + 1
			if visited[v][0] == "White":
				visited[v][0] = "Gray"
				visited[v][1] = visited[u][1] + G[u][v]
				visited[v][2] = u
				Q.put(v)
		visited[u][0] = "Black"
	return None

def makeGraph(M, L, R, C):
	G = Graph()
	start, end = None, None
	toVertex = lambda i,j,k : i*(R*C) + j*C + k
	for i in range(L):
		for j in range(R):
			for k in range(C):
				v = toVertex(i,j,k)
				if M[i][j][k] != "#":
					if M[i][j][k] == "S":
						start = v
						G.addVertex(v)
					if M[i][j][k] == ".":
						G.addVertex(v)
					if M[i][j][k] == "E":
						end = v
						G.addVertex(v)
					if i + 1 < L and M[i+1][j][k] != "#":
						u = toVertex(i+1,j,k)
						G.addVertex(u)
						G.addEdge(v, u, 1)
					if j + 1 < R and M[i][j+1][k] != "#":
						u = toVertex(i,j+1,k)
						G.addVertex(u)
						G.addEdge(v, u, 1)
					if k + 1 < C and M[i][j][k+1] != "#":
						u = toVertex(i,j,k+1)
						G.addVertex(u)
						G.addEdge(v, u, 1)
	return G, start, end

def main():
	while True:
		L, R, C = list(map(int, input().split()))
		if L == 0 and R == 0 and C == 0:
			break

		M = []
		for i in range(L):
			M.append([input() for x in range(R)])
			nl = input()
		G, start, end = makeGraph(M, L, R, C)
		result = lambda x: print("Trapped!") if x is None else print("Escaped in %d minute(s)." % x)
		result(bfs(G, start, end))
main()