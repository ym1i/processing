from random import randint

from section import Section
from cell import Cell
from wrapper import Wrapper
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    
def draw():
    render()
     

def init(): 
    global sections, palette, wrappings
    
    sections = [Section(0, 0, width, height)]
    palette = Palette()
    make_sections(2)
    make_cells()
    wrappings = wrap()
    

def render():
    noFill()
    for section in sections:
        section.render()
        for cell in section.cells:
            cell.pegs.render()
    
    for wrapping in wrappings:
        wrapping.render(palette.random_color(), palette.random_color(), sw=2, no_fill=True, no_stroke=False)
            

def wrap():
    wrappings = []
    # wrapping = Wrapper()
    # pegs2wrap = []
    for section in sections:
        pegs2wrap = []
        wrapping = Wrapper()
        for cell in section.cells:
            i = randint(0, 8)
            pegs2wrap.append(cell.pegs.pegs[i])
        wrapping.wrap(pegs2wrap)
        wrappings.append(wrapping)
        
    # wrapping.wrap(pegs2wrap)
    # wrapping.ameba_wrap(pegs2wrap)
    
    return wrappings

def make_sections(n):
    global sections
    
    next = []
    
    for i in range(n):
        for section in sections:
            offset = section.h / 4
            h = random(offset, section.h - offset)
            next.append(Section(section.x, section.y, section.w, h))
            next.append(Section(section.x, section.y + h, section.w, section.h - h))
        sections = next
        next = []
        
        for section in sections:
            offset = section.w / 5
            w = random(offset, section.w - offset)
            next.append(Section(section.x, section.y, w, section.h))
            next.append(Section(section.x + w, section.y, section.w - w, section.h))
        sections = next
        next = []
        

def make_cells():
    global sections
    
    for section in sections:
        n_cols = max(int(section.w / 100), 1)
        n_rows = max(int(section.h / 100), 1)
        cell_w = section.w / n_cols
        cell_h = section.h / n_rows
        n_grid = 3
        radius = cell_w / (n_grid + 1) * 0.3 if cell_w < cell_h else cell_h / (n_grid + 1) * 0.3
        
        for row in range(n_rows):
            for col in range(n_cols):
                section.cells.append(Cell(section.x + cell_w * col, section.y + cell_h * row, cell_w, cell_h, n_grid, radius))
        
            
