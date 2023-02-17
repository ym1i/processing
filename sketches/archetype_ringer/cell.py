from peg_system import PegSystem


class Cell():
    
    def __init__(self, x, y, w, h, layout, scaling, n_grid, radius, body, bg):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bg = bg
        self.pegs = PegSystem(layout, scaling, self, n_grid, radius, body, bg) 
        self.colors = []
        
    
    def set_colors(self, colors):
        self.colors = colors
    
    
    def render(self):
        fill(self.bg)
        rect(self.x, self.y, self.w, self.h)
