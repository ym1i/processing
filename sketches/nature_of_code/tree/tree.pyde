# 8.5 Tree | Nature of Code
# https://natureofcode.com/book/chapter-8-fractals/
# --------------------------------------------------------------------------------------------------

from branch import Branch


def setup():
    global branches
    
    size(600, 600)
    background(255)
    
    branches = []
    start = PVector(width / 2, height)
    vel = PVector(0, -1)
    branches.append(Branch(start, vel, 100))
    
    
def draw():
    global branches
    
    for b in reversed(branches):  
        b.update()
        b.render()
        
        if b.timer_to_branch():
            if len(branches) < 1024:
                branches.append(b.generate(30))
                branches.append(b.generate(-25))
    
    
def _branch(len):
    sw = map(len, 2, 200, 1, 10)
    strokeWeight(sw)
    
    line(0, 0, 0, -len)
    translate(0, -len)
    
    len *= 0.66
    
    if len > 2:
        pushMatrix()
        rotate(theta)
        branch(len)
        popMatrix()
        
        pushMatrix()
        rotate(-theta)
        branch(len)
        popMatrix()
