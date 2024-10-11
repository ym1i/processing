from random import random, randint, shuffle
from peg import Peg
from palette import Palette


class Cover():
    
    def __init__(self, palette):
        self.vertices = []
        self.pegs = []
        self.palette = palette
        # self.palette = Palette()
        self.circles = []
        
        
    def add_peg(self, peg):
        self.pegs.append(peg)
    
    
    def add_vertex(self, v):
        self.vertices.append(v)
        
    
    def render(self):
        beginShape()
        
        fill(self.palette.random_color())
        for v in self.vertices:
            vertex(v.x, v.y)  
              
        endShape()
        
        beginShape(QUAD_STRIP)
        
        fill(self.palette.random_color())
        stroke(0)
        strokeWeight(2)
        w = 6 # string width
        for i, v in enumerate(self.vertices):
            fill(self.palette.random_color())
            if i == 0:
                theta = PVector.sub(v, self.vertices[-1]).heading()
                first_v1 = PVector(v.x + w * cos(theta - HALF_PI), v.y + w * sin(theta - HALF_PI))
                first_v2 = PVector(v.x + w * cos(theta + HALF_PI), v.y + w * sin(theta + HALF_PI))
            else:
                theta = PVector.sub(v, self.vertices[i - 1]).heading()
            v1 = PVector(v.x + w * cos(theta - HALF_PI), v.y + w * sin(theta - HALF_PI))
            v2 = PVector(v.x + w * cos(theta + HALF_PI), v.y + w * sin(theta + HALF_PI))
            
            vertex(v1.x, v1.y)
            vertex(v2.x, v2.y)
        
        vertex(first_v1.x, first_v1.y)
        vertex(first_v2.x, first_v2.y)
        
        endShape()
        
        # ---- IF draw body AFTER string, it looks interesting ----
        # beginShape()
        # fill(self.palette.random_color())
        # stroke(0)
        # strokeWeight(3)
        # for v in self.vertices:
        #     vertex(v.x, v.y)
        # endShape()
        


            
    
    
    
