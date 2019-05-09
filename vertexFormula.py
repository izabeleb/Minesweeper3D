# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:48:56 2019

@author: bauzy
"""

class VertexList():
    
    @staticmethod
    def getList(numCol = 10, numRow = 10):

        verticesBase = (
                
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )
        
        
        xShift = 0
        yShift = 0
        
        boxes = []
        
        for r in range(numRow):
            
            xShift = 0
            
            for c in range(numCol):
                
                vertices = []
                
                for vertexBase in verticesBase:
                    
                    vertex = []
                    
                    vertex.append(vertexBase[0] + xShift)
                    vertex.append(vertexBase[1] + yShift)
                    vertex.append(vertexBase[2])
                    
                    vertices.append(tuple(vertex))
                    
                xShift += 2
                
                boxes.append(tuple(vertices))
        
            yShift += 2
            
        return boxes