from splitter import Splitter


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    
def draw():
    render()
    
def init():
    global splitter, splitters , small

    radius = 300
    # splitter = Splitter(width / 2, height / 2, radius)
    # small = Splitter(splitter.pivots[0].x, splitter.pivots[0].y, splitter.rad * 0.9)

    
    splitters = []
    for i in range(9):
        for j in range(9):
            x = map(i, 0, 8, 100, 700)
            y = map(j, 0, 8, 100, 700)
            r = 30
            splitters.append(Splitter(x, y, r))  
    
    # x = width / 2
    # y = height / 2
    # for i in range(2):
    #     r = map(i, 0, 1, 300, 130)
    #     splitters.append(Splitter(x, y, r))    
    
def render():
    # splitter.render()
    # small1.render()
    for splitter in splitters:
        splitter.render()
    
