
class Liquid(object):
    
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        
        
    def is_inside(self, x, y):
        if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
            return True
        return False

    def drag(self, v):
        speed = v.mag()
        magnitude = self.c * sq(speed)
        _drag = v.get()
        _drag.mult(-1)
        _drag.normalize()
        _drag.mult(magnitude)
        
        return _drag
    
    
    def display(self):
        noStroke()
        fill(175)
        rect(self.x, self.y, self.w, self.h)
