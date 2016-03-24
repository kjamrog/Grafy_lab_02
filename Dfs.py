# Algorytm przeszukiwania w głąb

from Graph import Graph

# W - white
# G - grey
# B - black

# klasa reprezentująca graf przeszukany w głąb
class Dfs:
	def __init__(self, graph):
		self.time = 0
		self.vertices = range(len(graph.AL))
		self.al = [ [j for j in i] for i in graph.AL]
		self.color = []
		self.pre = []
		self.d = []
		self.f = []
		for i in self.vertices:
			self.color.append("W")
			self.pre.append(None)
			self.d.append(None)
			self.f.append(None)
		
		for u in self.vertices:
			if self.color[u] == "W":
				self.dfsVisit(u)
			
		del(self.color)
		print(self.pre)
		print(self.d)
		print(self.f)		


	def dfsVisit(self, u):
		self.color[u] = "G"
		self.d[u] = self.time = self.time + 1
		for v in self.al[u]:
			if self.color[v] == "W":
				self.pre[v] = u
				self.dfsVisit(v)
		self.color[u] = "B"
		self.f[u] = self.time = self.time + 1

			


			

