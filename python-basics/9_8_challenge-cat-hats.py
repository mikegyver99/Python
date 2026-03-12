# -*- coding: utf-8 -*-
"""
created on 2026-03-10 08:37:33
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# 100 cats no hats, put hats on all. 
# Then every 2, 4, 6 check if hat remove if no hat put on if hat remove it. 
# Then every 3, 6, 9 check if hat remove if no hat put on if hat remove it. 
# repeat

cats_with_hats={'cat1': '', 'cat2': '', 'cat3': '', 'cat4': '', 'cat5': '', 'cat6': '', 'cat7': '', 'cat8': '', 'cat9': '', 'cat10': '', 'cat11': '', 'cat12': '', 'cat13': '', 'cat14': '', 'cat15': '', 'cat16': '', 'cat17': '', 'cat18': '', 'cat19': '', 'cat20': '', 'cat21': '', 'cat22': '', 'cat23': '', 'cat24': '', 'cat25': '', 'cat26': '', 'cat27': '', 'cat28': '', 'cat29': '', 'cat30': '', 'cat31': '', 'cat32': '', 'cat33': '', 'cat34': '', 'cat35': '', 'cat36': '', 'cat37': '', 'cat38': '', 'cat39': '', 'cat40': '', 'cat41': '', 'cat42': '', 'cat43': '', 'cat44': '', 'cat45': '', 'cat46': '', 'cat47': '', 'cat48': '', 'cat49': '', 'cat50': '', 'cat51': '', 'cat52': '', 'cat53': '', 'cat54': '', 'cat55': '', 'cat56': '', 'cat57': '', 'cat58': '', 'cat59': '', 'cat60': '', 'cat61': '', 'cat62': '', 'cat63': '', 'cat64': '', 'cat65': '', 'cat66': '', 'cat67': '', 'cat68': '', 'cat69': '', 'cat70': '', 'cat71': '', 'cat72': '', 'cat73': '', 'cat74': '', 'cat75': '', 'cat76': '', 'cat77': '', 'cat78': '', 'cat79': '', 'cat80': '', 'cat81': '', 'cat82': '', 'cat83': '', 'cat84': '', 'cat85': '', 'cat86': '', 'cat87': '', 'cat88': '', 'cat89': '', 'cat90': '', 'cat91': '', 'cat92': '', 'cat93': '', 'cat94': '', 'cat95': '', 'cat96': '', 'cat97': '', 'cat98': '', 'cat99': '', 'cat100': ''}
# cats_with_hats={'cat1': '', 'cat2': '', 'cat3': '', 'cat4': '', 'cat5': '', 'cat6': '', 'cat7': '', 'cat8': '', 'cat9': '', 'cat10': '', 'cat11': '', 'cat12': '', 'cat13': '', 'cat14': '', 'cat15': '', 'cat16': '', 'cat17': '', 'cat18': '', 'cat19': '', 'cat20': '', 'cat21': '', 'cat22': '', 'cat23': '', 'cat24': '', 'cat25': '', 'cat26': '', 'cat27': '', 'cat28': '', 'cat29': '', 'cat30': '', 'cat31': '', 'cat32': '', 'cat33': '', 'cat34': '', 'cat35': '', 'cat36': '', 'cat37': '', 'cat38': '', 'cat39': '', 'cat40': '', 'cat41': '', 'cat42': '', 'cat43': '', 'cat44': '', 'cat45': '', 'cat46': '', 'cat47': '', 'cat48': '', 'cat49': '', 'cat50': '', 'cat51': '', 'cat52': '', 'cat53': '', 'cat54': '', 'cat55': '', 'cat56': '', 'cat57': '', 'cat58': '', 'cat59': '', 'cat60': '', 'cat61': '', 'cat62': '', 'cat63': '', 'cat64': '', 'cat65': '', 'cat66': '', 'cat67': '', 'cat68': '', 'cat69': '', 'cat70': '', 'cat71': '', 'cat72': '', 'cat73': '', 'cat74': '', 'cat75': '', 'cat76': '', 'cat77': '', 'cat78': '', 'cat79': '', 'cat80': '', 'cat81': '', 'cat82': '', 'cat83': '', 'cat84': '', 'cat85': '', 'cat86': '', 'cat87': '', 'cat88': '', 'cat89': '', 'cat90': '', 'cat91': '', 'cat92': '', 'cat93': '', 'cat94': '', 'cat95': '', 'cat96': '', 'cat97': '', 'cat98': '', 'cat99': '', 'cat100': ''}

# for name, hat in cats_with_hats.items():
#     if hat == "":
#         cats_with_hats[name] = "Hat"
# print(cats_with_hats)

for i in range(1, 101,):
    for j in range(1, 101, i):
        cats_with_hats[(f"cat{i}")] = "Hat"
        
# print(cats_with_hats)
for name, hat in cats_with_hats.items():
    if hat == "":
        print(f"Cat {name} has no hat!")
  