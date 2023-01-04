# A force is a vector that causes an object with mass to accelerate.
# Force equals mass times acceleration. (Newton's 2nd Law) f = m * a | a = f / m 


class Mover(object):
    
    def __init__(self, x, y, vx, vy, ax, ay, max_vel=10):
        self.loc = PVector(x, y)
        self.vel = PVector(vx, vy)
        self.acc = PVector(ax, ay)
        self.mass = 10.0
        self.max_vel = max_vel
        self.G = 0.4
        
        
    def display(self):
        stroke(0)
        fill(175)
        ellipse(self.loc.x, self.loc.y, self.mass * 16, self.mass * 16)
        
        
    def apply_force(self, force):
        f = PVector.div(force, self.mass)
        self.acc.add(f)
        
        
    def attract(self, obj):
        force = PVector.sub(self.loc, obj.loc)
        distance = force.mag()
        distance = constrain(distance, 5, 25)
        force.normalize()
        strength = self.G * self.mass * obj.mass / sq(distance)
        force.mult(strength)
            
        return force
        
                
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.max_vel)
        self.loc.add(self.vel)
        self.acc.mult(0)
         
  
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
            
            
            
