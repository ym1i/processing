from peg import Peg


class PegSystem():
    
    def __init__(self, layout, style, scaling):
        self.pegs = []
        self.layout = layout
        self.style = style
        self.scaling = scaling
        self.probability = random(0.05, 0.5)
        self.n_cols = 0
        self.n_rows = 0
        self.col_width = 0
        self.colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194)]
        self.styles = ['solid', 'bulls_1', 'bulls_2', 'bulls_3']
        
    
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
        col_w = width / (n_grid + 1)
        row_h = height / (n_grid + 1)
        r = col_w * random(0.05, 0.3)
        self.col_width = col_w
        
        for i in range(n_grid):
            scale_x = self.scaling_map(i, n_grid-1, r)
                
            for j in range(n_grid):
                if random(1) < self.probability:
                    continue
                scale_y = self.scaling_map(j, n_grid-1, r)
                
                scaling = 0 if i == 0 or j == 0 or i == n_grid - 1 or j == n_grid - 1 else scale_x + scale_y
                style = self.random_style()
                self.add_peg(col_w * (i + 1), row_h * (j + 1), r + scaling, style, self.colors[0], self.colors[1])
                
                
    def tiled_layout(self, tile_1, tile_2):
    
        n_cols = tile_1 if tile_1 > tile_2 else tile_2
        col_w = width / (n_cols + 1)
        r = col_w * random(0.05, 0.3)
        self.col_width = col_w
        for i in range(n_cols):
            scale_x = self.scaling_map(i, n_cols - 1, r)
            # a = map(i, 0, n_cols - 1, 0, PI)
            # if self.scaling == 'bigger_near_center':
            #     scale_x = (r / 3) * sin(a)
            # elif self.scaling == 'smaller_near_center':
            #     scale_x = -(r / 3) * sin(a)
                
            if i % 2 == 0:
                row_h = height / (tile_1 + 1)
                for j in range(tile_1):
                    if random(1) < self.probability:
                        continue
                    scale_y = self.scaling_map(j, tile_1 - 1, r)
                    # a = map(j, 0, tile_1 - 1, 0, PI)
                    # if self.scaling == 'bigger_near_center':
                    #     scale_y = (r / 3) * sin(a) 
                    # elif self.scaling == 'smaller_near_center':
                    #     scale_y = -(r / 3) * sin(a)
                        
                    # scale_x = 0 if j == 0 or j == tile_1-1 else scale_x
                    # scale_y = 0 if i == 0 or i == n_cols-1 else scale_y
                    scaling = 0 if i == 0 or j == 0 or i == n_cols - 1 or j == tile_1 - 1 else scale_x + scale_y
                    style = self.random_style()
                    self.add_peg(col_w * (i + 1), row_h * (j + 1), r + scaling, style, self.colors[0], self.colors[1])
            else:
                row_h = height / (tile_2 + 1)
                for j in range(tile_2):
                    if random(1) < self.probability:
                        continue
                    scale_y = self.scaling_map(j, tile_2 - 1, r)
                    # a = map(j, 0, tile_2 - 1, 0, PI)
                    # if self.scaling == 'bigger_near_center':
                    #     scale_y = (r / 3) * sin(a) 
                    # elif self.scaling == 'smaller_near_center':
                    #     scale_y = -(r / 3) * sin(a)
                        
                    # scale_x = 0 if j == 0 or j == tile_2-1 else scale_x
                    # scale_y = 0 if i == 0 or i == n_cols-1 else scale_y
                    scaling = 0 if i == 0 or j == 0 or i == n_cols - 1 or j == tile_2 - 1 else scale_x + scale_y
                    style = self.random_style()
                    self.add_peg(col_w * (i + 1), row_h * (j + 1), r + scaling, style, self.colors[0], self.colors[1])
                    
    
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
        
    
    def render(self):
        for peg in self.pegs:
            peg.render()
            
            
    # def w_rap(self):
    #     n_pegs = len(self.pegs)
    #     n_wrap = n_pegs
    #     start = int(random(n_pegs))
    #     current = start
    #     prev = -99
        
    #     beginShape(QUAD)
    #     fill(self.colors[2])
    #     vertex(self.pegs[current].x, self.pegs[current].y)
        
    #     while n_wrap > 0:
    #         r = random(1)
    #         if r < 0.125:
    #             next = current - 1
    #         elif r < 0.25:
    #             next = current + self.n_rows - 1
    #         elif r < 0.375:
    #             next = current + self.n_rows
    #         elif r < 0.5:
    #             next = current + self.n_rows + 1
    #         elif r < 0.625:
    #             next = current + 1
    #         elif r < 0.75:
    #             next = current - self.n_rows + 1
    #         elif r < 0.875:
    #             next = current - self.n_rows
    #         else:
    #             next = current - self.n_rows - 1
            
    #         next %= n_pegs
    #         if next == prev:
    #             continue
        
    #         # vertex(self.pegs[current].x, self.pegs[current].y)
    #         vertex(self.pegs[next].x, self.pegs[next].y)
            
    #         if next == start:
    #             break
            
    #         prev = current
    #         current = next
    #         n_wrap -= 1
            
    #     endShape(CLOSE)
