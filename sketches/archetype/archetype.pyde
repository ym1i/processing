# Archetype 101 | Kjetil Golid
# https://kjetil-golid.medium.com/archetype-101-2f17633dcc86
# ------------------------------------------------------------------------------------------

import datetime

from section import Section
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    

def draw():
    init()
    
    make_partitions()
    make_cells()
    make_partitions_in_cells()
    
    render()
    

def init():
    global sections, palette
    palette = Palette()
    sections = [Section(0, 0, width, height, palette)]
    

def make_partitions():
    global sections    
    next_sections = []
    
    for section in sections:
        n_split = int(random(2, 5))
        next_sections.extend(section.make_partitions_v(n_split, palette))
        
    sections = next_sections
    next_sections = []
    
    for section in sections:
        n_split = int(random(1, 5))
        next_sections.extend(section.make_partitions_h(n_split, palette))
    
    sections = next_sections
    next_sections = []
            
    for section in sections:
        n_split = int(random(1, 4))
        next_sections.extend(section.make_partitions_v(n_split, palette))
            
    sections = next_sections
    next_sections = []
    
    
def make_cells():
    global sections
    for section in sections:
        section.make_cells()
        

def make_partitions_in_cells():
    global sections
    for section in sections:
        section.split_cell()


def render():
    for section in sections:
        section.render()
        
        for cell in section.cells:
            cell.render()
            cell.render_partitions()


def pprint():
    i = 0
    for section in sections:
        i += 1
        print '{}: (x:{}, y:{}, w:{}, h:{})'.format(i, int(section.x), int(section.y), int(section.w), int(section.h))
    print '-' * 100


def keyPressed():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
        
        
        
        
        
        
        
        
        
        
        
        
        
