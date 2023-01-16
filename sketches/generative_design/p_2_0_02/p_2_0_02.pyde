# P_2_0_02

def setup():
    size(720, 720)
    noFill()
    background(255)
    strokeWeight(2)
    stroke(0, 25)
    
def draw():
    if (mousePressed and mouseButton == LEFT):
        push()
        translate(width / 2, height / 2)
        
        circle_resolution = int(map(mouseY + 100, 0, height, 2, 10))
        radius = mouseX - width / 2
        angle = TWO_PI / circle_resolution
        
        beginShape()
        for i in range(circle_resolution):
            x = cos(angle * 1) * radius
            y = sin(angle * 1) * radius
            vertex(x, y)
        endShape()
        
        pop()
        
def keyPressed():
    if (keyCode == 'DELETE' or keyCode == 'BACKSPACE'):
        background(255)
    if ((key == 's') or (key == 'S')):
        saveFrame('{}.png'.format(datetime.datetime.now()))
