class Peg():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.center = PVector(x, y)
    
            
    def render(self, no_fill=False):
        fill(255)
        if no_fill:
            noFill()
        stroke(0)
        strokeWeight(1)
        ellipse(self.x, self.y, self.r * 2, self.r * 2)
                    
                    
    def bulls_eye(self, n, no_fill=False):
        for i in range(n):
            diameter = self.r * 2 * pow(0.6, i)
            if i % 2 == 0:
                fill(255)
                if no_fill:
                    noFill()
                ellipse(self.x, self.y, diameter, diameter)
            else:
                fill(255)
                if no_fill:
                    noFill()
                ellipse(self.x, self.y, diameter, diameter)
