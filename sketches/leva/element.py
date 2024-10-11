from peg import Peg


class Element():
    
    def __init__(self, layout, color, palette):
        self.pegs = []
        self.selected = []
        self.layout = layout
        self.color = color
        self.palette = palette
        self.n_cols = 3
        self.n_rows = 3
        self.grid_width = width / (self.n_cols + 1)
        self.grid_height = height / (self.n_rows + 1)
        
        self.grid_layout()
        
    
    def add_peg(self, x, y, r, style):
        self.pegs.append(Peg(x, y, r, style))
        
        
    def get_index(self, x, y):
        row = int(y / self.grid_height)
        col = int(x / self.grid_width)
        
        return row * self.n_cols + col
        
    
    def random_pegs(self):
        n = 2
        visited = []
        current = int(random(len(self.pegs)))
        self.selected.append(current)
        visited.append(current)
        
        for i in range(n):
            next, visited, complete = self.pick_neighbor(current, visited, self.n_cols, self.n_rows, self.grid_width, self.grid_height)
            if not complete:
                break
            self.selected.append(next)
            current = next
            
    
    def wrap(self):
        sorted_pegs = []
        for j in range(self.n_rows):
            sorted_pegs.append(sorted([peg for peg in self.selected if peg in range(j * self.n_rows, j * self.n_rows + self.n_cols)]))
        print 'sorted: ', sorted_pegs
        
        cur = sorted(self.selected)[0]
        cur_row = cur / self.n_rows
        
        beginShape()
        noFill()
        # start at CUR, go RIGHT to the right edge in the same row
        vertex(self.pegs[cur].x, self.pegs[cur].y - self.pegs[cur].r)
        for i in sorted_pegs[cur_row]:
            if i != cur:
                vertex(self.pegs[i].x, self.pegs[i].y - self.pegs[i].r)
                cur = i
                
        # ROUND the courner
        self.round_corner(1.5 * PI, TWO_PI, cur)
                
        # go DOWN along the RIGHT edge
        for j in range(cur_row, self.n_rows):
            if sorted_pegs[j]:
                next = sorted_pegs[j][-1]
                if cur % self.n_cols == next % self.n_cols:
                    # SAME COL, just go DOWN
                    vertex(self.pegs[next].x + self.pegs[next].r, self.pegs[next].y)
                    cur = next
                elif cur % self.n_cols < next % self.n_cols:
                    # go 1 COL RIGHT 1 ROW DOWN, then go RIGHT to the right edge in the row reacing to NEXT
                    
                    # ROUND the corner
                    self.round_corner(PI, HALF_PI, cur + 1)
                    
                    cur += self.n_cols + 1
                    for i in range(cur, next + 1):
                        vertex(self.pegs[i].x, self.pegs[i].y - self.pegs[i].r)
                    
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
                        vertex(self.pegs[cur].x, self.pegs[cur].y + self.pegs[cur].r)
                        
                    # ROUND the corner
                    self.round_corner(1.5 * PI, PI, cur + self.n_cols)
                     
                    vertex(self.pegs[next].x + self.pegs[next].r, self.pegs[next].y)
                    cur = next
                    
        # start at CUR, go LEFT to the left edge in the same row
        
        # ROUND the corner
        self.round_corner(0, HALF_PI, cur)
        
        cur_row = cur / self.n_rows
        for i in reversed(sorted_pegs[cur_row]):
            if i != cur:
                vertex(self.pegs[i].x, self.pegs[i].y + self.pegs[i].r)
                cur = i
                
        # ROUND the corner
        self.round_corner(HALF_PI, PI, cur)
                
        # go UP along the LEFT edge
        for j in reversed(range(cur_row)):
            if sorted_pegs[j]:
                next = sorted_pegs[j][0]
                if cur % self.n_cols == next % self.n_cols:
                    # go UP in the SAME column
                    vertex(self.pegs[next].x - self.pegs[next].r, self.pegs[next].y)
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                     # go up 1 COL LEFT and 1 ROW UP, then go LEFT to the left edge in the same row ([cur_row - 1])
                     
                     # ROUND the corner
                     self.round_corner(TWO_PI, 1.5 * PI, cur - 1)
                     
                     cur = cur - self.n_cols - 1
                     for i in reversed(range(next, cur + 1)):
                        vertex(self.pegs[i].x, self.pegs[i].y + self.pegs[i].r)
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
                        vertex(self.pegs[cur].x, self.pegs[cur].y - self.pegs[cur].r)
                        
                    # ROUND the corner
                    self.round_corner(HALF_PI, 0, cur - self.n_cols)
                            
                    vertex(self.pegs[next].x - self.pegs[next].r, self.pegs[next].y)
                    cur = next
            
        # # ROUND the corner
        self.round_corner(PI, 1.5 * PI, cur)
        endShape()
        
        
    def round_corner(self, theta_1, theta_2, peg_id):
        for i in range(10):
            theta = map(i, 0, 9, theta_1, theta_2)
            x = self.pegs[peg_id].x + self.grid_width / 2 * cos(theta)
            y = self.pegs[peg_id].y + self.grid_width / 2 * sin(theta)
            vertex(x, y)
    
    def pick_neighbor(self, current, visited, n_cols, n_rows, w, h):
        count = 0
        while count < 99:
            r = random(1)
            if r < 0.125:
                next = current - n_cols - 1
            elif r < 0.25:
                next = current - n_cols
            elif r < 0.375:
                next = current - n_cols + 1
            elif r < 0.5:
                next = current - 1
            elif r < 0.625:
                next = current + 1
            elif r < 0.75:
                next = current + n_cols - 1
            elif r < 0.875:
                next = current + n_cols
            else:
                next = current + n_cols + 1
                
            next %= len(self.pegs)
            
            d = PVector.dist(self.pegs[current].center, self.pegs[next].center)
            if d < w * sqrt(2) + 1 and next not in visited:
                break
            count += 1
        
        if count == 99:
            return next, visited, False
        else:
            visited.append(next)
            return next, visited, True
                
            
        
    def grid_layout(self):
        # r = map(self.n_cols, 3, 5, self.grid_width * 0.25, self.grid_width * 0.3)
        r = self.grid_width / 2
        
        for j in range(1, self.n_rows + 1):                
            for i in range(1, self.n_cols + 1):
                style = 'solid'
                self.add_peg(self.grid_width * i, self.grid_height * j, r, style)
                
        
    def render(self):
        self.wrap()
        fill(self.color)
    
        for peg in self.pegs:
            peg.render(self.palette.random_color(), self.palette.random_color())
            
        for i in self.selected:
            fill(255, 0, 0)
            ellipse(self.pegs[i].x, self.pegs[i].y, self.pegs[i].r * 1.2, self.pegs[i].r * 1.2)
            
