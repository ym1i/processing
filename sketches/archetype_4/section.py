from cell import Cell


class Section():
    
    def __init__(self, x, y, w, h, pl):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cells = []
        self.palette = pl
        
        
    def render_fill(self):
        noStroke()
        fill(self.palette.random_color())
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
        
    
    def render_stroke(self):
        noFill()
        stroke(0, 0, 0)
        strokeWeight(1)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
   
             
    def make_cells(self, n):
        cell_width = self.w / n
        cell_height = self.h / n
        for j in range(n):
            for i in range(n):
                self.cells.append(Cell(self.x + cell_width * i, self.y + cell_height * j, cell_width, cell_height))
    
