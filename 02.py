#!/usr/bin/env python3.4

# Główny skrypt wykonujący kolejne operacje na grafie

from sys import argv
from Graph import isGraphical
from Graph import Graph
from DFS import dfs

			
# przygotowanie ciągu		
seq = [int(i) for i in argv[1:]]
flag = isGraphical(seq)
print( flag )
if flag:
	graph = Graph(seq)
	graph.showAM()
	print(graph.rand())
	print(graph.AL)
	dfs(graph)




		
