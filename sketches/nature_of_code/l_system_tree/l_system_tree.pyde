# Nature Of Code
# 8.6 L-systems
# https://natureofcode.com/book/chapter-8-fractals/
# --------------------------------------------------------------------------------------------------

from l_system import LSystem
from rule import Rule
from tree import Tree
from turtle import Turtle


def setup():
    global tree, l_system
    size(600, 600)
    background(255)
    
    axiom = 'A'
    ruleset = []
    ruleset.append(Rule('A', 'F-[[A]+A]+F[+FA]-A'))
    ruleset.append(Rule('F', 'FF'))
    l_system = LSystem(axiom, ruleset)
    tree = Tree(l_system.sentence, 1, radians(22.5))
    
    for i in range(8):
        l_system.generate()
        tree.command = l_system.sentence
        
    
    # Random Mode -------------------------------------------------
    # Rule has multiple successors which will be selected at random
    # Pass list as the 2nd param of Rule
    # Use different L-System generator (generator_random()) 
    
    # axiom = 'A'
    # ruleset = []
    # ruleset.append(Rule('A', ['F-[[A]+A]+F[+FA]-A', 'F[+A]F[-A]A', 'F[+[FA[-A]F]][-A]FA']))
    # ruleset.append(Rule('F', ['FF']))
    # l_system = LSystem(axiom, ruleset)
    # tree = Tree(l_system.sentence, 4, radians(22.5))
    

def draw():
    translate(width / 2, height)
    rotate(PI)
    noLoop()
    
    for i in range(2):
        pushMatrix()
        tree.render()
        popMatrix()

def mousePressed():
    global tree
    l_system.generate()
    tree.command = l_system.sentence
    redraw()
