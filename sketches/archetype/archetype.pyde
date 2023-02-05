# Archetype 101 | Kjetil Golid
# https://kjetil-golid.medium.com/archetype-101-2f17633dcc86
# ------------------------------------------------------------------------------------------

import datetime

from section import Section
from cell import Cell
from partition import Partition
from palette import Palette


def setup():
    size(800, 800, P3D)
    background(255)
    noLoop()
    
 
def draw():
    init()
    
    make_sections(int(random(1, 4)), int(random(1, 4)))
    make_cells()
    make_partitions(3)
    
    translate(300, -150, -200)
    
    rotateX(radians(25))
    rotateZ(radians(30))

    
    render()
    saveFrame('{}.png'.format(datetime.datetime.now()))
     

def init(): 
    global sections, strategy, palette
    
    sections = [Section(0, 0, width, height)]
    palette = Palette()
    strategies = ['single', 'main', 'group', 'random']
    strategy = strategies[3]
    

def make_sections(v_split, h_split):
    global sections
    
    next = []
    while v_split > 0:
        for section in sections:
            offset = section.h / 10
            h = random(offset, section.h - offset)
            next.append(Section(section.x, section.y, section.w, h))
            next.append(Section(section.x, section.y + h, section.w, section.h - h))
        sections = next
        next = []
        v_split -= 1
        
    while h_split > 0:
        for section in sections:
            offset = section.w / 10
            w = random(offset, section.w - offset)
            next.append(Section(section.x, section.y, w, section.h))
            next.append(Section(section.x + w, section.y, section.w - w, section.h))
            # next.append(Section(section.x, section.x + w, section.w - w, section.h))
        sections = next
        next = []
        h_split -= 1
        
        
def make_sections_3d():
    pass
    
        
def make_cells():
    global sections
    
    for section in sections:
        n_cols = int(random(1, section.w / 30))
        n_rows = int(random(1, section.h / 30))
        cell_w = section.w / n_cols
        cell_h = section.h / n_rows
        
        for row in range(n_rows):
            for col in range(n_cols):
                section.cells.append(Cell(section.x + cell_w * col, section.y + cell_h * row, cell_w, cell_h, strategy))
                
        for cell in section.cells:
            cell.partitions.append(Partition(cell.x, cell.y, 0, cell.w, cell.h, random(10)))
        
        
def make_partitions(n_split):
    global sections
    
    for section in sections:    
        for split in range(n_split):
            n_partitions = len(section.cells[0].partitions)
            for i in range(n_partitions):
                partition = section.cells[0].partitions[i]

                if random(1) < 0.5:
                    offset = partition.h / 10
                    h = random(offset, partition.h - offset)
                    d = random(30)
                    
                    for cell in section.cells:
                        p = cell.partitions[0]
                        cell.partitions.pop(0)
                        cell.partitions.append(Partition(p.x, p.y, 0, p.w, h, d))
                        cell.partitions.append(Partition(p.x, p.y + h, 0, p.w, p.h - h, d))
                else:
                    offset = partition.w / 10
                    w = random(offset, partition.w - offset)
                    d = random(30)
                
                    for cell in section.cells:
                        p = cell.partitions[0]
                        cell.partitions.pop(0)
                        cell.partitions.append(Partition(p.x, p.y, 0, w, p.h, d))
                        cell.partitions.append(Partition(p.x + w, p.y, 0, p.w - w, p.h, d))
        
        colors = []
        for partition in section.cells[0].partitions:
            colors.append(palette.random_color())
            
        for cell in section.cells:
            cell.set_colors(colors)   
                            
        
def render():
    for section in sections:
        for cell in section.cells:
            cell.render_3D()
            # cell.render()
            

def keyPressed():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
                            
                                
                                                                

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
# def make_partitions():
#     global sections    
#     next_sections = []
    
#     for section in sections:
#         n_split = int(random(2, 5))
#         next_sections.extend(section.make_partitions_v(n_split, strategy, palette))
        
#     sections = next_sections
#     next_sections = []
    
#     for section in sections:
#         n_split = int(random(1, 5))
#         next_sections.extend(section.make_partitions_h(n_split, strategy, palette))
    
#     sections = next_sections
#     next_sections = []
            
#     for section in sections:
#         n_split = int(random(1, 4))
#         next_sections.extend(section.make_partitions_v(n_split, strategy, palette))
            
#     sections = next_sections
#     next_sections = []
        
                
# def make_partitions(v_split, h_split):    
#     for section in sections:
#         for v in range(v_split):
#             n_partitions = len(section.cells[0].partitions)
#             for i in range(n_partitions):
#                 partition = section.cells[0].partitions[i]    
#                 offset = partition.h / 10
#                 h = random(offset, partition.h - offset)
                
#                 for cell in section.cells:
#                     p = cell.partitions[0]
#                     cell.partitions.pop(0)
#                     cell.partitions.append(Partition(p.x, p.y, 0, p.w, h, cell.color, palette, section, strategy))
#                     cell.partitions.append(Partition(p.x, p.y + h, 0, p.w, p.h - h, cell.color, palette, section, strategy))
#         for h in range(h_split):
#             n_partitions = len(section.cells[0].partitions)
#             for i in range(n_partitions):
#                 partition = section.cells[0].partitions[i]    
#                 offset = partition.w / 10
#                 w = random(offset, partition.w - offset)
                
#                 for cell in section.cells:
#                     p = cell.partitions[0]
#                     cell.partitions.pop(0)
#                     cell.partitions.append(Partition(p.x, p.y, 0, w, p.h, cell.color, palette, section, strategy))
#                     cell.partitions.append(Partition(p.x + w, p.y, 0, p.w - w, p.h, cell.color, palette, section, strategy))
     
           
# def make_cells():
#     global sections
#     for section in sections:
#         section.make_cells()

# def make_partitions_in_cells():
#     global sections
#     for section in sections:
#         section.split_cell()    
        
        
        
        
        
        
        
