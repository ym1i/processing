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
    styles = ['solid', 'bulls_1', 'bulls_2', 'bulls_3']
    scalings = ['uniform', 'bigger_near_center', 'smaller_near_center']
    pegs = PegSystem(layouts[7], styles[0], scalings[1])  
    pegs.set_layout()
    pegs.wrap()
    
