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
    scalings = ['uniform', 'bigger_near_center', 'smaller_near_center']
    colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194), color(211, 51, 59)]
    
    
    pegs = PegSystem(layouts[2], scalings[0], colors[2], colors[1], colors[0], colors[1])  
    pegs.set_layout()
    pegs.set_forces()
    for i in range(150):
        pegs.add_forces()
    
