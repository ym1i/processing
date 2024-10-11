

class Peg():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.v = PVector(x, y)
        

    def render(self, c, sw=1, no_stroke=True, no_fill=False):
        stroke(0)
        strokeWeight(sw)
        if no_stroke:
            noStroke()
        fill(c)
        if no_fill:
            noFill()
        ellipse(self.x, self.y, self.r, self.r)
