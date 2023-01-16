# 8.3 The Cantor Set with a Recursive Function | Nature Of Code
# https://natureofcode.com/book/chapter-8-fractals/
# __________________________________________________________________________________________________

from cantor import Cantor


def setup():
    global cantor_lines, last_generation
    
    size(600, 600)
    background(255)
    
    start = PVector(100, 100)
    end = PVector(500, 100)
    cantor_lines = []
    cantor_lines.append(Cantor(start, end, 10, 20))
    
    last_generation = []
    last_generation.append(cantor_lines[0])
    
    generate()
    
    
    for c in cantor_lines:
        c.display()
    

def generate():
    global cantor_lines, last_generation
    
    while True:
        next = []
        for l in last_generation:
            print l
            vertise = l.generate()
            next_1 = Cantor(vertise[0], vertise[1], 10, 20)
            next_2 = Cantor(vertise[2], vertise[3], 10, 20)
            next.append(next_1)
            next.append(next_2)
            cantor_lines.append(next_1)
            cantor_lines.append(next_2)
    
        last_generation = next
        if last_generation[0].len < last_generation[0].min_len:
            break
    
    
