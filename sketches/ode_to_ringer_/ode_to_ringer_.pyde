from ode_to_ringer import OdeToRinger
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    otr.render()
    # smp.render()
    # element.random_pegs()
    # element.render()
    
    
def init():
    global otr
    palette = Palette()
    otr = OdeToRinger(palette)
    # smp = SoMuchPain(palette)
    # element = Element('grid', color(0), palette)
