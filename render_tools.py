import numpy as np
import pygame
from math import *

PROJECTION_MATRIX = np.array([(1, 0, 0),
                              (0, 1, 0)])


def project_matrix(matrix_list):
    matrix_list = [np.matmul(PROJECTION_MATRIX, matrix) for matrix in matrix_list]
    
    return [(float(i[0]), float(i[1])) for i in matrix_list]

def rotate(matrix_list:list[np.array], angle:float = 0, axis:int = None):
    rotation = 1
    
    if axis == 0: # rotate in X axis
        rotation = np.array([
            (1, 0, 0),
            (0, cos(angle), -sin(angle)),
            (0, sin(angle), cos(angle))
        ])
    elif axis == 1: # rotate in Y axis
        rotation = np.array([
            (cos(angle), 0, sin(angle)),
            (0, 1, 0),
            (-sin(angle), 0, cos(angle))
        ])
    elif axis == 2: # rotate in Z axis
        rotation = np.array([
            (cos(angle), -sin(angle), 0),
            (sin(angle), cos(angle), 0),
            (0, 0, 1)
        ])
        
    matrix_list = [np.matmul(rotation, matrix) for matrix in matrix_list]
    
    return matrix_list

def rescale(scales, vertices):
    rescaled_shape = []
    
    for vertex in vertices:
        x = vertex[0] * scales[0] + scales[1] / 2
        y = vertex[1] * scales[0] + scales[2] / 2
        rescaled_shape.append((x,y))
    
    return rescaled_shape

def draw_vertices(app, vertices):
    for vertex in vertices:
        pygame.draw.circle(app.screen, app.VERTICE_COLOR, vertex, 1)

def draw_edges(app, edges, vertices):
    for edge in edges:
        x1 = edge[0]
        x2 = edge[1]
        pygame.draw.line(
            app.screen,
            app.EDGE_COLOR,
            (vertices[x1][0], vertices[x1][1]),
            (vertices[x2][0], vertices[x2][1]),
            1
        )
        
def draw_faces(app, faces:list, projected:list, rotated:list):
    z_pos_dict = [(sum([rotated[i][2] for i in face]), face) for face in faces]
    sorted_z_pos = list(sorted(z_pos_dict.items(), key=lambda x: x[1]))
    ordered_faces = []
    
    for z in sorted_z_pos:
        if 'z_pos_list' not in locals(): z_pos_list = []
        for face in faces:
            if z in face and [i for i in z_pos_list if i in face]: ordered_faces.append(face)
        
        z_pos_list.append(z)
    
    for face in ordered_faces:
        face_vertices = []
        if 'color' not in locals() or color == 6: color = 0
            
        for i in face:
            face_vertices.append(np.array([projected[i][0], projected[i][1]]))
                                 
        pygame.draw.polygon(app.screen, app.FACE_COLORS[color], face_vertices)
        color += 1
