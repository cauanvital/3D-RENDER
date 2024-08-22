import numpy as np
from shapes import *


z_pos_dict = {i:j for i,j in enumerate([i[2] for i in mario['vertices']])}
sorted_z_pos = dict(sorted(z_pos_dict.items(), key=lambda x: x[1], reverse=True))

for index in sorted_z_pos.keys():
    ...
    
abc = dict(sorted({4: 'a', 0: 'a', 7: 'a', 1: 'a'}.items(), key=lambda x: x[0], reverse=True))

if [1,2,5]:
    print(abc)
