
class Cantor():
    
    def __init__(self, start, end, min_len, y_offset):
        self.start = start
        self.end = end
        self.len = PVector.sub(end, start).mag()
        self.min_len = min_len
        self.y_offset = y_offset
        
    def generate(self):
        next = []
        l = self.len / 3.0
        next.append(PVector(self.start.x, self.start.y + self.y_offset))
        next.append(PVector(self.start.x + l, self.start.y + self.y_offset))
        next.append(PVector(self.end.x - l, self.end.y + self.y_offset))
        next.append(PVector(self.end.x, self.end.y + self.y_offset))
        
        return next
        
    def display(self):
        beginShape()
        vertex(self.start.x, self.start.y)
        vertex(self.end.x, self.end.y)
        endShape()
