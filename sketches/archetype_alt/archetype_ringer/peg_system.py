from peg import Peg


class PegSystem():
    
    def __init__(self, layout, scaling, cell, n_grid, radius, body_color, bg_color):
        self.pegs = []
        self.layout = layout
        self.scaling = scaling
        self.cell = cell
        self.n_grid = n_grid
        self.grid_x = cell.x
        self.grid_y = cell.y
        self.grid_w = cell.w
        # self.probability = random(0.05, 0.5)
        self.probability = random(0.05, 0.1)
        self.radius = radius
        self.colors = [color(0, 0, 0), color(255, 255, 255), color(248, 198, 54), color(45, 132, 194)]
        self.styles = ['solid', 'bulls_1', 'bulls_2', 'bulls_3']
        self.body_color = body_color
        self.bg_color = bg_color
        
        self.square_grid(n_grid)
        # self.grid_layout(n_grid)
        
    
    def add_peg(self, x, y, r, style, c1, c2):
        self.pegs.append(Peg(x, y, r, style, c1, c2))
    
    
    def square_grid(self, n_grid):
        col_w = min(self.cell.w, self.cell.h) / (n_grid + 1)
        self.grid_w = col_w * n_grid
        offset = (max(self.cell.w, self.cell.h) - min(self.cell.w, self.cell.h)) / 2
        
        self.grid_x = self.cell.x + col_w if self.cell.w < self.cell.h else self.cell.x + col_w + offset
        self.grid_y = self.cell.y + col_w if self.cell.h < self.cell.w else self.cell.y + col_w + offset
        
        for i in range(n_grid):
            scale_x = self.scaling_map(i, n_grid-1, self.radius)
            
            for j in range(n_grid):
                # if random(1) < self.probability:
                #     continue
                scale_y = self.scaling_map(j, n_grid-1, self.radius)
                
                scaling = 0 if i == 0 or j == 0 or i == n_grid - 1 or j == n_grid - 1 else scale_x + scale_y
                style = self.random_style()
                if self.cell.w > self.cell.h:
                    self.add_peg(self.cell.x + col_w * (i + 1) + offset, self.cell.y + col_w * (j + 1), self.radius + scaling, style, self.colors[0], self.colors[1])
                else:    
                    self.add_peg(self.cell.x + col_w * (i + 1), self.cell.y + col_w * (j + 1) + offset, self.radius + scaling, style, self.colors[0], self.colors[1])
    
    def grid_layout(self, n_grid):
        col_w = self.cell.w / (n_grid + 1)
        row_h = self.cell.h / (n_grid + 1)
        
        for i in range(n_grid):
            scale_x = self.scaling_map(i, n_grid-1, self.radius)
            
            for j in range(n_grid):
                # if random(1) < self.probability:
                #     continue
                scale_y = self.scaling_map(j, n_grid-1, self.radius)
                
                scaling = 0 if i == 0 or j == 0 or i == n_grid - 1 or j == n_grid - 1 else scale_x + scale_y
                style = self.random_style()
                self.add_peg(self.cell.x + col_w * (i + 1), self.cell.y + row_h * (j + 1), self.radius + scaling, style, self.colors[0], self.colors[1])
                
                
    def wrap(self):
        prob = 0.6
        wrapped = []
        for peg in self.pegs:
            if random(1) < prob:
                wrapped.append(peg)
        if not wrapped:
            wrapped.append(self.pegs[0])
        
        # Find edges
        left_top = 0
        left_bottom = 0
        right_top = 0
        right_bottom = 0
        left_most = 0
        right_most = 0
        top_most = 0
        bottom_most = 0
        
        
        for i, peg in enumerate(wrapped):
            if peg.x <= wrapped[left_top].x and peg.y <= wrapped[left_top].y:
                left_top = i
            if peg.x <= wrapped[left_bottom].x and peg.y >= wrapped[left_bottom].y:
                left_bottom = i
            if peg.x >= wrapped[right_top].x and peg.y <= wrapped[right_top].y:
                right_top = i
            if peg.x >= wrapped[right_bottom].x and peg.y >= wrapped[right_bottom].y:
                right_bottom = i
            if peg.x < wrapped[left_most].x:
                left_most = i
            if peg.x > wrapped[right_most].x:
                right_most = i
            if peg.y < wrapped[top_most].y:
                top_most = i
            if peg.y > wrapped[bottom_most].y:
                bottom_most = i
                
        beginShape()
        fill(self.body_color)
        strokeWeight(2)
        r = wrapped[0].r
        offset = r * cos(PI/4)
        
        vertex(wrapped[left_top].x - r, wrapped[left_top].y)
        vertex(wrapped[left_most].x - r, wrapped[left_most].y)
        vertex(wrapped[left_bottom].x - r, wrapped[left_bottom].y)
        
        if wrapped[left_bottom].y < wrapped[bottom_most].y:
            vertex(wrapped[left_bottom].x - offset, wrapped[left_bottom].y + offset)
            vertex(wrapped[bottom_most].x - offset, wrapped[bottom_most].y + offset)
            vertex(wrapped[bottom_most].x, wrapped[bottom_most].y + r)
        else:    
            vertex(wrapped[left_bottom].x, wrapped[left_bottom].y + r)
            vertex(wrapped[bottom_most].x, wrapped[bottom_most].y + r)
        
        
        if wrapped[bottom_most].y > wrapped[right_bottom].y:
            vertex(wrapped[bottom_most].x + offset, wrapped[bottom_most].y + offset)
            vertex(wrapped[right_bottom].x + offset, wrapped[right_bottom].y + offset)
            vertex(wrapped[right_bottom].x + r, wrapped[right_bottom].y)
        else:
            vertex(wrapped[right_bottom].x, wrapped[right_bottom].y + r)
            vertex(wrapped[right_bottom].x + r, wrapped[right_bottom].y)
    
        
        if wrapped[right_bottom].x < wrapped[right_most].x:
            vertex(wrapped[right_bottom].x + offset, wrapped[right_bottom].y + offset)
            vertex(wrapped[right_most].x + offset, wrapped[right_most].y + offset)
            vertex(wrapped[right_most].x + r, wrapped[right_most].y)
        else:
            vertex(wrapped[right_most].x + r, wrapped[right_most].y)
        
        if wrapped[right_most].x > wrapped[right_top].x:
            vertex(wrapped[right_most].x + offset, wrapped[right_most].y - offset)
            vertex(wrapped[right_top].x + offset, wrapped[right_top].y - offset)
            vertex(wrapped[right_top].x, wrapped[right_top].y - r)
        else:
            vertex(wrapped[right_top].x + r, wrapped[right_top].y)
            vertex(wrapped[right_top].x, wrapped[right_top].y - r)
        
        if wrapped[right_top].y > wrapped[top_most].y:
            vertex(wrapped[right_top].x + offset, wrapped[right_top].y - offset)
            vertex(wrapped[top_most].x + offset, wrapped[top_most].y - offset)
            vertex(wrapped[top_most].x, wrapped[top_most].y - r)
        else:
            vertex(wrapped[right_top].x, wrapped[right_top].y - r)
            vertex(wrapped[top_most].x, wrapped[top_most].y - r)
        
        if wrapped[top_most].y < wrapped[left_top].y:
            vertex(wrapped[top_most].x - offset, wrapped[top_most].y - offset)
            vertex(wrapped[left_top].x - offset, wrapped[left_top].y - offset)
        else:
            vertex(wrapped[left_top].x, wrapped[left_top].y - r)
        
        endShape(CLOSE)
    
    
    def w_rap(self):
        prob = random(0.7, 1)
        wrapped = []
        for peg in self.pegs:
            # if random(1) < prob:
            #     wrapped.append(peg)
            wrapped.append(peg)
        if not wrapped:
            wrapped.append(self.pegs[0])
            
        beginShape()
        fill(self.body_color)
        stroke(0)
        strokeWeight(1)
        
        offset = self.pegs[0].r
        grid_width = min(self.cell.w, self.cell.h) / (self.n_grid + 1)
        
        current = wrapped[0]
        next = current
        current_y = current.y
        vertex(current.x - offset, current.y)
        
        # LEFT
        while True:
            if current_y + grid_width > self.grid_y + self.grid_w:
                break
            next_row = [peg for peg in wrapped if peg.y == current.y + grid_width]
            if next_row:
                next = next_row[0]
                for peg in next_row:
                    if peg.x < next.x:
                        next = peg
                
                # FOR SMOOTH WRAP CURVE
                if next.x > current.x:
                    vertex(current.x - current.r * cos(PI/4), current.y + current.r * sin(PI/4))
                    vertex(next.x - next.r * cos(PI/4), next.y + next.r * sin(PI/4))
                elif next.x < current.x:
                    vertex(current.x + current.r * cos(PI/4), current.y + current.r * sin(PI/4))
                    vertex(next.x - next.r * cos(PI/4), next.y - next.r * sin(PI/4))

                vertex(next.x - offset, next.y)
                current = next
                current_y = next.y
            else:
                current_y += grid_width
                
        
        #BOTTOM
        vertex(current.x, current.y + offset)
        current_x = current.x
        while True:
            if current_x + grid_width > self.grid_x + self.grid_w:
                break
            next_col = [peg for peg in wrapped if peg.x == current.x + grid_width]
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
                current_x += grid_width
                
        
        #RIGHT
        vertex(current.x + offset, current.y)
        current_y = current.y
        while True:
            if current_y - grid_width < self.grid_y:
                break
            next_row = [peg for peg in wrapped if peg.y == current.y - grid_width]
            if next_row:
                next = next_row[0]
                for peg in next_row:
                    if peg.x > next.x:
                        next = peg
                
                # FOR SMOOTH WRAP CURVE
                if next.x > current.x:
                    vertex(current.x + current.r * cos(PI/4), current.y + current.r * sin(PI/4))
                    vertex(next.x + next.r * cos(PI/4), next.y + next.r * sin(PI/4))
                elif next.x < current.x:
                    vertex(current.x + current.r * cos(PI/4), current.y - current.r * sin(PI/4))
                    vertex(next.x + next.r * cos(PI/4), next.y - next.r * sin(PI/4))

                vertex(next.x + offset, next.y)
                current = next
                current_y = next.y
            else:
                current_y -= grid_width
                
                
        #TOP
        vertex(current.x, current.y - offset)
        current_x = current.x
        while True:
            if current_x - grid_width < self.grid_x:
                break
            next_col = [peg for peg in wrapped if peg.x == current.x - grid_width]
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
                current_x = next.x
            else:
                current_x -= grid_width
        
        vertex(wrapped[0].x, wrapped[0].y - offset)
                
        endShape(CLOSE)
                
    
    def w_rap(self):
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
        col_width = min(self.cell.w, self.cell.h) / (self.n_grid + 1)
        
        # Find Pegs in the same column (LEFT most column in the wrapped section), and vertex() downward
        current = wrapped[0]
        # print 'cur.x: ', current.x
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
            if current_x + col_width >= width:
                break
            next_col = [peg for peg in wrapped if peg.x == current.x + col_width]
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
                current_x += col_width
                
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
            if current.x - col_width <= 0:
                break
            next_col = [peg for peg in wrapped if peg.x == current.x - col_width]
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
                current.x -= col_width
        
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
        else: 
            return 0
        
    
    def render(self):
        self.wrap()
        for peg in self.pegs:
            peg.render()
