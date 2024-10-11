from random import randint

from deformed_circle import DeformedCircle, double_circle
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    render()


def init():
    global circle_1, circle_2, circle_3, circles, palette
    
    palette = Palette()
    while len(palette.colors) < 3:
        palette = Palette()

    r1 = 100
    r2 = 200
    r3 = 300
    n_points = 80

    circle_1 = DeformedCircle(400, 400, r1, palette.random_color(), r1 , n_points)
    circle_2 = DeformedCircle(400, 400, r2, palette.random_color(), r2, n_points)
    circle_3 = DeformedCircle(400, 400, r3, palette.random_color(), r3, n_points)
    circle_1.set_vertices()
    circle_2.set_vertices() 
    circle_3.set_vertices() 
    
    circles = []
    n = 10
    center = PVector(width / 2, height / 2)
    for i in range(n):
        r = map(i, 0, n - 1, 300, 50)
        c = DeformedCircle(center.x, center.y, r, palette.random_color(), r / 2 , n_points)
        c.set_vertices()
        circles.append(c)
    

def render():
    for i, c in enumerate(circles):
        if random(1) < 0.5:
            # double_circle(circles[i], circles[i - 1], palette)
            double_circle(circles[i], circles[i - 1], palette)
        else:
            circles[i].render()
        # c.render()
    # double_circle(circle_3, circle_2, palette)
    # double_circle(circle_2, circle_1, palette)
