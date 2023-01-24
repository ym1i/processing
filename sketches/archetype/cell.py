
class Cell():
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.partitions = []
        
        
    def render(self):
        noFill()
        stroke(0)
        strokeWeight(2)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
        
    
    def render_partitions(self):
        for p in self.partitions:
            noFill()
            stroke(0, 0, 0)
            strokeWeight(1)
            rectMode(CORNER)
            rect(p.x, p.y, p.w, p.h)
        
        
class Partition():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def render(self):
        noFill()
        stroke(0)
        strokeWeight(1)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
