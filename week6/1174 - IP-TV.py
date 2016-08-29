parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(vertices,edgesList):
    for vertice in vertices:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(edgesList)
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

def main():
        T = int(input())
        _ = input()
        for vezes in range(T):
                M = int(input())
                N = int(input())
                cities = []
                edges = set()
                for i in range(N):
                        tmp = input().split()
                        if((tmp[0] in cities) == False):
                                cities.append(tmp[0])
                        if((tmp[1] in cities) == False):
                                cities.append(tmp[1])
                        edges.add((int(tmp[2]),tmp[0],tmp[1]))
                acc = 0
                for i in kruskal(cities,edges):
                        acc+=i[0]
                print("%d" %(acc))
                
                try:
                        _ = input()
                        print()
                except EOFError:
                        break
main()
