from peg import Peg


class PegSystem():
    
    def __init__(self, layout, scaling, cell, n_grid, radius):
        self.pegs = []
        self.layout = layout
        self.scaling = scaling
        self.cell = cell
        self.probability = random(0.05, 0.5)
        self.n_cols = 0
        self.n_rows = 0
        self.col_width = 0
        self.radius = radius
        self.colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194)]
        self.styles = ['solid', 'bulls_1', 'bulls_2', 'bulls_3']
        
        self.set_layout()
        
    
    def add_peg(self, x, y, r, style, c1, c2):
        self.pegs.append(Peg(x, y, r, style, c1, c2))
    
    
    def grid_layout(self, n_grid):
        col_w = self.cell.w / (n_grid + 1)
        row_h = self.cell.h / (n_grid + 1)
        # r = col_w * random(0.05, 0.3)
        self.col_width = col_w
        
        for i in range(n_grid):
            scale_x = self.scaling_map(i, n_grid-1, self.radius)
            
            for j in range(n_grid):
                if random(1) < self.probability:
                    continue
                scale_y = self.scaling_map(j, n_grid-1, self.radius)
                
                scaling = 0 if i == 0 or j == 0 or i == n_grid - 1 or j == n_grid - 1 else scale_x + scale_y
                style = self.random_style()
                self.add_peg(self.cell.x + col_w * (i + 1), self.cell.y + row_h * (j + 1), self.radius + scaling, style, self.colors[0], self.colors[1])
                
    
    def wrap(self):
        prob = random(0.5, 1)
        wrapped = []
        for peg in self.pegs:
            if random(1) < prob:
                wrapped.append(peg)
        if not wrapped:
            wrapped.append(self.pegs[0])
        
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
        
        
    def set_layout(self):
        if self.layout == 'grid_3':
            self.grid_layout(3)
            self.n_cols = 3
            self.n_rows = 3
            # self.radius = self.cell.w / (self.n_cols + 1) * random(0.05, 0.3) if self.cell.w < self.cell.h else self.cell.h / (self.n_cols + 1) * random(0.05, 0.3)
        elif self.layout == 'grid_4':
            self.grid_layout(4)
            self.n_cols = 4
            self.n_rows = 4
            # self.radius = self.cell.w / (self.n_cols + 1) * random(0.05, 0.3) if self.cell.w < self.cell.h else self.cell.h / (self.n_cols + 1) * random(0.05, 0.3)
        elif self.layout == 'grid_5':
            self.grid_layout(5)
            self.n_cols = 5
            self.n_rows = 5
            # self.radius = self.cell.w / (self.n_cols + 1) * random(0.05, 0.3) if self.cell.w < self.cell.h else self.cell.h / (self.n_cols + 1) * random(0.05, 0.3)
        elif self.layout == 'grid_6':
            self.grid_layout(6)
            self.n_cols = 6
            self.n_rows = 6
            # self.radius = self.cell.w / (self.n_cols + 1) * random(0.05, 0.3) if self.cell.w < self.cell.h else self.cell.h / (self.n_cols + 1) * random(0.05, 0.3)
        
                
    def random_style(self):
        rand = random(1)
        if rand < 0.05:
            return self.styles[1]
        elif rand < 0.1:
            return self.styles[2]
        elif rand < 0.15:
            return self.styles[3]
        else:
            return self.styles[0]
        
    
    def scaling_map(self, i, n, radius):
        a = map(i, 0, n, 0, PI)
        if self.scaling == 'bigger_near_center':
            return (radius / 3) * sin(a)
        elif self.scaling == 'smaller_near_center':
            return -(radius / 3) * sin(a)
        else: 
            return 0
        
    
    def render(self):
        for peg in self.pegs:
            peg.render()
