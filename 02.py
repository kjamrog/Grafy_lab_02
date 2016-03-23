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
		seq.sort(reverse=True)
		self.seq = (i for i in seq)
		#tworzenie kolejnych reprezentacji grafu, KOLEJNOŚĆ WYWOŁANIA WAŻNA !!!
		self.AM = self.makeAM()
		self.AL = self.makeAL()
		self.IM = self.makeIM()
		
				
	# wyświetlanie grafu				
	def showAM(self):
		for i in self.AM:
			print( [j for j in i])
	
	#tworzy macierz sąsiedztwa na podstawie ciągu graficznego
	def makeAM(self):
		seq = [i for i in self.seq]
		print(seq)
		length = len(seq)
		AM = []
		AM = [[0 for i in range(length)] for vertices in seq]
		for vertice in range(length):
			next = vertice + 1
			while seq[vertice] > 0:
				while seq[next]==0:
					next+=1
				AM[vertice][next] = AM[next][vertice] = 1
				seq[vertice] -= 1	
				seq[next] -= 1
				next += 1
		return AM
		
	#tworzt listę sąsiedztwa
	def makeAL(self):
		length = len(self.AM)
		l=[[] for i in range(length)]
		for i in range(length):
			for j in range(length):
				if self.AM[i][j] == 1 :
					l[i].append(j+1)
		return l


	def countEdges(self):
		n=0
		for i in range(len(self.AM)):
			for j in range(len(self.AM[i])):
				if self.AM[i][j]==1 and j>i:
					n=n+1
		return n

	def makeIM(self):
		edges=self.countEdges()		
		vertices=len(self.AL)
		im=[[0 for i in range(vertices)] for j in range(edges)]
		n=0
		for i in range(len(self.AL)):
			for j in self.AL[i]:
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
		edges=self.countEdges()
		edgesList=[[] for i in range(edges)]
		for i in range(len(self.IM)):
			for j in range(len(self.IM[i])):
				if self.IM[i][j]==1:
					edgesList[i].append(j)
		print(edgesList)			
	
		l=0
		s=0
		while l<1:
			a=randrange(0,edges)
			b=randrange(0,edges)
			print(a,b)
			if a!=b:
				if (edgesList[a][0] not in edgesList[b]) and (edgesList[a][1] not in edgesList[b]):
					if [edgesList[a][0],edgesList[b][1]] not in edgesList and [edgesList[b][0],edgesList[a][1]] not in edgesList:					
						edgesList[a][1],edgesList[b][1]=edgesList[b][1],edgesList[a][1]
						l=l+1
			s=s+1
			'''if s>20:
				break'''

		return edgesList
			

	


# przygotowanie ciągu		
seq = [int(i) for i in argv[1:]]
flag = isGraphical(seq)
print( flag )
if flag:
	graph = Graph(seq)
	graph.showAM()
	print(graph.rand())





		
