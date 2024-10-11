from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()


def draw():
       image(layer_1, 0, 0)
       image(layer_2, 0, 0)


def init():
    global layer_1, layer_2
    palette = Palette()
    radius = 30
    orientation = 0
    
    layer_1 = createGraphics(800, 800)
    layer_2 = createGraphics(800, 800)
    mask = createGraphics(800, 800)
    dot_layout(layer_1, radius, orientation, palette.colors[0], palette.white)
    dot_layout(layer_2, radius, orientation, palette.colors[1], palette.white)
    create_mask(mask)
    
    layer_2.mask(mask)
    

def dot_layout(base, radius, orientation, color, bg_color):
    base.beginDraw()
    base.background(bg_color)
    base.fill(color)
    base.noStroke()
    margin = 20
    offset = radius + margin / 2
    nx = width / (radius * 2 + margin)
    ny = height / (radius * 2 + margin)
    for j in range(int(ny)):
        for i in range(int(nx)):
            if j % 2 == 0:
                base.ellipse(i * (radius * 2 + margin) + offset, j * (radius * 2 + margin) + offset, radius * 2, radius * 2)
            else:
                base.ellipse(i * (radius * 2 + margin), j * (radius * 2 + margin) + offset, radius * 2, radius * 2)
    base.endDraw()


def create_mask(mask):
    mask.beginDraw()
    mask.beginShape()
    for i in range(400):
        x = map(i, 0, 400, 0, width)
        theta = map(i, 0, 400, 0, TWO_PI)
        mask.vertex(x, height / 2 + 50 * sin(theta))
    mask.vertex(width, height)
    mask.vertex(0, height)
    mask.vertex(0, height / 2)
    mask.endShape()
    mask.endDraw()
    
