
class Particle(object):
    def __init__(self, loc, mass=1.0):
        self.loc = loc.get()
        self.vel = PVector(random(-1, 1), random(-2, 0))
        self.acc = PVector(0, 0)
        self.mass = mass
        self.lifespan = 255.0
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        self.vel.add(self.acc)
        self.loc.add(self.vel)
        self.acc.mult(0)
        self.lifespan -= -2.0
        
    def apply_force(self, _force):
        force = _force.get()
        force.div(self.mass)
        self.acc.add(force)
        
    def display(self):
        stroke(0, self.lifespan)
        fill(175, self.lifespan)
        ellipse(self.loc.x, self.loc.y, 8, 8)
        
    def is_dead(self):
        return True if self.lifespan < 0 else False
    
    def check_boundary(self):
        if self.loc.x > width:
            self.loc.x = width
            self.vel.x *= -1
        elif self.loc.x < 0: 
            self.loc.x = 0
            self.vel.x *= -1
 
        if self.loc.y > height:
            self.loc.y = height
            self.vel.y *= -1
        elif self.loc.y < 0: 
            self.loc.y = 0
            self.vel.y *= -1
