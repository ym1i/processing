import time
from random import randint
from peg import Peg
from element import Element
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    el.wrap()
    el.render()

    
def init():
    global pegs, n_cols, n_rows, el, palette
    palette = Palette()
    n_cols = 3
    n_rows = 3
    pegs = make_grid(n_cols, n_rows)
    pegs_to_wrap = select_pegs_to_wrap()
    print 'pegs2wrap | ', pegs_to_wrap
    
    el = Element(pegs, pegs_to_wrap, n_cols, n_rows, palette)
    
    
def make_grid(n_cols, n_rows):
    global grid_width
    pegs = []
    margin = 300
    grid_width = (width - margin) / (n_cols + 1)
    grid_height = (height - margin) / (n_rows + 1)
    # rand = random(0.3, 0.4)
    rand = 0.4
    r = grid_width * rand
    ratio = 1.5
    n_scale = grid_width / ratio 
    # resolution = 0.8
    resolution = 0.2    # 0.005-0.03    
    
    fill(0)
    text('[ GRID_WIDTH: {} | N_SCALE: grid_width / {} ({:.1f})  |  RESOLUTION: {}  |  R: {:.1f}  |  PALETTE: {} | TIME: {}]'.format(grid_width, ratio, n_scale, resolution, rand, palette.name, time.time()), 15, height - 15)
        
    for j in range(1, n_rows + 1):                
        for i in range(1, n_cols + 1):
            n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
            pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            
    return pegs


def select_pegs_to_wrap():
    pegs_to_wrap = []
    n = (n_cols * n_rows) - 2
    visited = []
    current = randint(0, n - 1)
    pegs_to_wrap.append(current)
    visited.append(current)
    
    for i in range(n):
        next, visited, complete = pick_neighbor(current, visited, n)
        if not complete:
            break
        pegs_to_wrap.append(next)
        current = next
    
    if len(pegs_to_wrap) == 1:
        pegs_to_wrap.append((current + 1) % n)
    
    return pegs_to_wrap
    
    
def pick_neighbor(current, visited, n_pegs):
    count = 0
    while count < 9999:
        r = random(0, 1)
        if r < 0.125:
            next = current - n_cols - 1
        elif r < 0.25:
            next = current - n_cols
        elif r < 0.375:
            next = current - n_cols + 1
        elif r < 0.5:
            next = current - 1
        elif r < 0.625:
            next = current + 1
        elif r < 0.75:
            next = current + n_cols - 1
        elif r < 0.875:
            next = current + n_cols
        else:
            next = current + n_cols + 1
            
        next %= n_pegs
        
        d = PVector.dist(pegs[current].vec, pegs[next].vec)
        if d < grid_width * sqrt(2) + 2 and next not in visited:
            break
        count += 1
    
    if count == 9999:
        return next, visited, False
    else:
        visited.append(next)
        return next, visited, True

                
    
