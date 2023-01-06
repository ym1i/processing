
class Friction(object):
    
    def __init__(self, c=0.01, N=1):
        self.c = 0.01
        self.N = 1
        
        
    def friction(self, p):
        magnitude = self.c * self.N
        force = p.vel.get()
        force.mult(-1)
        force.normalize()
        force.mult(magnitude)
        
        return force
