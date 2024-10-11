import datetime
from peg_system import PegSystem


def setup():
    size(1000, 1000, P3D)
    background(255)
    noLoop()
    
    init()
    

def draw():
    translate(width/2, height/2, -width/2)
    rotateX(radians(-25))
    rotateY(radians(-45))
    ortho(-width, width, -height, height)
 
    ambientLight(10, 10, 10)
    lightSpecular(50, 0, 0)
    directionalLight(255, 255, 255, -1, 1, -1)

    
    pegs.render()
    
    t = datetime.datetime.now()
    saveFrame('{}{}_{}{}{}.png'.format(t.month, t.day, t.hour, t.minute, t.second))


def init():
    global pegs
    n_grid = 3
    colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194), color(211, 51, 59)]
    
    pegs = PegSystem(n_grid, colors[2], colors[1], colors[2], colors[1])  

    
    
