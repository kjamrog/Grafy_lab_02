#!/usr/bin/env python3.4

from sys import argv
from random import randint
from random import randrange

# sprawdzanie czy ciąg jest graficzny
def isGraphical(seq):
	length = len(seq)
	while True:
		seq.sort(reverse=True)
		x = seq[0]
		if x>=length:
			return False
		seq = seq[1:]
		seq = [seq[i]-1 if i < x else seq[i] for i in range(len(seq))]
		if not [i for i in seq if i !=0]:
			return True
		if seq[0] < 0:
			return False
	
# klasa graf, tworzona na podstawie ciągu graficznego	
class Graph:
	# konstrukcja grafu
	def __init__(self, seq):
		seq = [i for i in seq]
		self.adjacencyList = []
		length = len(seq)
		self.adjacencyList = [[0 for i in range(length)] for vertices in seq]
		for vertice in range(length):
			i=1
			while seq[0] > 0:
				print(seq)
				next = vertice + i
				self.adjacencyList[vertice][next] = self.adjacencyList[next][vertice] = 1
				seq[0] -= 1	
				seq[i] -= 1
				i+=1
			seq.sort(reverse=True)
	

			
	# wyświetlanie grafu				
	def show(self):
		x = 0
		for i in self.adjacencyList:
			print( [j for j in i])
	
	
	#zamiana krawędzi - randomizacja grafu nie działa!		
	'''def rand(self):
		from random import randint
		length = len(self.adjacencyList) - 1
		print(length)
			
		a, b, c, d = 0, 0, 0, 0	
			
		while True:
			a, b, c, d = randint(0, length), randint(0, length), randint(0, length), 0
			while self.adjacencyList[a][b] == 0 or a == b:
				b = randint(0, length)
				if b > length: 
					a=randint(0, length)
					b=0
		
			while c == a or c == b:
				c = randint(0, length)
				
			while self.adjacencyList[c][d] == 0 or d == c or d == a or d == b:
				d+=1
				if d > length:
					break
			else:
				break
			
		
		self.adjacencyList[a][b] = self.adjacencyList[b][a] = self.adjacencyList[c][d] = self.adjacencyList[d][c] = 0
		self.adjacencyList[a][d] = self.adjacencyList[d][a] = self.adjacencyList[c][b] = self.adjacencyList[b][c] = 1'''

	def toList(self):
		length = len(self.adjacencyList)
		l=[[] for i in range(length)]
		for i in range(length):
			for j in range(length):
				if self.adjacencyList[i][j] == 1 :
					l[i].append(j+1)
		return l


	def countEdges(self):
		n=0
		for i in range(len(self.adjacencyList)):
			for j in range(len(self.adjacencyList[i])):
				if self.adjacencyList[i][j]==1 and j>i:
					n=n+1
		return n

	def toIM(self, li):
		edges=self.countEdges()		
		vertices=len(li)
		im=[[0 for i in range(vertices)] for j in range(edges)]
		n=0
		for i in range(len(li)):
			for j in li[i]:
				if j>i:
					im[n][i]=im[n][j-1]=1
					n=n+1
					
		return im			
					
					
		


	'''def rand(self):
		im=self.toIM(self.toList())
		edges=self.countEdges()
		vertices=len(im[0])
		control=3*edges;
		flag=True
		c=0
		l=0
		while l<3:
			if c>control:
				print(c)
				return None
			a=randint(0,edges-1)
			b=randint(0,edges-1)
			print(a,b)
			if b==a:
				c=c+1
				continue
			else:
				for i in range(vertices):
					if im[a][i]==im[b][i]:
						flag=False
						c=c+1
				if flag==True:
					for ai in range(vertices):
						if im[a][ai]==1:
							for bi in range(vertices):
								if im[b][bi]==1:
									im[a][ai]=im[b][bi]=0
									im[a][bi]=im[b][ai]=1
									l=l+1
									flag=True
									break
							break
		return im'''

	def rand(self):
		im=self.toIM(self.toList())
		edges=self.countEdges()
		edgesList=[[] for i in range(edges)]
		for i in range(len(im)):
			for j in range(len(im[i])):
				if im[i][j]==1:
					edgesList[i].append(j)
		print(edgesList)			
	
		l=0
		s=0
		while l<4:
			a=randrange(0,edges)
			b=randrange(0,edges)
			print(a,b)
			if a!=b:
				if (edgesList[a][0] not in edgesList[b]) and (edgesList[a][1] not in edgesList[b]):
					if [edgesList[a][0],edgesList[b][1]] not in edgesList and [edgesList[b][0],edgesList[a][1]] not in edgesList:					
						edgesList[a][1],edgesList[b][1]=edgesList[b][1],edgesList[a][1]
						l=l+1
			s=s+1
			if s>20:
				break

		return edgesList
			

	


# przygotowanie ciągu		
seq = [int(i) for i in argv[1:]]
flag = isGraphical(seq)
print( flag )
if flag:
	graph = Graph(seq)
	print("\n\n")
	graph.show()

	#print(len(graph.adjacencyList))
	# randomizacja grafu
	#graph.rand()
	# porównanie po dokonanej randomizacji
	#graph.show()

	#print(graph.countEdges())



	#print(graph.toIM(graph.toList()))

#	print(graph.rand())
	




		
