
class Gravity(object):
    
    def __init__(self, G):
        self.G = G
        
    def gravity(self, p):
        return PVector(0, self.G * p.mass)
