

class Peg():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.center = PVector(x, y)
        self.r = r
    
    
    def render(self, c, sw=1, no_stroke=False, palette=False, style='None'):
        stroke(0)
        strokeWeight(sw)
        if no_stroke:
            noStroke()
            
        if style == 'None':
            fill(c)
            ellipse(self.x, self.y, self.r, self.r)
        elif style == 'bullseye':
            fill(palette.random_color())
            for i in range(3):
                # fill(palette.random_color())
                ellipse(self.x, self.y, self.r * (1.3 - 0.3 * i), self.r * (1.3 - 0.3 * i))
        
    
    
        
        
