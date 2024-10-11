
class Liquid(object):
    
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        
        
    def is_inside(self, p):
        if p.loc.x > self.x and p.loc.x < self.x + self.w and p.loc.y > self.y and p.loc.y < self.y + self.h:
            return True
        return False

    def drag(self, p):
        speed = p.vel.mag()
        magnitude = self.c * sq(speed)
        force = p.vel.get()
        force.mult(-1)
        force.normalize()
        force.mult(magnitude)
        
        return force
    
    
    def display(self):
        noStroke()
        fill(200, 100)
        rect(self.x, self.y, self.w, self.h)
