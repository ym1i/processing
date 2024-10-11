from random import randint
from vector_field import VectorField
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    # vf.render_grid()
    element.render()
    
    
def init():
    global vf, element

    grid_size = width / 80 
    step_size = grid_size * 20
    vf = VectorField(width, height, grid_size, step_size)
    vf.create_field(step_size)
    
    element_exists = False
    n_steps = 5
    amp = 180
    
    while not element_exists:
        x = random(50, width - 50)
        y = random(50, width - 50) 
        element = vf.create_element(x, y, n_steps)
        
        if element:
            element.enbody(amp)
            element.wrap()
            element.outer_wrap()
            element_exists = True
        
