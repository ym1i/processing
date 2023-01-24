from cell import Cell


class Section():
    
    def __init__(self, x, y, w, h, pl):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cells = []
        self.partition_width = random(10, self.w / 3)
        self.partition_height = random(10, self.h / 3)
        self.palette = pl
        
        
    def render(self):
        noStroke()
        fill(self.palette.random_color())
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
   
             
    def make_cells(self, n):
        col_width = self.w / n
        row_height = self.h / n
        self.cells = [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                self.cells[row][col] = Cell(self.x + col_width * col, self.y + row_height * row, col_width, row_height, self.partition_width, self.partition_height)    
        
    
    # def draw_circle(self):
    #     center = PVector(self.x + self.w/2, self.y + self.h/2)
    #     r = min(self.w, self.h)
    #     fill(self.palette.random_color())
    #     ellipse(center.x, center.y, r, r)
        
    #     self.rect_in_circle(center.x, center.y, r/2)
        
    # def rect_in_circle(self, cx, cy, cr):
    #     fill(self.palette.random_color())
    #     rectMode(CENTER)
    #     rect(cx, cy, cr, cr)
