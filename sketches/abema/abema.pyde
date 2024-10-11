from random import randint
import datetime
from ameba import Ameba
# from super_ameba import SuperAmeba
from deformed_circle import DeformedCircle
# from frammenti import Frammenti
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()


def draw():
    element_1.render(palette.colors[0], palette.colors[2])
    if element_1.type == 'regular' or  element_1.type == 'large': 
        circle_1.render()
        circle_2.render()


def init():
    global element_1, element_2, circle_1, circle_2, circle_3, circle_4, palette
    
    palette = Palette()
    while len(palette.colors) < 3:
        palette = Palette()

    r1 = 100
    r2 = 60
    r3 = 240
    r4 = 100
    n_points = 100

    circle_1 = DeformedCircle(400, 400, r1, palette.random_color(), r1 , n_points)
    circle_2 = DeformedCircle(400, 400, r2, palette.colors[1], r2, n_points)
    circle_1.set_vertices()
    circle_2.set_vertices()

    r = 200
    n_pegs = randint(3, 40)
    types = ['regular', 'large', 'grid5', 'grid3', 'grid4', 'grid3mix', 'grid4mix']
    type = types[-1]
    if type == types[1]:
        n_pegs = n_pegs + 1 if n_pegs %2 == 1 and n_pegs != 3 else n_pegs
    r_peg = map(n_pegs, 3, 40, 30, 3)
    
    element_1 = Ameba(400, 400, r, r_peg, n_pegs, palette, type=type)
    element_1.birth()
    

def keyPressed():
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
    
    
        
