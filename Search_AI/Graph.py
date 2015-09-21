#!/usr/bin/python
import math
from Nodes import Node
from Nodes import Vertex
from Nodes import Edge

#Class for Graph
class Graph:
    def __init__(self, filepath):
	file = open(filepath)
	lines = [line.rstrip('\n') for line in file.readlines()]
	self.verticies = [None]*275
	self.edges = [None]*641
	self.nodes = []
	#Getting list of all Vertex
	for line in lines[1:276]:
		entities = line.split(' ')
		self.verticies[int(entities[0])] = Vertex(entities[0], entities[1], entities[2])
	
	#Getting list of all Edges
	for line in lines[277:]:
		entities = line.split(' ')
		self.edges[int(entities[0])] = Edge(entities[0], entities[1], entities[2])
	
	#Getting list of all Nodes
	for vertex in self.verticies:
		self.nodes.append(Node(vertex.ID))
		for edge in self.edges: 
			if(vertex.ID == edge.V1):
				self.nodes[vertex.ID].successor.append(edge.V2)
			if(vertex.ID == edge.V2):
				self.nodes[vertex.ID].successor.append(edge.V1)
 
    #Breadth-First-Search
    def BFS_Search(self,initial_state, goal):
	queue = []
	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	print "solution path:"
	queue.append(initial_state.index)
	while queue:
		curr = queue[0]; queue = queue[1:] #equivalent to takine first element from queue
		
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks			
			return self.nodes[curr].tracebacks, v, i, max
			break
		
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == 0 :     #if index not visited
				queue.append(x)
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
		if len(queue) > max:
			max = len(queue)
		i += 1	
	
    #Depth-First-Search
    def DFS_Search(self,initial_state, goal):
	stack = []
 	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	print "solution path:"
	stack.append(initial_state.index)
	while stack:
		curr = stack[-1]; stack = stack[:-1] #equivalent to takine last element from stack
	
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks
			#print "vertex %d (%d,%d)"%(initial_state.index, self.verticies[initial_state.index].X, self.verticies[initial_state.index].Y)
			#for x in self.nodes[curr].tracebacks:
				#print "vertex %d (%d,%d)"%(x, self.verticies[x].X, self.verticies[x].Y)			
			return self.nodes[curr].tracebacks, v, i, max
			break
	
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == 0 :     #if index not visited
				stack.append(x)
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
		if len(stack) > max:
			max = len(stack)
		i += 1


    #Greedy-Best-First-Search
    def GBFS_Search(self,initial_state, goal):
	queue = {}          #queue having heuristic and index value so that index having best heuristic value can be selected
	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	debug = 1
	print "solution path:"
	queue[0] = initial_state.index
	while queue:
		
		best_heur = sorted(queue)[0]
		curr = queue[best_heur]; queue = {key: value for key, value in queue.items() if key != best_heur} #equivalent to taking  best element from queue
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks		
			return self.nodes[curr].tracebacks, v, i, max
			break
		i += 1	
		if debug==1 :
			print "iter=%d, frontier=%d, popped=%d (%d,%d), depth=%d, dist2goal=%f"%(i,len(queue),curr, self.verticies[curr].X, self.verticies[curr].Y, self.nodes[curr].depth, self.nodes[curr].heur)
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == 0 :     #if index not visited
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].heur = math.sqrt(math.pow(self.verticies[x].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[x].Y - self.verticies[goal.index].Y,2))
				queue[self.nodes[x].heur] = x
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
				if debug==1 :
					print "pushed %d (%d,%d)"%(x, self.verticies[x].X, self.verticies[x].Y)
		if len(queue) > max:
			max = len(queue)
		
 #ASTAR-Search
    def ASTAR_Search(self,initial_state, goal):
	queue = {}          #queue having heuristic and index value so that index having best heuristic value can be selected
	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	print "solution path:"
	queue[0] = initial_state.index
	while queue:
		
		best_heur = sorted(queue)[0]
		curr = queue[best_heur]; queue = {key: value for key, value in queue.items() if key != best_heur} #equivalent to taking  best element from queue
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks		
			return self.nodes[curr].tracebacks, v, i, max
			break
		
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == 0 :     #if index not visited
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].heur = math.sqrt(math.pow(self.verticies[x].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[x].Y - self.verticies[goal.index].Y,2)) + math.sqrt(math.pow(self.verticies[x].X - self.verticies[initial_state.index].X ,2) + math.pow(self.verticies[x].Y - self.verticies[initial_state.index].Y,2))
				queue[self.nodes[x].heur] = x
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
		if len(queue) > max:
			max = len(queue)
		i += 1	
