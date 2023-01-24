from cell import Cell


class Section():
    
    def __init__(self, x, y, w, h, pl):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cells = []
        self.palette = pl
        
        
    def render(self):
        noStroke()
        fill(self.palette.random_color())
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
        
    
    def render_2(self):
        noFill()
        stroke(255, 0, 0)
        strokeWeight(1)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
   
             
    def make_cells(self, n):
        cell_width = self.w / n
        for i in range(n):
            self.cells.append(Cell(self.x + cell_width * i, self.y, cell_width, self.h))
    
