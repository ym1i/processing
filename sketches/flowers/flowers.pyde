from flower import Flower
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
    flower.render()
    
    
def init():
    global flower
    plt = Palette()
    colors = []
    for i in range(100):
        colors.append(plt.random_color())
        
    flower = Flower(plt)
    
    
def keyPressed():
    filename = 'images/clecle_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
