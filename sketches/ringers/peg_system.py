from peg import Peg


class PegSystem():
    
    def __init__(self, layout, style, size):
        self.pegs = []
        self.layout = layout
        self.style = style
        self.size = size
        self.probability = random(0.05, 0.5)
        self.n_cols = 0
        self.n_rows = 0
        self.col_width = 0
        self.colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194)]
        
    
    def add_peg(self, x, y, r, style, c1, c2):
        self.pegs.append(Peg(x, y, r, style, c1, c2))
        
    
    def set_layout(self):
        if self.layout == 'grid_3':
            self.grid_layout(3)
            self.n_cols = 3
            self.n_rows = 3
        elif self.layout == 'grid_4':
            self.grid_layout(4)
            self.n_cols = 4
            self.n_rows = 4
        elif self.layout == 'grid_5':
            self.grid_layout(5)
            self.n_cols = 5
            self.n_rows = 5
        elif self.layout == 'grid_6':
            self.grid_layout(6)
            self.n_cols = 6
            self.n_rows = 6
        elif self.layout == 'tiled_23':
            self.tiled_layout(2, 3)
            self.n_cols = 3
            self.n_rows = 3
        elif self.layout == 'tiled_32':
            self.tiled_layout(3, 2)
            self.n_cols = 3
            self.n_rows = 3
        elif self.layout == 'tiled_34':
            self.tiled_layout(3, 4)
            self.n_cols = 4
            self.n_rows = 4
        elif self.layout == 'tiled_43':
            self.tiled_layout(4, 3)
            self.n_cols = 4
            self.n_rows = 4
        elif self.layout == 'tiled_45':
            self.tiled_layout(4, 5)
            self.n_cols = 5
            self.n_rows = 5
        elif self.layout == 'tiled_54':
            self.tiled_layout(5, 4)
            self.n_cols = 5
            self.n_rows = 5
            
    
    def grid_layout(self, n_grid):
        x = width / (n_grid + 1)
        y = height / (n_grid + 1)
        self.col_width = x
        for i in range(n_grid):
            for j in range(n_grid):
                if random(1) < self.probability:
                    continue
                self.add_peg(x * (i + 1), y * (j + 1), self.size, self.style, self.colors[0], self.colors[0])
                
                
    def tiled_layout(self, tile_1, tile_2):
    
        n_cols = tile_1 if tile_1 > tile_2 else tile_2
        x = width / (n_cols + 1)
        self.col_width = x
        for i in range(n_cols):
            if i % 2 == 0:
                y = height / (tile_1 + 1)
                for j in range(tile_1):
                    if random(1) < self.probability:
                        continue
                    self.add_peg(x * (i + 1), y * (j + 1), self.size, self.style, self.colors[0], self.colors[0])
            else:
                y = height / (tile_2 + 1)
                for j in range(tile_2):
                    if random(1) < self.probability:
                        continue
                    self.add_peg(x * (i + 1), y * (j + 1), self.size, self.style, self.colors[0], self.colors[0])
                    
    
    def wrap(self):
        prob = random(0.5, 1)
        wrapped = []
        for peg in self.pegs:
            if random(1) < prob:
                wrapped.append(peg)
        
        beginShape()
        fill(self.colors[2])
        strokeWeight(2)
        
        offset = self.pegs[0].r
        
        # Find Pegs in the same column (LEFT most column in the wrapped section), and vertex() downward
        current = wrapped[0]
        vertex(current.x - offset, current.y)
        target = [peg for peg in wrapped if peg.x == current.x]
        if target:
            for peg in target:
                if peg.y > current.y:
                    current = peg    
                    vertex(current.x - offset, current.y)        
        vertex(current.x, current.y + offset)
        
        # Find the bottom of the next right column recursively from the current position
        next = current
        current_x = current.x
        while True:
            if current_x + self.col_width >= width:
                break
            next_col = [peg for peg in wrapped if peg.x == current.x + self.col_width]
            if next_col:
                next = next_col[0]
                for peg in next_col:
                    if peg.y > next.y:
                        next = peg
                
                # FOR SMOOTH WRAP CURVE
                if next.y > current.y:
                    vertex(current.x - current.r * cos(PI/4), current.y + current.r * sin(PI/4))
                    vertex(next.x - next.r * cos(PI/4), next.y + next.r * sin(PI/4))
                elif next.y < current.y:
                    vertex(current.x + current.r * cos(PI/4), current.y + current.r * sin(PI/4))
                    vertex(next.x + next.r * cos(PI/4), next.y + next.r * sin(PI/4))
                
                vertex(next.x, next.y + offset)
                current = next
                current_x = next.x
            else:
                current_x += self.col_width
                
        # Find Pegs in the same column (right most column in the wrapped section), and vertex() upward
        current = next
        vertex(current.x + offset, current.y)
        target = [peg for peg in wrapped if peg.x == current.x]
        if target:
            for peg in target:
                if peg.y < current.y:
                    current = peg
                    vertex(current.x + offset, current.y)
                    
        # Find the TOP of the next left column recursively from the current position
        vertex(current.x, current.y - offset)
        while True:
            if current.x - self.col_width <= 0:
                break
            next_col = [peg for peg in wrapped if peg.x == current.x - self.col_width]
            if next_col:
                next = next_col[0]
                for peg in next_col:
                    if peg.y < next.y:
                        next = peg
                        
                # FOR SMOOTH WRAP CURVE
                if next.y > current.y:
                    vertex(current.x - current.r * cos(PI/4), current.y - current.r * sin(PI/4))
                    vertex(next.x - next.r * cos(PI/4), next.y - next.r * sin(PI/4))
                elif next.y < current.y:
                    vertex(current.x + current.r * cos(PI/4), current.y - current.r * sin(PI/4))
                    vertex(next.x + next.r * cos(PI/4), next.y - next.r * sin(PI/4))
                        
                vertex(next.x, next.y - offset)
                current = next
            else:
                current.x -= self.col_width
        
        vertex(wrapped[0].x, wrapped[0].y - offset)
        
        endShape(CLOSE)
        
    
    
    def w_rap(self):
        n_pegs = len(self.pegs)
        n_wrap = n_pegs
        start = int(random(n_pegs))
        current = start
        prev = -99
        
        beginShape(QUAD)
        fill(self.colors[2])
        vertex(self.pegs[current].x, self.pegs[current].y)
        
        while n_wrap > 0:
            r = random(1)
            if r < 0.125:
                next = current - 1
            elif r < 0.25:
                next = current + self.n_rows - 1
            elif r < 0.375:
                next = current + self.n_rows
            elif r < 0.5:
                next = current + self.n_rows + 1
            elif r < 0.625:
                next = current + 1
            elif r < 0.75:
                next = current - self.n_rows + 1
            elif r < 0.875:
                next = current - self.n_rows
            else:
                next = current - self.n_rows - 1
            
            next %= n_pegs
            if next == prev:
                continue
        
            # vertex(self.pegs[current].x, self.pegs[current].y)
            vertex(self.pegs[next].x, self.pegs[next].y)
            
            if next == start:
                break
            
            prev = current
            current = next
            n_wrap -= 1
            
        endShape(CLOSE)
            
            
        
    def render(self):
        for peg in self.pegs:
            peg.render()
