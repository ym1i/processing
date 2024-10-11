

class Attractor(object):
    
    def __init__(self, x, y, r, mass=20):
        self.loc = PVector(x, y)
        self.r = r
        self.mass = mass
        self.G = 0.4    
        
    def attract(self, p):
        force = PVector.sub(self.loc, p.loc)
        distance = force.mag()
        distance = constrain(distance, 5, 25)
        force.normalize()
        strength = self.G * self.mass * p.mass / sq(distance)
        force.mult(strength)
            
        return force
        
    def display(self):
        stroke(0)
        fill(color(211, 51, 59))
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)
        

class Repeller(object):
    def __init__(self, x, y, r, G=0.4):
        self.loc = PVector(x, y)
        self.r = r
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
        fill(color(45, 132, 194))
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)
        

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
    
    
class Gravity(object):
    
    def __init__(self, G):
        self.G = G
        
    def gravity(self, p):
        return PVector(0, self.G * p.mass)
    
    
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
    
