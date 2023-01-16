
class Branch():
    
    def __init__(self, start, vel, n):
        self.start = start.get()
        self.end = start.get()
        self.vel = vel.get()
        self.timer_start = n
        self.timer = self.timer_start
        self.growing = True
        
    def update(self):
        if self.growing:
            self.end.add(self.vel)
        
    def render(self):
        stroke(0)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        
        
    def generate(self, angle):
        theta = self.vel.heading()
        m = self.vel.mag()
        theta += radians(angle)
        new_vel = PVector(m * cos(theta), m * sin(theta))
        
        return Branch(self.end, new_vel, self.timer_start * 0.66)
        
    def timer_to_branch(self):
        self.timer -= 1
        if self.timer < 0 and self.growing:
            self.growing = False
            return True
        return False
    
    def rotate(self, v, theta):
        x = v.x * cos(theta) - v.y * sin(theta)
        y = v.x * sin(theta) + v.y * cos(theta)
        
        return PVector(x, y)
    
