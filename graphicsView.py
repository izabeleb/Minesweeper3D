# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:50:58 2019

@author: bauzy
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from vertexFormula import VertexList

boxes = VertexList.getList()

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube(vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


thing = pygame.Surface((50, 50))
thing.fill((255, 255, 255))


def main():
    pygame.init()
    display = (800,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.5,0.0, -40)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    
                    pass
                
                if event.key == pygame.K_DOWN:
                    
                    pass
                
                if event.key == pygame.K_LEFT:
                    
                    pass
                
                if event.key == pygame.K_RIGHT:
                    
                    pass

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        for vertices in boxes:
            
            Cube(vertices)
        
        # can't blit pygame Surfaces with OpenGL display :(
        #screen.blit(thing, (0, 0))
        
        pygame.display.flip()
        pygame.time.wait(10)


main()