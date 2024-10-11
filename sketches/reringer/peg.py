

class Peg():
    
    def __init__(self, loc, r, plt):
        self.loc = loc
        self.r = r
        self.plt = plt
        
        
    def render(self):
        fill(self.plt.random_color())
        ellipse(self.loc.x, self.loc.y, self.r * 2, self.r * 2)
