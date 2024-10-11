from datetime import datetime
from chicken import Chicken
from palette import Palette


def setup():
    size(800, 800, P3D)
    background(250, 250, 250)
    noLoop()
    init()
    

def draw():
    ambientLight(50, 50, 50)
    lightSpecular(20, 20, 20)
    directionalLight(255, 255, 255, -1, 0.5, -1)
    directionalLight(255, 255, 255, 1, 0.5, -0.5)
    
    rotateX(radians(-30))
    rotateY(radians(30))
    
    chicken.render()
    
    saveFrame('{}.png'.format(datetime.now()))
    
    
def init():
    global chicken
    chicken = Chicken(width / 2, height / 6, -200, Palette())
    
    
