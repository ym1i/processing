from circle import Circle
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    init()
    
    
def draw():
    background(255)
    for obj in objs:
        obj.update()
    render()
    # saveFrame('frames/######.png')


def render():
    for obj in objs:
        obj.render()
    
    strokeWeight(1)
    for i, obj in enumerate(objs):
        if obj != objs[-1]:
            # noFill()
            beginShape(QUAD_STRIP)
            for j, v in enumerate(obj.verts):
                fill(colors[j])
                vertex(v.x, v.y)
                vertex(objs[i+1].verts[j].x, objs[i+1].verts[j].y)
            vertex(objs[i].verts[0].x, objs[i].verts[0].y)
            vertex(objs[i+1].verts[0].x, objs[i+1].verts[0].y)
            endShape(CLOSE)  
    
    
def init():
    global objs, plt, colors
    
    plt = Palette()
    colors = []
    for i in range(100):
        colors.append(plt.random_color())
    
    pos = PVector(400, 400)
    objs = []
    objs.append(Circle(pos=pos, r=250, rand=False ,plt=plt))
    objs.append(Circle(pos=pos, r=200, rand=False ,plt=plt))
    objs.append(Circle(pos=pos, r=150, rand=False ,plt=plt))
    objs.append(Circle(pos=pos, r=100, rand=False ,plt=plt))
    objs.append(Circle(pos=pos, r=50, rand=False ,plt=plt))    
        
    
def keyPressed():
    filename = 'images/eddifice_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
