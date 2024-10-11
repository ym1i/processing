from random import randint
from peg import Peg
from wrapper import Wrapper


class Element():
    
    def __init__(self, palette):
        self.pegs = []
        self.side_1 = []
        self.side_2 = []
        self.palette = palette
        
        
    def add_peg(self, v, r):
        self.pegs.append(Peg(v.x, v.y, r))
        
    
    def render(self):
        self.wrapping.render(self.palette.random_color(), sw=3, no_stroke=False)
        
        for peg in self.pegs:
            peg.render(self.palette.random_color())
        for peg in self.side_1:
            peg.render(self.palette.random_color())
        for peg in self.side_2:
            peg.render(self.palette.random_color())
            
        self.pegs[0].render(color(0))
        
        fill(0)
        text('[P: {}]'.format(self.palette.name), 15, height - 15)
    
                
    
    def enbody(self, amp):
        for i, v in enumerate(self.pegs):
            if v == self.pegs[-1] or v == self.pegs[0]:
                continue
            else:
                next = self.pegs[i + 1]
            a = PVector.sub(next.center, v.center).heading()
            peg_r = 20 
            self.side_1.append(Peg(v.x + amp * cos(a - HALF_PI), v.y + amp * sin(a - HALF_PI), peg_r))
            self.side_2.append(Peg(v.x + amp * cos(a + HALF_PI), v.y + amp * sin(a + HALF_PI), peg_r))
            
        
    def wrap(self):
        self.wrapping = Wrapper() 
        pegs_to_wrap = []
    
        for peg in self.side_1:
            pegs_to_wrap.append(peg)
           
        pegs_to_wrap.append(self.pegs[-1])
        
        for peg in reversed(self.side_2):
           pegs_to_wrap.append(peg)
           
        pegs_to_wrap.append(self.pegs[0])
        
        self.wrapping.ameba_wrap(pegs_to_wrap) 
            
    
    def check_collision(self, x, y):
        vertices = self.wrapping.vertices
        n_verts = len(vertices)
        c = False
        j = n_verts - 1
        
        for i  in range(n_verts):
            delta_x = vertices[j].x - vertices[i].x
            delta_y = vertices[j].y - vertices[i].y
            y_spread = y - vertices[i].y
            
            if (vertices[i].y > y) != (vertices[j].y > y) and x < (delta_x * y_spread / delta_y) + vertices[i].x:
                c = False if c else True
                
            j = i
        return c
           
