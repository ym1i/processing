
class Cell(object):
    
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.state = int(random(2))
        self.prev = self.state
        
    def render(self):
        # fill(0) if self.board[row][col].state == 1 else fill(255)
        if self.prev == 0 and self.state == 1:
            fill(0, 0, 255)
        elif self.state == 1:
            fill(0, 0, 0)
        elif self.prev == 1 and self.state == 0:
            fill(255, 0, 0)
        else:
            fill(255) 
        rect(self.x, self.y, self.w, self.w)
        
