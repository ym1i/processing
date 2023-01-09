from cell import Cell


class GameOfLife(object):
    
    def __init__(self, n_col, n_row, w):
        self.board = [[Cell(col * w, row * w, w) for col in range(n_col)] for row in range(n_row)]
        self.n_col = n_col
        self.n_row = n_row
        self.w = w
        
                
    def update(self):
        for row in range(self.n_row):
            for col in range(self.n_col):
                self.board[row][col].prev = self.board[row][col].state
        
        for row in range(0, self.n_row):
            for col in range(0, self.n_col):    
                neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbors += self.board[(row + i + self.n_row) % self.n_row][(col + j + self.n_col) % self.n_col].prev
                neighbors -= self.board[row][col].prev
        
                if self.board[row][col].state == 1 and neighbors < 2:
                    self.board[row][col].state = 0
                elif self.board[row][col].state == 1 and neighbors > 3:
                    self.board[row][col].state = 0
                elif self.board[row][col].state == 0 and neighbors == 3:
                    self.board[row][col].state = 1
 
       
    def rebirth(self):
        for i in range(10):
            self.board[int(random(self.n_row))][int(random(self.n_col))].state == 1
                    
                
    def render(self):
        for row in range(self.n_row):
            for col in range(self.n_col):
                self.board[row][col].render()
                
                
                
                
