#!/usr/bin/env python2
# -*- coding: latin-1 -*-
"""
    Graphs Representation
    - Matrix (dense) or List (sparse)
    Graphs Search algorithms
    - Depth First Search
    - Breadth First Search
"""
from Queue import LifoQueue, Queue

#     Graphs Representation
class cGraph:
    """
        Graphs (Matrix) Representation
    """
    def __init__(self, nCount):
        self.VertexList=range(nCount)
        self.Edges={}
        self.Visited={}
        self.Dist={}
        for i in self.VertexList:
            for j in self.VertexList:
                self.Edges[(i,j)]=False
        self.initVisit()
        
    def initVisit(self):
        for i in self.VertexList:
            self.Visited[i]=False
    
    def addEdge(self,i,j,dist=None):
        self.Edges[(i,j)]=True
        self.Edges[(j,i)]=True
        if dist:
            self.Dist[(i,j)]=dist
            self.Dist[(j,i)]=dist
    
    def setVisited(self,i):
        self.Visited[i]=True
    
    def printGraph(self):
        print (self.VertexList)
        print (self.Edges)
        print (self.Visited)
        
#     Graphs Search algorithms
def recursiveDFS(Graph, vroot):
    """
        Depth First Search: recursive version
    """
    iV=vroot
    print ("Visit :", iV)
    Graph.setVisited(iV)
    for jV in Graph.VertexList:
        if Graph.Edges[iV,jV] and not Graph.Visited[jV]:
            recursiveDFS(Graph, jV)

def stackDFS(Graph, vroot):
    """
        Depth First Search: stack version
    """
    Stack=LifoQueue()
    Stack.put(vroot)
    while not Stack.empty():
        iV=Stack.get()
        print ("Visit :", iV)
        Graph.setVisited(iV)
        for jV in Graph.VertexList:
            if Graph.Edges[iV,jV] and not Graph.Visited[jV]:
                Stack.put(jV)

def BFS(Graph, vroot):
    """
        Breadth First Search
    """
    FIFO=Queue()
    FIFO.put(vroot)
    while not FIFO.empty():
        iV=FIFO.get()
        print ("Visit :", iV)
        Graph.setVisited(iV)
        for jV in Graph.VertexList:
            if Graph.Edges[iV,jV] and not Graph.Visited[jV]:
                FIFO.put(jV)

