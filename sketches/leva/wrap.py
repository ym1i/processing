from random import random, randint, shuffle
from peg import Peg


class Wrap():
    
    def __init__(self, palette):
        self.vertices = []
        self.palette = palette
    
    
    def add_vertex(self, v):
        self.vertices.append(v)
        
    
    def render(self, no_fill, ribon, fill_color):
    
        beginShape()
        strokeWeight(2)
        
        if no_fill:
            noFill()
        else:
            fill(fill_color)    
            # fill(self.palette.random_color())
            
        for v in self.vertices:
            vertex(v.x, v.y)
            
        endShape()
        
        if ribon:
            beginShape(QUAD_STRIP)
            
            fill(self.palette.random_color())
            stroke(0)
            strokeWeight(2)
            w = 20 # string width
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
        
        # self.add_circles(100)
        # for peg in self.circles:
        #     peg.render(self.palette.random_color(), self.palette.random_color)
        
       
    # def add_circles(self, n):
    #     n_circles = n
    #     count = 0
    #     trial = 0 
        
    #     for peg in self.pegs:
    #         self.circles.append(peg)
        
    #     while count < n_circles:
    #         if trial > 1000:
    #             break
    #         # if trial > 1000:
    #         #     r  = randint(3, 10)
    #         # else:
    #         #     r = randint(3, 80)
    #         t = int(trial / 10)
    #         r = randint(3, 105 - t)
    #         x = randint(r, width - r)
    #         y = randint(r, height - r)
    #         c = True
    #         intersect = False
            
    #         # check intersection
    #         for circle in self.circles:
    #             if dist(circle.x, circle.y, x, y) < circle.r + r:
    #                 intersect = True
    #                 continue
    #         if intersect:
    #             trial += 1
    #             continue
            
    #         for i in range(16):
    #             theta =  map(i, 0, 15, 0, TWO_PI)
    #             _x = x + r * cos(theta)
    #             _y = y + r * sin(theta)
                
    #             if not self.circle_packing(_x, _y):
    #                 c = False
    #         if c:
    #             self.circles.append(Peg(x, y, r, 'style'))
    #             trial = 0
    #             count += 1
    #         else:
    #             trial += 1
        
    #     print 'count: ', count
                
    
    # def circle_packing(self, x, y):
    #     n_verts = len(self.vertices)
    #     c = False
    #     j = n_verts - 1
        
    #     for i  in range(n_verts):
    #         delta_x = self.vertices[j].x - self.vertices[i].x
    #         delta_y = self.vertices[j].y - self.vertices[i].y
    #         y_spread = y - self.vertices[i].y
            
    #         if (self.vertices[i].y > y) != (self.vertices[j].y > y) and x < (delta_x * y_spread / delta_y) + self.vertices[i].x:
    #             c = False if c else True
                
    #         j = i
    #     return c
        

            
    
    
    
