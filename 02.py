#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Główny skrypt wykonujący kolejne operacje na grafie

from os import system
from sys import argv
from random import randint
from Graph import isGraphical
from Graph import Graph
from Graph import kregular
from Dfs import Dfs
from Euler import eulerianCycle

def menu():
	print '''
1. Macierz sąsiedztwa
2. Lista sąsiedztwa
3. Macierz incydencji
4. Rysuj graf
5. Radnomizacja grafu
6. Przeszukiwanie grafu w głąb
7. Cykl Eulera
8. Cykl Hamiltona
0. Exit
'''
			
# przygotowanie ciągu		
seq = [int(i) for i in argv[1:]]

if isGraphical(seq) == False:
	exit("Ciąg nie jest graficzny!")


graph = Graph(seq)
'''
kgraph=kregular()
kgraph.showAM()
graph.draw()
'''

flag = None
while True:
	menu()
	flag = input(">>> ")
	if flag==0:
		break
	elif flag==1:
		graph.showAM()
	elif flag==2:
		graph.showAL()
	elif flag==3:
		graph.showIM()
	elif flag==4:
		graph.draw()
	elif flag==5:
		for i in range(randint(5, 10)):
			if not graph.rand():
				print("Grafu nie można randomizować!")
				break
	elif flag==6:
		dfs = Dfs(graph)
		dfs.show()
	elif flag==7:
		if graph.isEulerian():
			eulerianCycle(graph)
		else:
			print "Graf nie posiada cyku Eulera!"
	elif flag==8:
		if graph.isHamiltonian():
			print "Graf jest hamiltonowski"

		
