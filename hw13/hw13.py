#вариант1
#какова максимальная глубина папки в этом дереве (глубину папки с программой нужно считать равной 0) 

import os
import re
lst = []
deep = []

start_path = os.getcwd()
for root, dirs, files in os.walk(start_path):
    if dirs != []:
        fol = re.findall( r'\\', root)
        depth = len(fol)
        deep.append(depth)
        max_d = max(deep)
        sp = re.findall( r'\\', start_path)
        len_sp = len(sp)
        final_depth = max_d - len_sp + 1
print('Максимальная глубина папки в этом дереве: ',final_depth)
