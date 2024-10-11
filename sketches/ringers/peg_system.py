from peg import Peg
from wrap import Wrap


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
        self.pegs.append(Peg(x, y, r, style, c1, c2))
        
        
    def render(self):
        fill(self.background_color)
        rect(0, 0, width, height)
    
        wrap = Wrap(self.pegs, self.layout, 'style', self.body_color)
        wrap.mushroom()
        
        for peg in self.pegs:
            peg.render()
            
            
    def recursive(self, n_grid):
        grid = width / n_grid
        r = grid * 0.3
        for j in range(n_grid):
            for i in range(n_grid):
                rand = random(1)
                if rand < 0.5:
                    style = 'solid'
                elif rand < 0.75:
                    style = 'recursive_2'  
                else:
                    style = 'recursive_3'    
                self.add_peg(i * grid + grid / 2, j * grid + grid / 2, r, style, self.peg_color_1, self.peg_color_2)    
            
    
    def grid_layout(self, n_grid):
        col_w = width / (n_grid + 1)
        row_h = height / (n_grid + 1)
        # r = col_w * random(0.05, 0.3)
        r = map(n_grid, 3, 5, col_w * 0.25, col_w * 0.3)
        # r = col_w * 0.3
        
        for j in range(n_grid):
            scale_x = self.scaling_map(j, n_grid-1, r)
                
            for i in range(n_grid):
                # if random(1) < 0.1:
                #     continue
                scale_y = self.scaling_map(i, n_grid-1, r)
                
                scaling = 0 if i == 0 or j == 0 or i == n_grid - 1 or j == n_grid - 1 else scale_x + scale_y
                # style = self.random_style()
                style = 'solid'
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
        elif self.layout == 'grid_7':
            self.grid_layout(7)
        elif self.layout == 'grid_8':
            self.grid_layout(8)
        elif self.layout == 'grid_9':
            self.grid_layout(9)
        elif self.layout == 'grid_10':
            self.grid_layout(10)
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
        elif self.layout == 'recursive_2':
            self.recursive(2)
            
            

  
