import datetime
from section import Section
from cell import Cell
from partition import Partition
from palette import Palette


def setup():
    size(800, 800, P3D)
    background(255)
    noLoop()
    
    init()
    
    
def draw():
    # rotateX(radians(-25))
    # rotateY(radians(-45))
    ambientLight(10, 10, 10)
    lightSpecular(50, 0, 0)
    directionalLight(255, 255, 255, 0, 1, -1)
    render()
    saveFrame('{}.png'.format(datetime.datetime.now()))
    

def init():
    global sections, strategy, palette
    
    sections = [Section(100, 100, width - 200, height - 200)]
    palette = Palette()
    strategies = ['single', 'main', 'group', 'random']
    strategy = strategies[3]
    
    make_sections(4, 4)
    make_cells()
    
    
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
    

def render():
    for section in sections:
        col = palette.colors[int(random(len(palette.colors)))]
        # r = random(3, 5)
        r = 3
        for cell in section.cells:  
            rand = random(1)      
            if rand < 0.5:
                tube(cell.x, cell.y, cell.w, cell.h, r, col)
            else:
                stroke(255)
                rect(cell.x, cell.y, cell.w, cell.h)   
            # else:
            #     stroke(0)
            #     noFill()
            #     rect(cell.x, cell.y, cell.w, cell.h)
                # tube_line(cell.x, cell.y + cell.h / 2, cell.w, cell.h, 1, col)
                    
                      
        
        
def tube(x, y, w, h, r, col):
    fill(col)
    for i in range(int(w)):
        pushMatrix()
        noStroke()
        translate(x + i, y, 0)
        sphere(r)
        popMatrix()
    for j in range(int(h)):
        pushMatrix()
        noStroke()
        translate(x, y + j, 0)
        sphere(r)
        popMatrix()
    for i in range(int(w)):
        pushMatrix()
        noStroke()
        translate(x + i, y + h, 0)
        sphere(r)
        popMatrix()
    for j in range(int(h)):
        pushMatrix()
        noStroke()
        translate(x + w, y + j, 0)
        sphere(r)
        popMatrix()
        
def tube_line(x, y, w, h, r, col):
    fill(col)
    for i in range(int(w)):
        pushMatrix()
        noStroke()
        translate(x + i, y, 0)
        sphere(r)
        popMatrix()
        
    

    
    
    
    
    
    
    
    
    
    
    
