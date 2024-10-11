from peg import Peg


class PegSystem():
    
    def __init__(self, cell, n_grid, radius):
        self.pegs = []
        self.cell = cell
        self.n_grid = n_grid
        self.radius = radius
        
        self.square_grid(n_grid)
        # self.grid_layout(n_grid)
        
    
    def add_peg(self, x, y, r):
        self.pegs.append(Peg(x, y, r))
                
    
    def render(self):
        for peg in self.pegs:
            peg.render()
    
    
    def square_grid(self, n_grid):
        col_w = min(self.cell.w, self.cell.h) / (n_grid + 1)
        self.grid_w = col_w * n_grid
        offset = (max(self.cell.w, self.cell.h) - min(self.cell.w, self.cell.h)) / 2
        
        self.grid_x = self.cell.x + col_w if self.cell.w < self.cell.h else self.cell.x + col_w + offset
        self.grid_y = self.cell.y + col_w if self.cell.h < self.cell.w else self.cell.y + col_w + offset
        
        for i in range(n_grid):
            for j in range(n_grid):
                if self.cell.w > self.cell.h:
                    self.add_peg(self.cell.x + col_w * (i + 1) + offset, self.cell.y + col_w * (j + 1), self.radius)
                else:    
                    self.add_peg(self.cell.x + col_w * (i + 1), self.cell.y + col_w * (j + 1) + offset, self.radius)
    
    def grid_layout(self, n_grid):
        col_w = self.cell.w / (n_grid + 1)
        row_h = self.cell.h / (n_grid + 1)
        
        for i in range(n_grid):
            for j in range(n_grid):
                self.add_peg(self.cell.x + col_w * (i + 1), self.cell.y + row_h * (j + 1), self.radius)
                
                
   
    
    

                
    
