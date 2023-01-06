
class Gravity(object):
    
    def __init__(self):
        self.G = 0.1
        
    def gravity(self, p):
        return PVector(0, self.G * p.mass)
