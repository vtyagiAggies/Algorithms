#!/usr/bin/python

from state import Node
from state import Vertex

if __name__ == "__main__":
    stack = [['A', 'B', 'C'],['D'],['E','F','G']]
    initialvertex = Vertex(stack)
    initialstate = Node(initialvertex)
    for x in initialstate.successors():
        x.display()
    #print initialvertex.stacks
    
