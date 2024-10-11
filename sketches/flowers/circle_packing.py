

class CirclePacking():
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r
        self.circles = []
        self.outer_circle = Circle(self.pos.x, self.pos.y, self.r, color(255, 255, 255))
        
        self.pack()
        
    
    def pack(self):
        n = 10
        count = 0
        attempts = 0
        while count < n and attempts < 2000:
            if self.create_circle():
                count += 1 
            else:
                attempts += 1
                
    def create_circle(self):
        r = random(self.r * 0.15, self.r * 0.4)
        x = random(self.pos.x - self.r + r, self.pos.x + self.r - r)
        y = random(self.pos.y - self.r + r, self.pos.y + self.r - r)
        v = PVector(x, y)
        colour = color(255, 255, 255)
        
        # check if inside circle
        inside = PVector.sub(v, self.pos).mag() + r <= self.r
        
        # collision detection
        collide = False
        play = r * 0.4
            
        for other_circle in self.circles:
            if PVector.sub(other_circle.pos, v).mag() < r + other_circle.r - play:
                collide = True
                break
        
        if inside and not collide:
            self.circles.append(Circle(x, y, r, colour))
            return True
        else:
            return False  
        
    def render(self):
        self.outer_circle.render()
        for circle in self.circles:
            circle.render()
        
        

class Circle():
    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.pos = PVector(x, y)
        self.r = r
        self.verts = []
        self.colour = colour
        
        self.set_verts()
    
    def set_verts(self):
        n = 30
        nx_scale = self.r * random(0.3, 0.6)
        ny_scale = self.r * random(0.3, 0.6)
        noise_step = 0.002
        for i in range(n):
            theta = map(i, 0, n-1, 0, TAU)
            x = self.x + self.r * cos(theta)
            y = self.y + self.r * sin(theta)
            nx = map(noise(x * noise_step, y * noise_step), 0, 1, -nx_scale, nx_scale)
            ny = map(noise(x * noise_step, y * noise_step), 0, 1, -ny_scale, ny_scale)
            self.verts.append(PVector(x + nx, y + ny))
      
    def render(self):
        fill(self.colour)
        beginShape()
        for v in self.verts:
            vertex(v.x, v.y)
        endShape()    
        
