
class Peg():
    
    def __init__(self, x, y, r, style, color_1, color_2, mass):
        self.x = x
        self.y = y
        self.loc = PVector(x, y)
        self.r = r
        self.style = style
        self.color_1 = color_1
        self.color_2 = color_2
        # self.vel = PVector(random(-1, 1), random(-2, 0))
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.mass = mass
    
            
    def render(self):
        fill(self.color_1)
        stroke(0)
        
        if self.style == 'solid':
            ellipse(self.x, self.y, self.r * 2, self.r * 2)
        elif self.style == 'bulls_1':
            self.bulls_eye(2)
        elif self.style == 'bulls_2':
            self.bulls_eye(3)
        elif self.style == 'bulls_3':
            self.bulls_eye(4)
                    
                    
    def bulls_eye(self, n):
        for i in range(n):
            diameter = self.r * 2 * pow(0.6, i)
            if i % 2 == 0:
                fill(self.color_1)
                ellipse(self.x, self.y, diameter, diameter)
            else:
                fill(self.color_2)
                ellipse(self.x, self.y, diameter, diameter)
                

    def update(self):
        self.vel.add(self.acc)
        self.loc.add(self.vel)
        self.x = self.loc.x
        self.y = self.loc.y
        self.acc.mult(0)
    
        
    def apply_force(self, f):
        force = f.get()
        force.div(self.mass)
        self.acc.add(force)
        
        
        
        
