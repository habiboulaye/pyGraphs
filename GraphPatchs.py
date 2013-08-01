#!/usr/bin/env python2
# -*- coding: latin-1 -*-
"""
    Graphs Paths algorithms  
"""
import sys
from Queue import PriorityQueue
#from GraphSearch import cGraph

#Minimum Spanning Tree
def Prims(Graph,vStart,vEnd):
    """
        Prim's: Minimum Spanning Tree algorithm
    """
    Dist={}
    for i in Graph.VertexList:
        Dist[i]=sys.maxint

    Dist[vStart]=0
    PrtQ=PriorityQueue()
    PrtQ.put((0,vStart))
    Prev={}
    Prev[vStart]=None
    while not PrtQ.empty():
        iV=PrtQ.get()[1]
        Graph.setVisited(iV)
        for jV in Graph.VertexList:
            if Graph.Edges[(iV,jV)] and not Graph.setVisited(jV):
                ### Prim's Cost : Greedy
                if Dist[jV] > Graph.Dist[(iV,jV)]: 
                    Dist[jV] = Graph.Dist[(iV,jV)]
                    Prev[jV]=iV
                    PrtQ.put((Dist[jV],jV))
    
    print ("Prim's Distance Min:", Dist[vEnd])
    iV=vEnd
    minTree={}
    for ij in Graph.Edges:
        if Graph.Edges[ij]==True and ij[0]<=ij[1]:
            if (Prev[ij[0]]==ij[1] or Prev[ij[1]]==ij[0]):
                minTree[ij]=Graph.Edges[ij]
    print ("Prim's MST  :", minTree)


#Shortest-path
def Dijkstra(Graph,vStart,vEnd):
    """
        Dijkstra: Shortest-path algorithm
    """
    Dist={}
    for i in Graph.VertexList:
        Dist[i]=sys.maxint

    Dist[vStart]=0
    PrtQ=PriorityQueue()
    PrtQ.put((0,vStart))
    Prev={}
    Prev[vStart]=None
    while not PrtQ.empty():
        iV=PrtQ.get()[1]
        Graph.setVisited(iV)
        for jV in Graph.VertexList:
            if Graph.Edges[(iV,jV)] and not Graph.setVisited(jV):
                ### Dijkstra Cost : Shortest Path
                if Dist[jV] > Dist[iV] + Graph.Dist[(iV,jV)]:
                    Dist[jV] = Dist[iV] + Graph.Dist[(iV,jV)]
                    Prev[jV]=iV
                    PrtQ.put((Dist[jV],jV))
    
    print ("Dijkstra Distance Min: {0}".format(Dist[vEnd]))
    print ("Dijkstra Shortest Path:")
    iV=vEnd
    while iV!=None:
        print (iV),
        iV=Prev[iV]


#All-shortest-paths
def FloydWarshall(Graph):
    """
        FloydWarshall: All-shortest-paths algorithm
    """
    Dist={}
    for i in Graph.VertexList:
        for j in Graph.VertexList:
            if i==j:
                Dist[(i,j)]=0
            elif Graph.Edges[(i,j)]:
                Dist[(i,j)]=Graph.Dist[(i,j)]
            else:     
                Dist[(i,j)]=sys.maxint
    Next={}
    for i in Graph.VertexList:
        for j in Graph.VertexList:
            for k in Graph.VertexList:
                if Dist[(i,k)] > Dist[(i,j)] + Dist[(j,k)]:
                    Dist[(i,k)] = Dist[(i,j)] + Dist[(j,k)]
                    Next[(i,k)] = j
                    
    print ("Shortest Paths: {0}".format(Dist))
    print ("Paths Next : {0}".format(Next))
        
