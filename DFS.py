# Algorytm przeszukiwania w głąb

from Graph import Graph

# W - white
# G - grey
# B - black

# singleton do przechowywania informacji o wierzchołkach
class Dfs:
	pass

def dfs(graph):
	# inicjalizacja singletonu Dfs
	Dfs.time = 0
	Dfs.vertices = range(len(graph.AL))
	Dfs.al = [ [j-1 for j in i] for i in graph.AL]
	Dfs.color = []
	Dfs.pre = []
	Dfs.d = []
	Dfs.f = []
	for i in Dfs.vertices:
		Dfs.color.append("W")
		Dfs.pre.append(None)
		Dfs.d.append(None)
		Dfs.f.append(None)
		
	for u in Dfs.vertices:
		if Dfs.color[u] == "W":
			dfsVisit(u)
			
	print(Dfs.color)
	print(Dfs.pre)
	print(Dfs.d)
	print(Dfs.f)
			
def dfsVisit(u):
	Dfs.color[u] = "G"
	Dfs.d[u] = Dfs.time = Dfs.time + 1
	for v in Dfs.al[u]:
		if Dfs.color[v] == "W":
			Dfs.pre[v] = u
			dfsVisit(v)
	Dfs.color[u] = "B"
	Dfs.f[u] = Dfs.time = Dfs.time + 1

			

