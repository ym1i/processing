from random import randint
from vector_field import VectorField
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    

def draw():
    # vf.render_grid()
    for element in elements:
        element.render()
    
    
def init():
    global vf, elements

    elements = []
    grid_size = width / 80 
    step_size = grid_size * 6
    vf = VectorField(width, height, grid_size, step_size)
    vf.create_field(step_size)
    
    count = 0
    n = 3
    for i in range(n):
        print 'i: {} -------------------------------------------'.format(i)
        element_exists = False
        n_steps = 5
        amp = 60
        # text('[N: {} | amp: {}]'.format(n, amp), 200, height - 15)
        while not element_exists:
            
            x = random(100, width - 100)
            y = random(100, width - 100) 
            new_element = vf.create_element(x, y, n_steps)
            count += 1
            if count % 20 == 0:
                n_steps -= 1
                amp -= 1
                if n_steps < 3:
                    n_steps += 3
                if amp < 20:
                    amp += 10
                print 'n_steps => : {}'.format(n_steps)
                print 'amp => : {}'.format(amp)
            if new_element:
                if len(elements) > 0:
                    element_exists = True
                    new_element.enbody(amp)
                    for j in range(i):
                        for peg in new_element.pegs:
                            if elements[j].check_collision(peg.x, peg.y):
                                element_exists = False
                        for peg in new_element.side_1:
                            if elements[j].check_collision(peg.x, peg.y):
                                element_exists = False
                        for peg in new_element.side_2:
                            if elements[j].check_collision(peg.x, peg.y):
                                element_exists = False
                    if element_exists:
                        new_element.wrap()
                        elements.append(new_element)
                else:
                    new_element.enbody(amp)
                    new_element.wrap()
                    elements.append(new_element)
                    element_exists = True
    
