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
    colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194), color(211, 51, 59)]
    bg_colors = [color(255, 255, 255), color(248, 198, 54), color(45, 132, 194), color(211, 51, 59)]
    
    for section in sections:
        n_cols = int(random(1, section.w / 50))
        n_rows = int(random(1, section.h / 50))
        cell_w = section.w / n_cols
        cell_h = section.h / n_rows
        layout = layouts[int(random(len(layouts)))]
        # layout = layouts[0]
        scaling = scalings[0]
        n_grid = int(random(3, 6)) 
        radius = cell_w / (n_grid + 1) * random(0.1, 0.3) if cell_w < cell_h else cell_h / (n_grid + 1) * random(0.1, 0.3)
        body = colors[int(random(5))]
        bg = bg_colors[int(random(4))]
        
        for row in range(n_rows):
            for col in range(n_cols):
                section.cells.append(Cell(section.x + cell_w * col, section.y + cell_h * row, cell_w, cell_h, layout, scaling, n_grid, radius, body, bg))
        

def render():
    noFill()
    for section in sections:
        for cell in section.cells:
            cell.render()
            cell.pegs.render()
