#!/usr/bin/env python3.4

from Graph import Graph
	
def eulerianCycle(graph):
	al = [ [j for j in i] for i in graph.AL]
	stack = []
	cycle = []
	v = 0
	stack.append(v)
	while stack:
		v = stack.pop()
		cycle.append(v)
		print(cycle)
		while al[v]:
			w = al[v][0]
			stack.append(v)
			al[v].remove(w)
			al[w].remove(v)
			v=w	
	return cycle
