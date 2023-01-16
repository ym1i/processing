# Nature Of Code
# 8.6 L-systems
# https://natureofcode.com/book/chapter-8-fractals/
# --------------------------------------------------------------------------------------------------

from l_system import LSystem
from rule import Rule
from koch import Koch


def setup():
    global koch, l_system
    size(1000, 1000)
    background(255)
    
    axiom = 'F'
    ruleset = []
    ruleset.append(Rule('F', 'F-F+F+FF-F-F+F'))
    
    # Koch ----
    # axiom = 'F'
    # ruleset = []
    # ruleset.append(Rule('F', 'F+F--F+F'))
    
    l_system = LSystem(axiom, ruleset)

    for i in range(1):
        l_system.generate()
    koch = Koch(l_system.sentence, 20, radians(90))
    


def draw():
    translate(150, height / 4)
    # rotate(PI)
    noLoop()
    
    koch.render()
    

def mousePressed():
    global koch
    l_system.generate()
    koch.command = l_system.sentence
    redraw()
