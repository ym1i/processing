
class Repeller(object):
    def __init__(self, x, y, G=0.4):
        self.loc = PVector(x, y)
        self.r = 10
        self.G = G
        
    def repel(self, p):
        force = PVector.sub(self.loc, p.loc)
        d = force.mag()
        d = constrain(d, 5, 100)
        force.normalize()
        magnitude = -1 * self.G / sq(d)
        force.mult(magnitude)
        return force
    
    def display(self):
        stroke(0)
        fill(0)
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)
        
