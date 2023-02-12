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
    smooth()
    noLoop()
    
 
def draw():
    init()
    
    make_sections(1, 1, 1)
    make_cells()
    make_partitions(2)
    
    translate(width/2, height/2, -width/2)
    
    # camera(0, 0, 1500.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    ortho(-width, width, -height, height)
    
    rotateX(radians(-25))
    rotateY(radians(-45))

    render()
    
    t = datetime.datetime.now()
    saveFrame('{}{}_{}{}{}.png'.format(t.month, t.day, t.hour, t.minute, t.second))
     

def init(): 
    global sections, strategy, palette
    
    sections = [Section(-width/2, -height/2, -width/2, width, height, width)]
    palette = Palette()
    strategies = ['single', 'main', 'group', 'random']
    strategy = strategies[3]
    

def make_sections(y_split, x_split, z_split):
    global sections
    
    next = []
    while y_split > 0:
        for section in sections:
            offset = section.h / 10
            _h = random(offset, section.h - offset)
            # random_x = random(100)
            # random_z = random(100)
            next.append(Section(section.x, section.y, section.z, section.w, _h, section.d))
            next.append(Section(section.x, section.y + _h, section.z, section.w, section.h - _h, section.d))
        sections = next
        next = [] 
        y_split -= 1
        
    while x_split > 0:
        for section in sections:
            offset = section.w / 10
            _w = random(offset, section.w - offset)
            # random_y = random(100)
            # random_z = random(100)
            next.append(Section(section.x, section.y, section.z, _w, section.h, section.d))
            next.append(Section(section.x + _w, section.y, section.z, section.w - _w, section.h, section.d))
        sections = next
        next = []
        x_split -= 1
        
    while z_split > 0:
        for section in sections:
            offset = section.d / 10
            _d = random(offset, section.d - offset)
            next.append(Section(section.x, section.y, section.z, section.w, section.h, _d))
            next.append(Section(section.x, section.y, section.z + _d, section.w, section.h, section.d - _d))
        sections = next
        next = []
        z_split -= 1
        
        
def make_cells():
    global sections
    
    for section in sections:
        n_x = int(random(1, section.w / 50))
        n_y = int(random(1, section.h / 50))
        n_z = int(random(1, section.d / 50))
        cell_w = section.w / n_x
        cell_h = section.h / n_y
        cell_d = section.d / n_z
        
        for y in range(n_y):
            for x in range(n_x):
                for z in range(n_z):
                    section.cells.append(Cell(section.x + cell_w * x, section.y + cell_h * y, section.z + cell_d * z, cell_w, cell_h, cell_d, strategy))
                
        colors = [palette.random_color()]
        
        for cell in section.cells:
            cell.partitions.append(Partition(cell.x, cell.y, cell.z, cell.w, cell.h, cell.d))
            cell.set_colors(colors) 

        
def make_partitions(n_split):
    global sections
    
    for section in sections:    
        for split in range(n_split):
            n_partitions = len(section.cells[0].partitions)
            for i in range(n_partitions):
                partition = section.cells[0].partitions[i]

                rand = random(1)
                if rand < 0.33:
                    offset = partition.h / 10
                    h = random(offset, partition.h - offset)
                    
                    for cell in section.cells:
                        p = cell.partitions[0]
                        cell.partitions.pop(0)
                        cell.partitions.append(Partition(p.x, p.y, p.z, p.w, h, p.d))
                        cell.partitions.append(Partition(p.x, p.y + h, p.z, p.w, p.h - h, p.d))
                elif rand > 0.66:
                    offset = partition.w / 10
                    w = random(offset, partition.w - offset)
                
                    for cell in section.cells:
                        p = cell.partitions[0]
                        cell.partitions.pop(0)
                        cell.partitions.append(Partition(p.x, p.y, p.z, w, p.h, p.d))
                        cell.partitions.append(Partition(p.x + w, p.y, p.z, p.w - w, p.h, p.d))
                else:
                    offset = partition.d / 10
                    d = random(offset, partition.d - offset)
                
                    for cell in section.cells:
                        p = cell.partitions[0]
                        cell.partitions.pop(0)
                        cell.partitions.append(Partition(p.x, p.y, p.z, p.w, p.h, d))
                        cell.partitions.append(Partition(p.x, p.y, p.z + d, p.w, p.h, p.d - d))
                    
        
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
        
