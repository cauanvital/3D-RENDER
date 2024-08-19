import numpy as np

def center_shape(vertices):
    centered = []
    
    c_x = sum([i[0] for i in vertices]) / len(vertices)
    c_y = sum([i[1] for i in vertices]) / len(vertices)
    c_z = sum([i[2] for i in vertices]) / len(vertices)
    
    for vertex in vertices:
        c_vertex = np.array([
            vertex[0] - c_x,
            vertex[1] - c_y,
            vertex[2] - c_z
        ])
        
        centered.append(c_vertex)
    
    return centered
    
