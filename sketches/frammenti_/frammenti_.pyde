from frammenti import Frammenti
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    
    
def draw():
    for i in range(6):
        frammenti.split()
    frammenti.render()
    noFill()
    rect(200, 200, 400, 400)


def init():
    global frammenti
    
    palette = Palette()
    types = ['rect', 'circle', 'triangle', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'decagon']
    decay = ['no', 'low', 'mid', 'high']
    frammenti = Frammenti(200, 200, 400, 400, types[1], decay[0], palette) 
    
