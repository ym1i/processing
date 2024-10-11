from triangle import Triangle
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    divide()
    tile()
    bend()
    

def draw():
    for triangle in triangles:
        if triangle.divisions:
            for division in triangle.divisions:
                division.render()
                division.render_tile()
        else:
            triangle.render()
            triangle.render_tile()

def init():
    global triangles, dividing
    triangles = []
    DIVIDING_MODE = ['all', 'random', 'noise', 'center', 'edge']
    dividing = DIVIDING_MODE[2]
    side = 200
    n_strip = width / side
    range_y = height / side
    margin = (width - (0.5 * side * sqrt(3) * n_strip)) * 0.5
    x = 0 + margin
    y = 0
    offset = side * sqrt(3) / 2
    
    palette = Palette()
    primary_color = palette.colors[0]
    primary_shade_color = palette.colors[1]
    secondary_color = palette.white
    secondary_shade_color = palette.grey

    for i in range(n_strip):
        for j in range(range_y):
            if i % 2 == 0:
                triangles.append(Triangle(i * offset + x, y + j * side, side, 'right', primary_color, primary_shade_color, secondary_color, secondary_shade_color))
                triangles.append(Triangle(i * offset + x + offset, y + (0.5 * side) + (j * side), side, 'left', primary_color, primary_shade_color, secondary_color, secondary_shade_color))
            else:
                triangles.append(Triangle(i * offset + x + offset, y + (j * side), side, 'left', primary_color, primary_shade_color, secondary_color, secondary_shade_color))
                triangles.append(Triangle(x + i * offset, y  + (0.5 * side) + j * side, side, 'right', primary_color, primary_shade_color, secondary_color, secondary_shade_color))
                

def divide():
    center = PVector(width * 0.5, height * 0.5)
    for triangle in triangles:
        if dividing == 'all':
            triangle.divide()
        elif dividing == 'random':
            if random(1) < 0.5:
                triangle.divide()
        elif dividing == 'noise':
            if noise(triangle.center.x, triangle.center.y) < 0.5:
                triangle.divide()
        elif dividing == 'center':
            if PVector.dist(center, triangle.center) < width / 4:
                triangle.divide()
        elif dividing == 'edge':
            if PVector.dist(center, triangle.center) > width / 4:
                triangle.divide()


def tile():
    for triangle in triangles:
        if triangle.divisions:
            for division in triangle.divisions:
                division.tile()
        else:
            triangle.tile()
            

def bend():
    for triangle in triangles:
        if triangle.divisions:
            for division in triangle.divisions:
                r = random(1)
                if r < 0.07:
                    division.bend('left')
                elif r < 0.15:
                    division.bend('right')
        else:
            r = random(1)
            if r < 0.07:
                triangle.bend('left')
            elif r < 0.15:
                triangle.bend('right')        










        
        
                
