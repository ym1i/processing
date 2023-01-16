# P_4_1_2_01

import datetime


def setup():
    global img
    size(1024, 780)
    background(255)
    img = loadImage('data/klimt.jpeg')
    image(img, 0, 100)
    
    
def draw():
    x1 = int(random(0, width))
    y1 = 0
    x2 = round(x1 + random(-7, 7))
    y2 = int(random(-5, 5))
    w = int(random(10, 40))
    h = height - 100
    set(x2, y2, get(x1, y1, w, h))
    

def keyReleased():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
    if key == DELETE or key == BACKSPACE:
        clear()
        image(img, 0, 100)
