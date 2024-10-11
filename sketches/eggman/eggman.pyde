from egg import Egg


def setup():
    size(800, 800)
    background(255)
    init()
    
    
def draw():
    background(255)
    egg.move()
    # noLoop()
    render()
    
    
def init():
    global egg
    r = 150
    egg = Egg(0.5 * width, 0.5 * height, r)
    egg.crack() 
    # egg.static_move()  
    
def render():
    egg.render()
    
def keyPressed():
    filename = 'images/eggman_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
