import datetime

from section import Section
from cell import Cell
from partition import Partition
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    
def draw():
    render()
    # saveFrame('{}.png'.format(datetime.datetime.now()))
     

def init(): 
    global sections, palette
    
    sections = [Section(0, 0, width, height)]
    palette = Palette()
    make_sections(int(random(1, 4)), int(random(1, 4)))
    make_cells()
    # make_partitions(3)
    

def make_sections(v_split, h_split):
    global sections
    
    next = []
    while v_split > 0:
        for section in sections:
            offset = section.h / 4
            h = random(offset, section.h - offset)
            next.append(Section(section.x, section.y, section.w, h))
            next.append(Section(section.x, section.y + h, section.w, section.h - h))
        sections = next
        next = []
        v_split -= 1
        
    while h_split > 0:
        for section in sections:
            offset = section.w / 5
            w = random(offset, section.w - offset)
            next.append(Section(section.x, section.y, w, section.h))
            next.append(Section(section.x + w, section.y, section.w - w, section.h))
        sections = next
        next = []
        h_split -= 1
        

def make_cells():
    global sections
    layouts = ['grid_3', 'grid_4', 'grid_5']
    scalings = ['uniform', 'bigger_near_center', 'smaller_near_center']
    
    for section in sections:
        n_cols = int(random(1, section.w / 80))
        n_rows = int(random(1, section.h / 80))
        cell_w = section.w / n_cols
        cell_h = section.h / n_rows
        layout = layouts[int(random(len(layouts)))]
        # layout = layouts[0]
        scaling = scalings[0]
        n_grid = int(random(3, 6)) 
        radius = cell_w / (n_grid + 1) * random(0.1, 0.3) if cell_w < cell_h else cell_h / (n_grid + 1) * random(0.1, 0.3)
        
        for row in range(n_rows):
            for col in range(n_cols):
                section.cells.append(Cell(section.x + cell_w * col, section.y + cell_h * row, cell_w, cell_h, layout, scaling, n_grid, radius))
                
        # for cell in section.cells:
        #     cell.partitions.append(Partition(cell.x, cell.y, cell.w, cell.h))
        

def render():
    noFill()
    for section in sections:
        stroke(0)
        strokeWeight(2)
        fill(random(255), random(255), random(255), 100)
        rect(section.x, section.y, section.w, section.h)
        
        for cell in section.cells:
            stroke(255, 0, 0)
            strokeWeight(1)
            noFill()
            rect(cell.x, cell.y, cell.w, cell.h)
            cell.pegs.render()
