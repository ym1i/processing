from peg import Peg
from triangle import Triangle
from layout import grid_layout
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    palette = Palette()
    for peg in pegs:
        peg.render(palette.random_color(), no_stroke=False, no_fill=True)
    for t in triangles:
        t.wrap()
        t.render(palette.random_color())
        

def init():
    global pegs, n_rows, n_cols, triangles    
    
    pegs = []
    n_cols = 10
    n_rows = 10
    margin = 200
    r = (width - margin) / (n_cols + 1) * 0.4
    vertices = grid_layout(width, height, n_cols, n_rows, margin)
    for v in vertices:
        pegs.append(Peg(v.x, v.y, r))
    triangles = wrap()
        

def wrap():
    triangles = []
    for j in range(n_rows):
        for i in range(n_cols):
            if i % 4 == 1 and j % 2 == 0 and j + 1 < n_rows and i in range(1, n_cols - 1):
                triangle = Triangle('up', pegs[0].r)
                triangle.add_vertices(pegs[(j * n_rows) + i].v)
                triangle.add_vertices(pegs[((j + 1) * n_rows) + (i + 1)].v)
                # triangle.add_vertices(pegs[((j + 1) * n_rows) + i].v)
                triangle.add_vertices(pegs[((j + 1) * n_rows) + (i - 1)].v)
                triangles.append(triangle)
            elif i % 4 == 3 and j % 2 == 1 and j - 1 >= 0 and i in range(1, n_cols - 1):
                triangle = Triangle('down', pegs[0].r)
                triangle.add_vertices(pegs[(j * n_rows) + i].v)
                triangle.add_vertices(pegs[((j - 1) * n_rows) + (i - 1)].v)
                # triangle.add_vertices(pegs[((j - 1) * n_rows) + i].v)
                triangle.add_vertices(pegs[((j - 1) * n_rows) + (i + 1)].v)
                triangles.append(triangle)
    
    return triangles
                
                
                
                
        
        

            


        

    
