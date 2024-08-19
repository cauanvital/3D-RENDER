import pygame
import numpy as np
from math import *

from shapes import *
from render_tools import *

shape = mario


class RenderApp:
    def __init__(self):
        pygame.display.set_caption('3D RENDER')
        
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1200, 600
        self.CENTER_CORDS = self.WIDTH / 2, self.HEIGHT / 2
        self.BG_COLOR = (49, 79, 79)
        
        self.VERTICE_COLOR = (255, 0, 0)
        self.EDGE_COLOR = (255, 255, 255)
        self.FACE_COLOR = (100, 100, 100)
        self.SCALE = 10
        
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.clock = pygame.time.Clock()
        
    def run(self):
        pygame.init()
        mouse_is_pressed = False
        
        angle_x = 0
        angle_y = 0
        angle_z = 0
        
        while True:
            self.clock.tick(60)
            self.screen.fill(self.BG_COLOR)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_is_pressed = True
                    pygame.mouse.set_pos(self.CENTER_CORDS)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_is_pressed = False
            if mouse_is_pressed:
                xy = pygame.mouse.get_pos()
                x = xy[0] - self.CENTER_CORDS[0]
                y = xy[1] - self.CENTER_CORDS[1]
                angle_x = x * 0.01
                angle_y = y * 0.01
            self.display(angle_x, angle_y, angle_z)
            
            pygame.display.update()
            
    def display(self, angle_x, angle_y, angle_z):
        rotated_vertices = rotate(rotate(rotate(shape['vertices'], angle_x, 0), angle_y, 1), angle_z, 2)
            
        projected_vertices = project_matrix(rotated_vertices)
        rescaled_vertices = rescale([self.SCALE, self.WIDTH, self.HEIGHT], projected_vertices)
                    
        draw_vertices(self, rescaled_vertices)
        draw_edges(self, shape['edges'], rescaled_vertices)
        draw_faces(self, shape['faces'], rescaled_vertices)

    
if __name__ == '__main__':
    app = RenderApp()
    app.run()
