# -*- coding: utf-8 -*-


import networkx as nx
import matplotlib.pyplot as plt

from random import randrange
from BaseGraph import BaseGraph
from BaseGraph import isGraphical


# funkcja tworząca i zwracająca losowy graf k-regularny
def kregular():
	f=False
	while f==False:	
		k=randrange(1,10)
		il=randrange(1,10)
		seq=[int(k) for i in range(il)]
		if isGraphical(seq):
			f=True	
	g=Graph(seq)
	g.rand()
	return g

 
	
# klasa Graph, tworzona na podstawie ciągu graficznego	
class Graph(BaseGraph):
	def __init__(self, seq):
		BaseGraph.__init__(self, seq)
		
	def draw(self):
		g = nx.Graph()
		nr = 0
		for i in range(len(self.AL)):
		    g.add_node(i)
		    for j in self.AL[i]:
		        if j > i:
		            g.add_edge(i, j)
		            nr += 1

		
		pos = nx.shell_layout(g)
		nx.draw_networkx_nodes(g, pos, node_size=300)
		nx.draw_networkx_edges(g, pos)
		nx.draw_networkx_labels(g, pos)

		plt.axis('off')
		plt.savefig("temp.png")
		plt.clf()


	def isEulerian(self):
		for i in self.seq:
			if i%2 != 0:
				return False
		return True


	def isHamiltonian(self):
		al=self.AL
		length=len(al)
		n=1
		s={}
		for i in range(length):	
			for i in range(length):
				s[i]=False
			cur=i
			s[cur]=True
			l=[]
			l.append(cur)
			while len(l)<length:
				j=0
				while s[al[cur][j]]==True:
					j=j+1
					if j==len(al[cur]):
						break	
				if j<len(al[cur]):
					cur=al[cur][j]
					s[cur]=True
					l.append(cur)
					n=n+1
					if len(l)==length:
						return True
				else: 
					l.remove(l[len(l)-1])
					if len(l)!=0:
						cur=l[len(l)-1]
					else:
						break
		return False
