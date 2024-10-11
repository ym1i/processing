from peg import Peg
from forces import Repeller, Attractor, Gravity


class PegSystem():
    
    def __init__(self, layout, scaling, body_color, background_color, peg_color_1, peg_color_2):
        self.pegs = []
        self.layout = layout
        self.scaling = scaling
        self.body_color = body_color
        self.background_color = background_color
        self.peg_color_1 = peg_color_1
        self.peg_color_2 = peg_color_2
        
    
    def add_peg(self, x, y, r, style, c1, c2):
        self.pegs.append(Peg(x, y, r, style, c1, c2, 1.0))
        
    
    def set_forces(self):
        self.gravity = Gravity(0.01)
        attractor_id = int(random(len(self.pegs)))
        repeller_id = (attractor_id + int(random(len(self.pegs) - 1))) % len(self.pegs)
        self.attractor = Attractor(self.pegs[attractor_id].x, self.pegs[attractor_id].y, self.pegs[attractor_id].r)
        self.repeller = Repeller(self.pegs[repeller_id].x, self.pegs[repeller_id].y, self.pegs[repeller_id].r)
        
    
    def add_forces(self):
        # self.apply_repeller(self.repeller)
        self.apply_gravity(self.gravity)
        self.apply_attractor(self.attractor)
        for peg in self.pegs:
            peg.update()
        
        
    def render(self):
        fill(self.background_color)
        rect(0, 0, width, height)
        fill(self.body_color)
        self.wrap()
        
        
        self.repeller.display()
        for peg in self.pegs:
            peg.render()
        self.attractor.display()
            
    
    def grid_layout(self, n_grid):
        col_w = width / (n_grid + 1)
        row_h = height / (n_grid + 1)
        r = col_w * random(0.05, 0.3)
        
        for i in range(n_grid):
            scale_x = self.scaling_map(i, n_grid-1, r)
                
            for j in range(n_grid):
                if random(1) < 0.1:
                    continue
                scale_y = self.scaling_map(j, n_grid-1, r)
                
                scaling = 0 if i == 0 or j == 0 or i == n_grid - 1 or j == n_grid - 1 else scale_x + scale_y
                style = self.random_style()
                self.add_peg(col_w * (i + 1), row_h * (j + 1), r + scaling, style, self.peg_color_1, self.peg_color_2)
                
                
    def tiled_layout(self, tile_1, tile_2):
    
        n_cols = tile_1 if tile_1 > tile_2 else tile_2
        col_w = width / (n_cols + 1)
        r = col_w * random(0.05, 0.3)
        for i in range(n_cols):
            scale_x = self.scaling_map(i, n_cols - 1, r)
    
            if i % 2 == 0:
                row_h = height / (tile_1 + 1)
                for j in range(tile_1):
                    if random(1) < 0.1:
                        continue
                    scale_y = self.scaling_map(j, tile_1 - 1, r)
                   
                    scaling = 0 if i == 0 or j == 0 or i == n_cols - 1 or j == tile_1 - 1 else scale_x + scale_y
                    style = self.random_style()
                    self.add_peg(col_w * (i + 1), row_h * (j + 1), r + scaling, style, self.colors[0], self.colors[1])
            else:
                row_h = height / (tile_2 + 1)
                for j in range(tile_2):
                    if random(1) < 0.1:
                        continue
                    scale_y = self.scaling_map(j, tile_2 - 1, r)
                    
                    scaling = 0 if i == 0 or j == 0 or i == n_cols - 1 or j == tile_2 - 1 else scale_x + scale_y
                    style = self.random_style()
                    self.add_peg(col_w * (i + 1), row_h * (j + 1), r + scaling, style, self.colors[0], self.colors[1])
                    
    
    def wrap(self):
        prob = 0.8
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
    
        
    def random_style(self):
        styles = ['solid', 'bulls_1', 'bulls_2', 'bulls_3']
        rand = random(1)
        if rand < 0.05:
            return styles[1]
        elif rand < 0.1:
            return styles[2]
        elif rand < 0.15:
            return styles[3]
        else:
            return styles[0]
        
    
    def scaling_map(self, i, n, radius):
        a = map(i, 0, n, 0, PI)
        if self.scaling == 'bigger_near_center':
            return (radius / 3) * sin(a)
        elif self.scaling == 'smaller_near_center':
            return -(radius / 3) * sin(a)
        else:
            return 0
        
    
    def set_layout(self):
        if self.layout == 'grid_3':
            self.grid_layout(3)
        elif self.layout == 'grid_4':
            self.grid_layout(4)
        elif self.layout == 'grid_5':
            self.grid_layout(5)
        elif self.layout == 'grid_6':
            self.grid_layout(6)
        elif self.layout == 'tiled_23':
            self.tiled_layout(2, 3)
        elif self.layout == 'tiled_32':
            self.tiled_layout(3, 2)
        elif self.layout == 'tiled_34':
            self.tiled_layout(3, 4)
        elif self.layout == 'tiled_43':
            self.tiled_layout(4, 3)
        elif self.layout == 'tiled_45':
            self.tiled_layout(4, 5)
        elif self.layout == 'tiled_54':
            self.tiled_layout(5, 4)
            
            
    def apply_force(self, force):
        for peg in self.pegs:
            peg.apply_force(force)
            
            
    def apply_gravity(self, gravity):
        for peg in self.pegs:
            force = gravity.gravity(peg)
            peg.apply_force(force)
            
    def apply_attractor(self, attractor):
        for peg in self.pegs:
            force = attractor.attract(peg)
            peg.apply_force(force)
            
    def apply_repeller(self, repeller):
        for peg in self.pegs:
            force = repeller.repel(peg)
            peg.apply_force(force)
            
            

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
    
    # -------------------------------------------------------------------------------------------------
    
    # def w_rap(self):
    #     prob = random(0.5, 1)
    #     wrapped = []
    #     for peg in self.pegs:
    #         if random(1) < 0.9:
    #             wrapped.append(peg)
    #     if not wrapped:
    #         wrapped.append(self.pegs[0])
        
    #     beginShape()
    #     fill(self.colors[2])
    #     strokeWeight(2)
        
    #     offset = self.pegs[0].r
        
    #     # Find Pegs in the same column (LEFT most column in the wrapped section), and vertex() downward
    #     current = wrapped[0]
    #     vertex(current.x - offset, current.y)
    #     target = [peg for peg in wrapped if peg.x == current.x]
    #     if target:
    #         for peg in target:
    #             if peg.y > current.y:
    #                 current = peg    
    #                 vertex(current.x - offset, current.y)        
    #     vertex(current.x, current.y + offset)
        
    #     # Find the bottom of the next right column recursively from the current position
    #     next = current
    #     current_x = current.x
    #     while True:
    #         if current_x + self.col_width >= width:
    #             break
    #         next_col = [peg for peg in wrapped if peg.x == current.x + self.col_width]
    #         if next_col:
    #             next = next_col[0]
    #             for peg in next_col:
    #                 if peg.y > next.y:
    #                     next = peg
                
    #             # FOR SMOOTH WRAP CURVE
    #             if next.y > current.y:
    #                 vertex(current.x - current.r * cos(PI/4), current.y + current.r * sin(PI/4))
    #                 vertex(next.x - next.r * cos(PI/4), next.y + next.r * sin(PI/4))
    #             elif next.y < current.y:
    #                 vertex(current.x + current.r * cos(PI/4), current.y + current.r * sin(PI/4))
    #                 vertex(next.x + next.r * cos(PI/4), next.y + next.r * sin(PI/4))
                
    #             vertex(next.x, next.y + offset)
    #             current = next
    #             current_x = next.x
    #         else:
    #             current_x += self.col_width
                
    #     # Find Pegs in the same column (right most column in the wrapped section), and vertex() upward
    #     current = next
    #     vertex(current.x + offset, current.y)
    #     target = [peg for peg in wrapped if peg.x == current.x]
    #     if target:
    #         for peg in target:
    #             if peg.y < current.y:
    #                 current = peg
    #                 vertex(current.x + offset, current.y)
                    
    #     # Find the TOP of the next left column recursively from the current position
    #     vertex(current.x, current.y - offset)
    #     while True:
    #         if current.x - self.col_width <= 0:
    #             break
    #         next_col = [peg for peg in wrapped if peg.x == current.x - self.col_width]
    #         if next_col:
    #             next = next_col[0]
    #             for peg in next_col:
    #                 if peg.y < next.y:
    #                     next = peg
                        
    #             # FOR SMOOTH WRAP CURVE
    #             if next.y > current.y:
    #                 vertex(current.x - current.r * cos(PI/4), current.y - current.r * sin(PI/4))
    #                 vertex(next.x - next.r * cos(PI/4), next.y - next.r * sin(PI/4))
    #             elif next.y < current.y:
    #                 vertex(current.x + current.r * cos(PI/4), current.y - current.r * sin(PI/4))
    #                 vertex(next.x + next.r * cos(PI/4), next.y - next.r * sin(PI/4))
                        
    #             vertex(next.x, next.y - offset)
    #             current = next
    #         else:
    #             current.x -= self.col_width
        
    #     vertex(wrapped[0].x, wrapped[0].y - offset)
        
    #     endShape(CLOSE)
