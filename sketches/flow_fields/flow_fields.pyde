from vector_fields import VectorFields
from circle_packing import CirclePacking
from palette import Palette


def setup():
    size(1000, 1000)
    background(255)
    noLoop()
    init()
    

def draw():
    noFill()   
    for v in starting_positions:
        stroke(0)
        
        vector_fields.render_shape(v.x, v.y, 100, palette) 
        # vector_fields.render_line(v.x, v.y, 100)    
    
    # for c in cp.circles:
    #     c.render()
    
    # vector_fields.render_vector_fields()
     
    # for i in range(n_cols):
    #     render(i, n_rows / 2)       
    # for _ in range(3000):
    #     stroke(palette.random_color())
    #     render()
    
    
def init():
    global vector_fields, cp, starting_positions, palette

    grid_size = width / 100
    step_size = grid_size * 0.3
    vector_fields = VectorFields(width, height, grid_size, step_size)
    
    cp = CirclePacking(150, 20, 20, width, height)
    starting_positions = cp.get_starting_positions()
    
    palette = Palette()
    


    
