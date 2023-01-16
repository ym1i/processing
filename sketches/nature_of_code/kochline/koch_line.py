
class KochLine():
    
    def __init__(self, start, end):
        self.start = start.get()
        self.end = end.get()
        
    def koch_a(self):
        return self.start.get()
    
    def koch_b(self):
        v = PVector.sub(self.end, self.start)
        v.div(3)
        v.add(self.start)
        return v
    
    def koch_c(self):
        a = self.start.get()
        v = PVector.sub(self.end, self.start)
        v.div(3)
        a.add(v)
        v.rotate(-radians(60))
        # self.rotate(v, -radians(60))
        a.add(v)
        return a
    
    def koch_d(self):
        v = PVector.sub(self.end, self.start)
        v.mult(2 / 3.0)
        v.add(self.start)
        return v 
    
    def koch_e(self):
        return self.end.get()
    
    def rotate(self, v, theta):
        temp = v.x
        v.x = v.x * cos(theta) - v.y * sin(theta)
        v.y = temp * sin(theta) + v.y * cos(theta)
        
    
    def display(self):
        stroke(0)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
