

class Peg():
    
    def __init__(self, x, y, r, side):
        self.x = x
        self.y = y
        self.r = r
        self.v = PVector(x, y)
        self.side = side
        

    def render(self, c, sw=1, no_stroke=True, no_fill=False):
        stroke(0)
        strokeWeight(sw)
        if no_stroke:
            noStroke()
        fill(c)
        if no_fill:
            noFill()
        ellipse(self.x, self.y, self.r, self.r)

        
    def open_circle(self, c, no_fill=True):
        stroke(0)
        strokeWeight(1)
        fill(c)
        if no_fill:
            noFill()
        
        if self.side == 'left': 
            start = PI + QUARTER_PI
            stop = start + 1.5 * PI
        else:
            start = QUARTER_PI
            stop = start + 1.5 * PI
            
        beginShape()
        # vertex(self.x, self.y)
        for i in range(20):
            a = map(i, 0, 19, start, stop)
            vertex(self.x + self.r * cos(a), self.y + self.r * sin(a))
        # vertex(self.x, self.y)
        endShape()
