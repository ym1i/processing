

class CirclePacking():
    
    def __init__(self, n_circles, min_r, max_r, w, h):
        self.circles = [Circle(min_r, max_r, w, h)]
        
        self.pack(n_circles, min_r, max_r, w, h)
        
    
    def pack(self, n_circles, min_r, max_r, w, h):
        count = 1
        while count < n_circles:
            intersect = False
            circle = Circle(min_r, max_r, w, h)
            for c in self.circles:
                if circle.intersects(c):
                    intersect = True
                    break
                
            if not intersect:
                self.circles.append(circle)
                count += 1
                    
                
    def get_starting_positions(self):
        starting_positions = []
        for c in self.circles:
            starting_positions.append(PVector(c.x, c.y))
            
        return starting_positions
            

class Circle():
    
    def __init__(self, min_r, max_r, w, h):
        self.r = random(min_r, max_r)
        self.x = random(self.r, w - self.r)
        self.y = random(self.r, h - self.r)
        
    
    def intersects(self, circle):
        return dist(circle.x, circle.y, self.x, self.y) < circle.r + self.r
    
    
    def render(self):
        noFill()
        stroke(0)
        ellipse(self.x, self.y, self.r * 2, self.r * 2)
        
        
