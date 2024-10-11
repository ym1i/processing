from peg import Peg
from wrapper import Wrapper


class Element(Wrapper):
    
    def __init__(self, pegs, id, n_cols, n_rows, palette):
        self.pegs = pegs
        self.element_id = id
        self.vertices = []
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.palette = palette
        
    
    def wrap(self):
        grid_width = width / (self.n_cols + 1)
        r = grid_width / 2
        sorted_pegs = []
        for j in range(self.n_rows):
            sorted_pegs.append(sorted([peg for peg in self.element_id if peg in range(j * self.n_rows, j * self.n_rows + self.n_cols)]))
    
        cur = sorted(self.element_id)[0]
        cur_row = cur / self.n_rows
        
        # start at CUR, go RIGHT to the right edge in the same row
        self.vertices.append(PVector(self.pegs[cur].x, self.pegs[cur].y - r))
        for i in sorted_pegs[cur_row]:
            if i != cur:
                self.vertices.append(PVector(self.pegs[i].x, self.pegs[i].y - r))
                cur = i
                
        # ROUND the courner
        self.round_corner(1.5 * PI, TWO_PI, cur)
                
        # go DOWN along the RIGHT edge
        for j in range(cur_row, self.n_rows):
            if sorted_pegs[j]:
                next = sorted_pegs[j][-1]
            
                if cur % self.n_cols == next % self.n_cols:
                    # SAME COL, just go DOWN
                    self.vertices.append(PVector(self.pegs[next].x + r, self.pegs[next].y))
                    cur = next
                elif cur % self.n_cols < next % self.n_cols:
                    # go 1 COL RIGHT 1 ROW DOWN, then go RIGHT to the right edge in the row reacing to NEXT
                    
                    # ROUND the corner
                    self.round_corner(PI, HALF_PI, cur + 1)
                    
                    cur += self.n_cols + 1
                    for i in range(cur, next + 1):
                        self.vertices.append(PVector(self.pegs[i].x, self.pegs[i].y - r))
                    
                    cur = next        
                    # ROUND the corner
                    self.round_corner(1.5 * PI, TWO_PI, cur)
                    
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                    dcol = cur % self.n_cols - next % self.n_cols
                    # go LEFT several cols in the current row until the NEXT is located just at left bottom
                    
                    # ROUND the corner
                    self.round_corner(0, HALF_PI, cur)
                    
                    for i in range(dcol - 1):
                        cur -= 1
                        self.vertices.append(PVector(self.pegs[cur].x, self.pegs[cur].y + r))
                        
                    # ROUND the corner
                    self.round_corner(1.5 * PI, PI, cur + self.n_cols)
                    self.vertices.append(PVector(self.pegs[next].x + r, self.pegs[next].y))
                    cur = next
                    
        # start at CUR, go LEFT to the left edge in the same row
        
        # ROUND the corner
        self.round_corner(0, HALF_PI, cur)
        
        cur_row = cur / self.n_rows
        for i in reversed(sorted_pegs[cur_row]):
            if i != cur:
                self.vertices.append(PVector(self.pegs[i].x, self.pegs[i].y + r))
                cur = i
                
        # ROUND the corner
        self.round_corner(HALF_PI, PI, cur)
                
        # go UP along the LEFT edge
        for j in reversed(range(cur_row)):
            if sorted_pegs[j]:
                next = sorted_pegs[j][0]
                if cur % self.n_cols == next % self.n_cols:
                    # go UP in the SAME column
                    self.vertices.append(PVector(self.pegs[next].x - r, self.pegs[next].y))
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                     # go up 1 COL LEFT and 1 ROW UP, then go LEFT to the left edge in the same row ([cur_row - 1])
                     
                     # ROUND the corner
                     self.round_corner(TWO_PI, 1.5 * PI, cur - 1)
                     
                     cur = cur - self.n_cols - 1
                     for i in reversed(range(next, cur + 1)):
                        self.vertices.append(PVector(self.pegs[i].x, self.pegs[i].y + r))
                     cur = next
                     
                     # ROUND the corner
                     self.round_corner(HALF_PI, PI, cur)
                     
                elif cur % self.n_cols < next % self.n_cols:
                    dcol = next % self.n_cols - cur % self.n_cols
                    # go RIGHT DCOLs in CUR_ROW until the NEXT is at 1 COL RIGHT and 1 ROW UP
                    
                    # ROUND the corner
                    self.round_corner(PI, 1.5 * PI, cur)
                    
                    for i in range(dcol - 1):
                        cur += 1
                        self.vertices.append(PVector(self.pegs[cur].x, self.pegs[cur].y - r))
                        
                    # ROUND the corner
                    self.round_corner(HALF_PI, 0, cur - self.n_cols)            
                    self.vertices.append(PVector(self.pegs[next].x - r, self.pegs[next].y))
                    cur = next
            
        # ROUND the corner
        self.round_corner(PI, 1.5 * PI, cur)
    
    
    def round_corner(self, theta_1, theta_2, peg_id):
        grid_width = width / (self.n_cols + 1)
        grid_height = height / (self.n_rows + 1)
        delta = PI / 20
        for i in range(10):
            if theta_2 > theta_1:
                theta = map(i, 0, 9, theta_1 + delta, theta_2 - delta)
            else:
                theta = map(i, 0, 9, theta_1 - delta, theta_2 + delta)
            # theta = map(i, 0, 9, theta_1, theta_2)
            x = self.pegs[peg_id].x + grid_width / 2 * cos(theta)
            y = self.pegs[peg_id].y + grid_height / 2 * sin(theta)
            self.vertices.append(PVector(x, y))
