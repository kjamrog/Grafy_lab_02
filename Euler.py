#!/usr/bin/env python3.4

from Graph import Graph

def eulerianPath(graph):
	# przy zmianie na numercję wierzchołków od 0 zmienić z j-1 na j
	al = [ [j-1 for j in i] for i in graph.AL]
	print(al)
	stack = []
	i = 0
	stack.append(i)
	while al:
		j = al[i][0]
		stack.append(j)
		al[i].remove(j)
		al[j].remove(i)
		i = j
		
	for i in range(len(stack)):
		print(stack[len(stack)-i], "->")

		

