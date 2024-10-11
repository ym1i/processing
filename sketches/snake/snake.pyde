from shape import Shape
from shape_j import ShapeJ
from shape_jj import ShapeJJ
from shape_7 import Shape7
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
    strokeWeight(2)
    # noStroke()
    jj4.render()
    jj3.render()
    jj2.render()
    jj1.render()
    # u4.render()
    # u3.render()
    # u2.render()
    # u1.render()
    j4.render()
    j3.render()
    j2.render()
    j1.render()
    element.render()
    # element2.render()
    
    
def init():
    global element, element2, j1, j2, j3, j4, jj1, jj2, jj3, jj4, u1, u2, u3, u4
    
    palette = Palette()
    start_pos = PVector(140, 100)
    w = 50
    element = Shape(start_pos, w, palette)
    element2 = Shape(start_pos.copy().add(PVector(-w, 300)), w, palette)
    j1 = ShapeJ(start_pos.copy().add(PVector(-w, 0)), w, palette)
    j2 = ShapeJ(start_pos.copy().add(PVector(2 * w, 100)), w, palette)
    j3 = ShapeJ(start_pos.copy().add(PVector(5 * w, 200)), w, palette)
    j4 = ShapeJ(start_pos.copy().add(PVector(8 * w, 300)), w, palette)
    jj1 = ShapeJJ(start_pos.copy().add(PVector(-2 * w, 0)), w, palette)
    jj2 = ShapeJJ(start_pos.copy().add(PVector(1 * w, 100)), w, palette)
    jj3 = ShapeJJ(start_pos.copy().add(PVector(4 * w, 200)), w, palette)
    jj4 = ShapeJJ(start_pos.copy().add(PVector(7 * w, 300)), w, palette)
    u1 = Shape7(start_pos.copy().add(PVector(0, 100)), w, palette)
    u2 = Shape7(start_pos.copy().add(PVector(3 * w, 200)), w, palette)
    u3 = Shape7(start_pos.copy().add(PVector(6 * w, 300)), w, palette)
    u4 = Shape7(start_pos.copy().add(PVector(9 * w, 400)), w, palette)
    
def keyPressed():
    filename = 'images/eddifice_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
