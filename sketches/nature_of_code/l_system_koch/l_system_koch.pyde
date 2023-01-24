# Nature Of Code
# 8.6 L-systems
# https://natureofcode.com/book/chapter-8-fractals/
# --------------------------------------------------------------------------------------------------

from l_system import LSystem
from rule import Rule
from renderer import Renderer


def setup():
    global l_system, renderer
    size(1000, 1000)
    background(255)
    
    cantor()
    

def koch():
    global l_system, renderer
    axiom = 'F'
    ruleset = []
    ruleset.append(Rule('F', 'F+F--F+F'))
    l_system = LSystem(axiom, ruleset)
    l_system.generate()
    renderer = Renderer(l_system.sentence, 2, radians(60))
    
    
def snow_flake():
    global l_system, renderer
    axiom = 'F++F++F'
    ruleset = []
    ruleset.append(Rule('F', 'F-F++F-F'))
    l_system = LSystem(axiom, ruleset)
    l_system.generate()
    renderer = Renderer(l_system.sentence, 2, radians(60))
    
    
def l_square():
    global l_system, renderer
    axiom = 'F-F-F-F'
    ruleset = []
    # ruleset.append(Rule('F', 'F-F+F+FF-F-F+F'))
    # ruleset.append(Rule('F', 'FF-F-F-F-F-F+F'))
    ruleset.append(Rule('F', 'FF-F-F-F-FF'))
    # ruleset.append(Rule('F', 'FF-F+F-F-FF'))
    # ruleset.append(Rule('F', 'FF-F--F-F'))
    # ruleset.append(Rule('F', 'F-FF--F-F'))
    # ruleset.append(Rule('F', 'F-F+F-F-F'))
    l_system = LSystem(axiom, ruleset)
    l_system.generate()
    renderer = Renderer(l_system.sentence, 3, radians(90))
    

def cantor():
    global l_system, renderer
    # axiom = 'FfF'
    axiom = 'F+F+F+F'
    ruleset = []
    # ruleset.append(Rule('F', 'FfF'))
    # ruleset.append(Rule('f', 'fff'))
    ruleset.append(Rule('F', 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF'))
    ruleset.append(Rule('f', 'ffffff'))
    l_system = LSystem(axiom, ruleset)
    l_system.generate()
    renderer = Renderer(l_system.sentence, 2, radians(90))
    

def draw():
    translate(width * 0.5, height * 0.5)
    # rotate(PI)
    noLoop()
    renderer.render()
    

def mousePressed():
    global renderer
    l_system.generate()
    renderer.command = l_system.sentence
    redraw()
