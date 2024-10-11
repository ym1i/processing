from heart import Heart
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    init()
    
    
def draw():
    background(255)
    noLoop()
    render()
    # saveFrame('frames/######.png')


def render():
    heart.render()
    
    
def init():
    global heart
    
    plt = Palette()
    heart = Heart(plt)
        
    
def keyPressed():
    filename = 'images/eddifice_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
