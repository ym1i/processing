# 8.4 The Koch Curve and the ArrayList Technique | Nature Of Code
# https://natureofcode.com/book/chapter-8-fractals/
# __________________________________________________________________________________________________

from koch_line import KochLine


def setup():
    global koch_lines
    
    size(600, 300)
    background(255)
    
    koch_lines = []
    start = PVector(0, 200)
    end = PVector(width, 200)
    koch_lines.append(KochLine(start, end))
    
    for i in range(2):
        generate()
    
    
    for koch in koch_lines:
        koch.display()
    

def generate():
    global koch_lines
    
    next = []
    
    for koch_line in koch_lines:
        a = koch_line.koch_a()
        b = koch_line.koch_b()
        c = koch_line.koch_c()
        d = koch_line.koch_d()
        e = koch_line.koch_e()
        
        next.append(KochLine(a, b))
        next.append(KochLine(b, c))
        next.append(KochLine(c, d))
        next.append(KochLine(d, e))
        
    koch_lines = next
