
# Substrate Watercolor
# http://www.complexification.net/gallery/machines/substrate/index.php
# --------------------------------------------------------------------------------------------

import Crack
import SandPainter

def setup():
    pprint('setup()')
    global crack_grid, cracks, dim_x, dim_y, num, max_num, good_color, sands
    crack_grid = []
    cracks = []
    dim_x = 400
    dim_y = 400
    num = 0
    max_num = 200 
    good_color = []
    sands = []
    
    size(400, 400)
    background(255)
    
    begin()
    
    
def draw():
    pprint('draw()')
    for n in range(num):
        cracks[n].move()
        
        
def mousePressed():
    begin()
    
  
def begin():
    pprint('begin()')
    global num, crack_grid
    
    for y in range(dim_y):
        for x in range(dim_x):
            crack_grid.append(10001)
            
    for k in range(16):
        i = int(random(dim_x * dim_y - 1))
        crack_grid[i] = int(random(360))
        
    num = 0
    for k in range(3):
        make_crack()
        
    background(255)
    

def make_crack():
    pprint('make_crack()')
    global cracks, num
    
    if num < max_num:
        cracks.append(Crack.Crack(dim_x, dim_y, crack_grid, make_crack))
        num += 1
        print 'num: ', num


def pprint(arg):
    print '> {} | main.py'.format(arg)
        
       
