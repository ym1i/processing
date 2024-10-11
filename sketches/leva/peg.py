

class Peg():
    
    def __init__(self, x, y, r, style):
        self.center = PVector(x, y)
        self.x = x
        self.y = y
        self.r = r
        self.style = style
        self.reverse = False
    
    def render(self, body_color, stroke_color):
        # fill(body_color)
        fill(0)
        strokeWeight(3)
        stroke(0)
        ellipse(self.x, self.y, self.r * 0.8, self.r * 0.8)
