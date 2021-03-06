# punkcja zachowujaca sie jak print w python3.x
from __future__ import print_function

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
		while al[v]:
			w = al[v][0]
			stack.append(v)
			al[v].remove(w)
			al[w].remove(v)
			v=w	
	for i in range(0, len(cycle)):
		if i==len(cycle)-1:
			print(cycle[i])
		else:
			print(cycle[i], end=" -> ")
	return cycle
