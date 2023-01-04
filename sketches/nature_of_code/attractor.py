
class Attractor(object):
    
    def __init__(self, x=0, y=0, mass=20):
        self.loc = PVector(x, y)
        self.mass = mass
        self.G = 0.4
        
        
    def attract(self, obj):
        force = PVector.sub(self.loc, obj.loc)
        distance = force.mag()
        distance = constrain(distance, 5, 25)
        force.normalize()
        strength = self.G * self.mass * obj.mass / sq(distance)
        force.mult(strength)
            
        return force
    
        
    def display(self):
        stroke(0)
        fill(175, 200)
        ellipse(self.loc.x, self.loc.y, self.mass * 2, self.mass * 2)
        
    
