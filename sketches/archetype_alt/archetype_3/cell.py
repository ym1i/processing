

class Cell():
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # self.sections = []
    
        
    def render(self):
        # noStroke()
        # fill(self.palette.random_color())
        noFill()
        stroke(0)
        strokeWeight(1)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
        
