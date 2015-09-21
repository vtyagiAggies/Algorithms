#!/usr/bin/python
import sys
from Graph import Graph	
from Nodes import Node			

if __name__ == "__main__":
	filepath = sys.argv[1]
	search_algo = sys.argv[2]
	source_x = int(sys.argv[3])
	source_y =int(sys.argv[4])
	destination_x =int(sys.argv[5])
	destination_y = int(sys.argv[6]) 

	print destination_x
	print destination_y
    	#Intializing graph
	graph = Graph(filepath)
	for vertex in graph.verticies:
		if(vertex.X == source_x and vertex.Y == source_y):
			initial_state = Node(vertex.ID)
		if(vertex.X == destination_x and vertex.Y == destination_y):
			goal = Node(vertex.ID)
	if not goal:#todo
		print "destination doesn't exist"

	#Calling search algorithm according to user input
	if(search_algo == "BFS"):
		traceback, vertices_visited, iterations, max  = graph.BFS_Search(initial_state, goal)
	elif(search_algo == "DFS"):
		traceback, vertices_visited, iterations, max  = graph.DFS_Search(initial_state, goal)
	elif search_algo == "GBFS":
		traceback, vertices_visited, iterations, max  = graph.GBFS_Search(initial_state, goal)
	elif search_algo == "ASTAR":
		traceback, vertices_visited, iterations, max  = graph.ASTAR_Search(initial_state, goal)


	#Printing result
	for x in traceback:
		print "%d %d"%(graph.verticies[x].X, graph.verticies[x].Y)
	print "Search algorithm  = ", search_algo
	print "Total iterations  = %d"%(iterations)
	print "Max frontier size = %d"%(max)
	print "Vertices visited  = %d/275"%(vertices_visited)
	print "Path length       = %d"%(len(traceback)-1)
	
  
	
