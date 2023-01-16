# P_2_0_01
import datetime

def setup():
    size(550, 550)
    strokeCap(SQUARE)

def draw():
    background(255)
    translate(width / 2, height / 2)
    
    circle_resolution = int(map(mouseY, 0, height, 2, 80))
    radius = mouseX - width / 2
    angle = TWO_PI / circle_resolution
    
    strokeWeight(mouseY / 20)
    
    for i in range(circle_resolution):
        x = cos(angle * i) * radius
        y = sin(angle * i) * radius
        line(0, 0, x, y)
    
def keyPressed():
    if ((key == 's') or (key == 'S')):
        saveFrame('{}.png'.format(datetime.datetime.now()))
    
