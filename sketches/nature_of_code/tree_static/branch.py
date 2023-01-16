
class Branch():
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.has_branch = False      

    def generate(self, theta):
        mag = PVector.sub(self.end, self.start).mag()
        # mag *= 0.66
        sc = random(0.5, 0.8)
        mag *= sc
        
        v = PVector(mag * cos(theta), mag * sin(theta))
        new_start = self.end.get()
        new_end = new_start.get().add(v)
        
        self.has_branch = True
        
        return Branch(new_start, new_end)
    
    def render(self):
        len = PVector.sub(self.end, self.start).mag()
        sw = map(len, 1, 120, 1, 3)
        strokeWeight(sw)
        
        line(self.start.x, self.start.y, self.end.x, self.end.y)
    
