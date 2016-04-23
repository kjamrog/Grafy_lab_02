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
0. Exit
'''
			
# przygotowanie ciągu		
seq = [int(i) for i in argv[1:]]

if isGraphical(seq) == False:
	exit("Ciąg nie jest graficzny!")



graph = Graph(seq)
graphDfsInfo = Dfs(graph)
#graphDfsInfo.show()
#print(graph.isEulerian())
#eulerp = eulerianPath(graph)
#print(graph.isHamiltonian())
#kgraph=kregular()
#kgraph.showAM()
#graph.draw()
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
			graph.rand()
'''

graph.showAM()

graph.rand()
graph.showAM()
graph.draw()

		
