import numpy as np
from shapes import *

rotated = {i:cube['vertices'][i] for i in range(len(cube['vertices']))}
rotated = {i:j for i,j in sorted(rotated.items(), key=lambda x: x[1][2], reverse=True)}
print(rotated)
