

class Peg():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.center = PVector(x, y)
        self.r = r
    
    
    def render(self, c, sw=1, no_stroke=False):
        stroke(0)
        strokeWeight(sw)
        if no_stroke:
            noStroke()
        fill(c)
        ellipse(self.x, self.y, self.r * 2, self.r * 2)
        
        
