from truchet import Truchet
from splitter import Splitter
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    
def draw():
    render()
    
def init():
    global splitter, palette
    # palette = Palette()
    splitter = Splitter(100, 100, 600, 600)
    splitter.split()
    splitter.move()
    
def render():
    splitter.render()
    
