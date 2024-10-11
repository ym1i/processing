from circle_packing import CirclePacking, Circle


class Buds():
    
    def __init__(self, pos, r, colour):
        self.pos = pos
        self.r = r
        self.colour = colour
        self.packed_circles = []
        self.outer_circle = Circle(pos.x, pos.y, r, color(255, 255, 255))
        
        self.make_buds()
        
    
    def make_buds(self):
        layers = 3
        inner_r = 30
        outer_r = self.r - 10
        bud_r = (outer_r - inner_r) / (layers + 1)
        for j in range(layers):
            r = map(j, 0, layers-1, inner_r, outer_r)
            n = int(r / 5)
            for i in range(n):
                a = map(i, 0, n-1, 0, TAU)
                x = self.pos.x + r * cos(a)
                y = self.pos.y + r * sin(a)
                self.packed_circles.append(CirclePacking(PVector(x, y), bud_r))
            
    
    def circle_packing(self):
        n = 40
        count = 0
        attempts = 0
        while count < n and attempts < 2000:
            if self.create_bud():
                count += 1 
            else:
                attempts += 1
                
    
    def create_bud(self):
        r = random(self.r * 0.14, self.r * 0.16)
        x = random(self.pos.x - self.r + r, self.pos.x + self.r - r)
        y = random(self.pos.y - self.r + r, self.pos.y + self.r - r)
        v = PVector(x, y)
        colour = color(255, 255, 255)
        
        # check if inside circle
        inside = PVector.sub(v, self.pos).mag() + r <= self.r
        
        # collision detection
        collide = False
        play = r * 0.1
            
        for other_circle in self.packed_circles:
            if PVector.sub(other_circle.pos, v).mag() < r + other_circle.r - play:
                collide = True
                break
        
        if inside and not collide:
            self.packed_circles.append(CirclePacking(v, r))
            return True
        else:
            return False  
        
    
    def render(self):
        strokeWeight(2)
        self.outer_circle.render()
        for circle in self.packed_circles:
            circle.render()
        
        


    
