from peg_system import PegSystem


class Cell():
    
    def __init__(self, x, y, w, h, n_grid, radius):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pegs = PegSystem(self, n_grid, radius) 
            
    
    def render(self, no_fill=False):
        fill(0)
        if no_fill:
            noFill()
        rect(self.x, self.y, self.w, self.h)
