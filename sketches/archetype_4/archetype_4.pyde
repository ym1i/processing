# Archetype 101 | Kjetil Golid
# https://kjetil-golid.medium.com/archetype-101-2f17633dcc86
# ------------------------------------------------------------------------------------------

import datetime

from section import Section
from palette import Palette


def setup():
    global sections, sections_2, palette
    
    size(800, 800)
    background(255)
    
    palette = Palette()
    palette.mantel_colors()
    palette.golid_colors()
    sections = []
    sections_2 = []
    

def draw():
    noLoop()
    make_sections()
    # make_partitions()
    
    for section in sections:
        section.render_fill()
        n_cell = int(random(2, 4))
        section.make_cells(n_cell)
        x = random(50, section.w / n_cell - 50)
        y = random(50, section.h / n_cell - 50)
        for cell in section.cells:
            cell.render()
            make_sections_2(cell, x, y)
            
    for section in sections_2:
        section.render_stroke()
    #     n_cell = int(random(2, 6))
    #     section.make_cells(n_cell)
    #     y = random(25, section.h)
    #     for cell in section.cells:
    #         cell.render()
    
def make_sections():
    global sections
    
    x = int(random(100, width - 100))
    y = int(random(100, height - 100))
    sections.append(Section(0, 0, x, y, palette))
    sections.append(Section(x, 0, width - x, y, palette))
    sections.append(Section(0, y, x, height - y, palette))
    sections.append(Section(x, y, width - x, height - y, palette))
    
def make_partitions():
    global sections
    
    n_cols = int(random(1, 4))
    n_rows = int(random(1, 4))
    
    section_width = width / n_cols
    section_height = height / n_rows
    
    for j in range(n_rows):
        for i in range(n_cols):
            sections.append(Section(section_width * i, section_height * j, section_width, section_height, palette))
    
    
def make_sections_2(cell, x, y):
    global sections_2
    
    sections_2.append(Section(cell.x, cell.y, x, y, palette))
    sections_2.append(Section(cell.x + x, cell.y, cell.w - x, y, palette))
    sections_2.append(Section(cell.x, cell.y + y, x, cell.h - y, palette))
    sections_2.append(Section(cell.x + x, cell.y + y, cell.w - x, cell.h - y, palette))

    
def keyPressed():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
        
        
        
        
        
        
        
        
        
        
        
        
        
