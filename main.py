import pygame
import numpy as np
from math import *
from shapes import *
from render_tools import *

shape = cube
#shape['vertices'] = rotate(shape['vertices'], 1.6, 0)


class RenderApp:
    def __init__(self):
        pygame.display.set_caption('3D RENDER')
        
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1200, 800
        self.BG_COLOR = (49, 79, 79)
        
        self.VERTICE_COLOR = (255, 0, 0)
        self.EDGE_COLOR = (255, 255, 255)
        self.FACE_COLOR = (100, 100, 100)
        self.SCALE = 10
        
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.clock = pygame.time.Clock()
        
    def run(self):
        pygame.init()
        angle = 0
        
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                        
            self.screen.fill(self.BG_COLOR)
                        
            rotated_vertices = rotate(rotate(shape['vertices'], angle, 1), angle, 0)
            projected_vertices = project_matrix(rotated_vertices)
            rescaled_vertices = rescale([self.SCALE, self.WIDTH, self.HEIGHT], projected_vertices)
            
            draw_vertices(self, rescaled_vertices)
            draw_edges(self, shape['edges'], rescaled_vertices)
            draw_faces(self, shape['faces'], rescaled_vertices)
            
            pygame.display.update()
            
            angle += 0.01
        
        pygame.quit()

    
if __name__ == '__main__':
    app = RenderApp()
    app.run()
