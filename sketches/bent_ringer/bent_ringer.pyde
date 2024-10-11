from peg import Peg
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    for peg in pegs:
        peg.open_circle(palette.random_color())
        peg.render(palette.random_color())
    wrap()
        

def init():
    global pegs, palette, n_cols, n_rows
    palette = Palette()
    n_cols = 9
    n_rows = 9
    pegs = grid_layout(n_cols, n_rows)
    

def wrap():
    for i, peg in enumerate(pegs):
        row = i / n_cols
        noFill()
        stroke(0)
        strokeWeight(1)
        beginShape()
        if peg.side == 'left' and i % n_cols != n_cols - 1:
            next = pegs[i + 1]
            start = PI + QUARTER_PI
            mid_1 = PVector.sub(next.v, peg.v).heading()
            mid_2 = PVector.sub(peg.v, next.v).heading()
            stop = QUARTER_PI
            
            mid_1 = mid_1 + TAU if mid_1 < start else mid_1
            stop = stop - TAU if stop > mid_2 else stop
            
            r = PVector.sub(next.v, peg.v).mag() / 2
            
            for i in range(20):
                a = map(i, 0, 19, start, mid_1)
                vertex(peg.x + r * cos(a), peg.y + r * sin(a))
            
            for i in range(20):
                a = map(i, 0, 19, mid_2, stop)
                vertex(next.x + r * cos(a), next.y + r * sin(a))
        endShape()
            
            


def grid_layout(n_cols, n_rows):
        pegs = []
        margin = 200
        grid_width = (width - margin) / (n_cols + 1)
        grid_height = (height - margin) / (n_rows + 1)
        r = grid_width * 0.4
        ratio = 1
        n_scale = grid_width / ratio 
        resolution = 0.08
        
        for j in range(1, n_rows + 1):                
            for i in range(1, n_cols + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                n = 0
                if j % 2 == 0:
                    if i % 2 == 0:
                        pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r, 'left'))
                    else:
                        pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r, 'right'))
                else:
                    if i % 2 == 1:
                        pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r, 'left'))
                    else:
                        pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r, 'right'))
        return pegs
    
