from element import Element
from so_much_pain import SoMuchPain
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    smp.render()
    # element.random_pegs()
    # element.render()
    
    
def init():
    global element, smp
    palette = Palette()
    smp = SoMuchPain(palette)
    # element = Element('grid', color(0), palette)
    
    
