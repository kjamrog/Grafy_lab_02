#!/usr/bin/env python3.4

# Główny skrypt wykonujący kolejne operacje na grafie

from sys import argv
from Graph import isGraphical
from Graph import Graph
from Graph import kregular
from Dfs import Dfs
from Euler import eulerianCycle

			
# przygotowanie ciągu		
seq = [int(i) for i in argv[1:]]
flag = isGraphical(seq)
if ( flag == False ):
	exit("Ciąg nie jest graficzny!")


graph = Graph(seq)
graph.showAM()
#print(graph.rand())
print(graph.AL)
print()
graphDfsInfo = Dfs(graph)
#print(graph.isEulerian())
#eulerp = eulerianPath(graph)
print(graph.isHamiltonian())
kgraph=kregular()
kgraph.showAM()

		
