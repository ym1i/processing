
class Spring(object):
    def __init__(self, x, y, len, k=0.1):
        self.anchor = PVector(x, y)
        self.len = len
        self.k = k
        
    def connect(self, p):
        force = PVector.sub(p.loc, self.anchor)
        d = force.mag()
        stretch = d - self.len
        
        force.normalize()
        force.mult(-1 * self.k * stretch)
        
        p.apply_force(force)
        
    def display(self):
        fill(100)
        rectMode(CENTER)
        rect(self.anchor.x, self.anchor.y, 10, 10)
        
    def display_line(self, p):
        stroke(255)
        line(p.loc.x, p.loc.y, self.anchor.x, self.anchor.y)
