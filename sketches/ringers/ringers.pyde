from peg_system import PegSystem


def setup():
    size(800, 800)
    background(255)
    noLoop()
    
    init()
    

def draw():
    pegs.render()


def init():
    global pegs
    layout = 'grid_3'
    radius = 30
    style = 'bulls_2'
    pegs = PegSystem(layout, style, radius)  
    pegs.set_layout()
    pegs.wrap()
    
