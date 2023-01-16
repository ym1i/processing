# 8.5 Tree | Nature of Code
# https://natureofcode.com/book/chapter-8-fractals/
# --------------------------------------------------------------------------------------------------

from branch import Branch


def setup():
    global branches
    size(600, 600)
    background(255)
    
    branches = []
    init()
    

def draw():
    global branches
    
    theta = - PI / 8
    
    for i in range(10):
        # theta *= 1.1
        for b in reversed(branches):
            if not b.has_branch:
                    branches.append(b.generate(theta))
                    branches.append(b.generate(PI - theta))
    
    for b in branches:
        b.render()
    noLoop()
    

def init():
    global branches
    
    start = PVector(width / 2, height)
    end = PVector(width / 2, height - 120)
    branches.append(Branch(start, end))
    
    
    
    
    
    
