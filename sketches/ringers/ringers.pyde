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
    layouts = ['grid_3', 'grid_4', 'grid_5', 'grid_6', 'tiled_23', 'tiled_32', 'tiled_34', 'tiled_43', 'tiled_45', 'tiled_54']
    radius = 30
    style = 'solid'
    pegs = PegSystem(layouts[7], style, radius)  
    pegs.set_layout()
    pegs.w_rap()
    
