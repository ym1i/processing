# Archetype 101 | Kjetil Golid
# https://kjetil-golid.medium.com/archetype-101-2f17633dcc86
# ------------------------------------------------------------------------------------------

import datetime

from section import Section
from palette import Palette


def setup():
    global sections, sections_2, palette
    
    size(600, 600)
    background(255)
    
    palette = Palette()
    palette.mantel_colors()
    palette.golid_colors()
    sections = []
    sections_2 = []
    

def draw():
    noLoop()
    make_sections()
    
    for section in sections:
        # section.render()
        n_cell = int(random(3, 8))
        section.make_cells(n_cell)
        y = random(50, section.h)
        for cell in section.cells:
            # cell.render()
            make_sections_2(cell, y)
            
    for section in sections_2:
        section.render()
        n_cell = int(random(2, 6))
        section.make_cells(n_cell)
        y = random(25, section.h)
        for cell in section.cells:
            cell.render()
    
def make_sections():
    global sections
    
    y = int(random(100, height))
    sections.append(Section(0, 0, width, y, palette))
    sections.append(Section(0, y, width, height - y, palette))
    
    
def make_sections_2(cell, y):
    global sections_2
    
    sections_2.append(Section(cell.x, cell.y, cell.w, y, palette))
    sections_2.append(Section(cell.x, cell.y + y, cell.w, cell.h - y, palette))

    
def keyPressed():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
        
        
        
        
        
        
        
        
        
        
        
        
        
