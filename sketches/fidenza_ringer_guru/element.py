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
        self.wrapping.render(self.palette.random_color(), sw=3, no_fill=False, no_stroke=False)
        
    
        for outer_wrapping in self.outer_wrappings:
            outer_wrapping.render(self.palette.random_color(), sw=1, no_fill=True, no_stroke=False)
    
        for peg in self.pegs:
            peg.render(self.palette.random_color())
        for i, peg in enumerate(self.side_1):
            if i % 2 == 1:
                peg.render(self.palette.random_color())
        for peg in self.side_2:
            peg.render(self.palette.random_color())
            
        self.pegs[0].render(color(0))
        
        # fill(0)
        # text('[P: {}]'.format(self.palette.name), 15, height - 15)
    
                
    
    def enbody(self, amp):
        for i, v in enumerate(self.pegs):
            if v == self.pegs[-1] or v == self.pegs[0]:
                continue
            else:
                next = self.pegs[i + 1]
            a = PVector.sub(next.center, v.center).heading()
            peg_r = 30 
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
        
    
    def outer_wrap(self):
        self.outer_wrappings = []
        n = 10
        padding = 8
        for i in range(n):
            # padding = randint(3, 8)
            self.outer_wrappings.append(Wrapper())
            # self.outer_wrappings[i].wrap(self.wrapping.vertices, padding * (i + 1))
            self.outer_wrappings[i].wrap(self.wrapping.vertices, padding * (n - i))
            
