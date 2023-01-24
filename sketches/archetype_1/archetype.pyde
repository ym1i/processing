# Archetype 101 | Kjetil Golid
# https://kjetil-golid.medium.com/archetype-101-2f17633dcc86
# 1/19/2023
# ------------------------------------------------------------------------------------------

import datetime

from section import Section
from palette import Palette


def setup():
    global sections, palette
    
    size(600, 600)
    background(255)
    
    palette = Palette()
    palette.mantel_colors()
    sections = []
    

def draw():
    noLoop()
    make_sections()
    
    for section in sections:
        section.render()
        section.draw_circle()

    
def make_sections():
    global sections
    
    x = int(random(30, width))
    y = int(random(30, height))
    
    sections.append(Section(0, 0, x, y, palette))
    sections.append(Section(0, y, x, height - y, palette))
    sections.append(Section(x, 0, width - x, y, palette))
    sections.append(Section(x, y, width - x, height - y, palette))
    
    
def keyPressed():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
        
        
        
        
        
        
        
        
        
        
        
        
        
