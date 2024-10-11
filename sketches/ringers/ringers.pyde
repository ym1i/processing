import datetime
from peg_system import PegSystem


def setup():
    size(800, 800)
    background(255)
    noLoop()
    
    init()
    

def draw():
    pegs.render()
    # saveFrame('{}.png'.format(datetime.datetime.now()))


def init():
    global pegs
    grid_layouts = ['grid_3', 'grid_4', 'grid_5', 'grid_6', 'grid_7', 'grid_8', 'grid_9', 'grid_10']
    tiled_layouts = ['tiled_23', 'tiled_32', 'tiled_34', 'tiled_43', 'tiled_45', 'tiled_54']
    recursive_layouts = ['recursive_2']
    scalings = ['uniform', 'bigger_near_center', 'smaller_near_center']
    colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194), color(211, 51, 59)]
    layout = grid_layouts[int(random(3))]
    
    pegs = PegSystem(layout, scalings[0], colors[4], colors[1], colors[0], colors[2])  
    pegs.set_layout()
    
    
