#!/usr/bin/python
import copy

#Class for Vertex
class Vertex:
    def __init__(self, stacks):
        self.stacks = stacks          #Type: List[List[char]]
    
    def display(self):
        print "____________________________________"
        for stack in self.stacks:
            print stack
        print "____________________________________"
        
        
class Node:
    def __init__(self, vertex, parent = None) :
        self.vertex = vertex                #Type: Vertex
        self.parent = parent
        self.depth = 0
        self.heur = 0.0
        self.successor = []
        self.traceback = []

    def successors(self):
        if self.successor == [] :
            for i in range(len(self.vertex.stacks)):                #stores all possible next states in successor
               #print newstacks
               for j in range(len(self.vertex.stacks)) :
                   newstacks = copy.deepcopy(self.vertex.stacks)
                   temp = newstacks[i][len(newstacks[i]) - 1]
                   del newstacks[i][len(newstacks[i])-1:]
                   if(i==j) :
                       continue
                   newstacks[j].append(temp)
                   self.successor.append(Vertex(newstacks))
        return self.successor
                        
