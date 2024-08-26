import pygame
import numpy as np
from math import *

from shapes import *
from render_tools import *


class RenderApp:
    def __init__(self):
        pygame.display.set_caption('3D RENDER')
        
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1200, 600
        self.CENTER_CORDS = self.WIDTH / 2, self.HEIGHT / 2
        self.BG_COLOR = (49, 79, 79)
        
        self.VERTICE_COLOR = (255, 0, 0)
        self.EDGE_COLOR = (255, 255, 255)
        self.FACE_COLORS = [(130, 130, 130),(120, 120, 120),(110, 110, 110),(100, 100, 100),(90, 90, 90),(80, 80, 80)]
        self.SCALE = 10
        
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.clock = pygame.time.Clock()
        
        self.model_index = 0
        self.shape = models[self.model_index]
        self.shape['vertices'] = center_shape(self.shape['vertices'])
        
    def run(self):
        pygame.init()
        mouse_is_pressed = False
        
        angle_x = 0
        angle_y = 0
        angle_z = 0
        
        center = None
        
        while True:
            self.clock.tick(60)
            self.screen.fill(self.BG_COLOR)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: self.change_model('+')
                    elif event.key == pygame.K_LEFT: self.change_model('-')
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_is_pressed = True
                    if center == None:
                        center = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_is_pressed = False

            if mouse_is_pressed:
                xy = pygame.mouse.get_pos()
                x = (xy[1] - center[1]) * -1
                y = (xy[0] - center[0]) * -1
                angle_x = x * 0.01
                angle_y = y * 0.01
            self.display(angle_x, angle_y, angle_z)
            
            pygame.display.update()
            
    def display(self, angle_x, angle_y, angle_z):
        rotated_vertices = rotate(rotate(rotate(self.shape['vertices'], angle_x, 0), angle_y, 1), angle_z, 2)
            
        projected_vertices = project_matrix(rotated_vertices)
        rescaled_vertices = rescale([self.SCALE, self.WIDTH, self.HEIGHT], projected_vertices)
                    
        draw_vertices(self, rescaled_vertices)
        draw_edges(self, self.shape['edges'], rescaled_vertices)
        draw_faces(self, self.shape['faces'], rescaled_vertices, rotated_vertices)
        
    def change_model(self, direction:str):
        if direction == '-':
            if self.model_index - 1 < 0: self.model_index = len(models) - 1
            else: self.model_index -= 1
        elif direction == '+':
            if self.model_index + 1 == len(models): self.model_index = 0
            else: self.model_index += 1
        self.shape = models[self.model_index]
        self.shape['vertices'] = center_shape(self.shape['vertices'])

    
if __name__ == '__main__':
    app = RenderApp()
    app.run()
