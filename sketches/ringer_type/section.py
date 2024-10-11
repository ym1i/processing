class Section():
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cells = []
        
    def render(self):
        if random(1) < 0.1:
            fill(0)
        elif random(1) < 0.2:
            stroke(1)
        else:
            noFill()
            noStroke()
        rect(self.x, self.y, self.w, self.h)
        strokeWeight(1)
