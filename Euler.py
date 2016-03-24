#!/usr/bin/env python3.4

from Graph import Graph

def eulerianPath(graph):
	al = [ [j for j in i] for i in graph.AL]
	print(al)
	stack = []
	i = 0
	stack.append(i)
	while al[0]:
		j = al[i][0]
		stack.append(j)
		al[i].remove(j)
		al[j].remove(i)
		i = j
		
	print(stack)

		

