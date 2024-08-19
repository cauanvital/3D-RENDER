import pygame
import numpy as np
from math import *
from shapes import *
from render_tools import *

shape = mario
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                        
            self.screen.fill(self.BG_COLOR)
                        
            rotated_shape = rotate(rotate(shape['vertices'], angle, 1), angle, 0)
            projected_shape = project_matrix(rotated_shape)
            rescale_shape = rescale([self.SCALE, self.WIDTH, self.HEIGHT], projected_shape)
            
            for v in rescale_shape:
                pygame.draw.circle(self.screen, self.VERTICE_COLOR, v, 1)
            draw_edges(self, shape['edges'], rescale_shape)
                
                
            pygame.display.update()
            
            angle += 0.01

    
if __name__ == '__main__':
    app = RenderApp()
    app.run()
