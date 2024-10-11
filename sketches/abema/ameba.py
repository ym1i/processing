from random import randint
import time
from peg import Peg
from wrapper import Wrapper


class Ameba():
    
    def __init__(self, x, y, r, r_peg, n, palette, type):
        self.pegs = []
        self.x = x
        self.y = y
        self.r = r
        self.r_peg = r_peg
        self.n_pegs = n
        self.type = type
        self.palette = palette
        
        
    def birth(self):
        self.inner_wrap = Wrapper()
        self.outer_wrap = Wrapper()
        self.outer_wrap_2 = Wrapper()
        
        
        if self.type == 'regular':
            self.pegs = self.deformed_circle(self.x, self.y, self.r, self.n_pegs, 0)
            self.inner_wrap.ameba_wrap(self.pegs)
            self.outer_wrap.wrap(self.pegs)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 30, 20, 0)
            self.outer_wrap_2.wrap(outer_pegs_2) 
            
        elif self.type == 'large':
            self.r_peg *= 0.8
            inner_pegs = self.deformed_circle(self.x, self.y, self.r, self.n_pegs, 0)
            outer_pegs = self.deformed_circle(self.x, self.y, self.r + self.r_peg * 2, self.n_pegs, PI / self.n_pegs)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 50, 20, 0)
            for i in range(self.n_pegs):
                self.pegs.append(inner_pegs[i])
                self.pegs.append(outer_pegs[i])
            self.inner_wrap.ameba_wrap(self.pegs)
            self.outer_wrap.wrap(outer_pegs)
            self.outer_wrap_2.wrap(outer_pegs_2) 
            
        elif self.type == 'grid5':
            self.pegs = self.grid_layout(5, 5)
            outer_pegs = self.deformed_circle(self.x, self.y, self.r, 20, 0)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 30, 20, 0)
            self.inner_wrap.grid_wrap(self.pegs, 5, 5, toggle=True)
            self.outer_wrap.wrap(outer_pegs)  
            self.outer_wrap_2.wrap(outer_pegs_2) 
            
        elif self.type == 'grid3':
            self.pegs = self.grid_layout(3, 3)
            self.inner_wrap.grid_wrap(self.pegs, 3, 3, toggle=True)
            outer_pegs = self.deformed_circle(self.x, self.y, self.r, 20, 0)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 30, 20, 0)
            self.outer_wrap.wrap(outer_pegs)
            self.outer_wrap_2.wrap(outer_pegs_2) 
    
        elif self.type == 'grid4':
            self.pegs = self.grid_layout(4, 4)
            self.inner_wrap.grid_wrap(self.pegs, 4, 4, toggle=False, even=True)
            outer_pegs = self.deformed_circle(self.x, self.y, self.r, 20, 0)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 30, 20, 0)
            self.outer_wrap.wrap(outer_pegs)   
            self.outer_wrap_2.wrap(outer_pegs_2) 
            
        elif self.type == 'grid3mix':
            
            self.pegs = self.mixed_grid(3, 3)

            self.inner_wrap.ameba_wrap(self.pegs)
            outer_pegs = self.deformed_circle(self.x, self.y, self.r, 20, 0)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 30, 20, 0)
            self.outer_wrap.wrap(outer_pegs) 
            self.outer_wrap_2.wrap(outer_pegs_2) 
     
        elif self.type == 'grid4mix':
            self.pegs = self.mixed_grid(4, 4)

            self.inner_wrap.ameba_wrap(self.pegs)
            outer_pegs = self.deformed_circle(self.x, self.y, self.r, 20, 0)
            outer_pegs_2 = self.deformed_circle(self.x, self.y, self.r + 30, 20, 0)
            self.outer_wrap.wrap(outer_pegs) 
            self.outer_wrap_2.wrap(outer_pegs_2) 
                 
    
    def render(self, body_color, peg_color):
        if self.outer_wrap_2:
            self.outer_wrap_2.render(self.palette.random_color(), no_stroke=True)
        self.outer_wrap.render(self.palette.random_color(), no_stroke=True)
        self.inner_wrap.render(body_color, no_stroke=False)
        
        for peg in self.pegs:
            peg.render(peg_color, no_stroke=False)
        
    
    def deformed_circle(self, x, y, r, n_points, offset):
        pegs = []
        scale = r / 2
        resolution = 0.002
        
        for i in range(n_points):
            a = map(i, 0, n_points - 1, TAU / n_points + offset, TAU + offset)
            _x = x + r  * cos(a)
            _y = y + r  * sin(a)
            n = map(noise(_x * resolution, _y * resolution), 0, 1, -scale, scale)
            pegs.append(Peg(_x + n, _y + n, self.r_peg))
        
        return pegs
    
    
    def grid_layout(self, n_cols, n_rows):
        pegs = []
        margin = 300
        grid_width = (width - margin) / (n_cols + 1)
        grid_height = (height - margin) / (n_rows + 1)
        r = grid_width * random(0.15, 0.2)
        ratio = 1
        n_scale = grid_width / ratio # gird_width / 2 would be better for grid_5
        resolution = 0.8
        
        fill(0)
        text('[ GRID_WIDTH: {} | N_SCALE: grid_width / {} ({:.1f})  |  RESOLUTION: {}  |  R: {:.1f}  |  PALETTE: {} | TIME: {}]'.format(grid_width, ratio, n_scale, resolution, r, self.palette.name, time.time()), 15, height - 15)
        
        for j in range(1, n_rows + 1):                
            for i in range(1, n_cols + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
                
        return pegs
    
    
    def mixed_grid(self, n_cols, n_rows):
        pegs = []
        margin = 300
        grid_width = (width - margin) / (n_cols + 1)
        grid_height = (height - margin) / (n_rows + 1)
        r = grid_width * random(0.15, 0.3)
        n_scale = grid_width / 1
        resolution = 0.8
        
        fill(0)
        text('[ n_scale: grid_width / 1 ({:.1f})  |  resolution: {}  |  r: {:.1f}  |  palette: {} ]'.format(n_scale, resolution, r, self.palette.name), width - 600, height - 15)
        
        big_peg = randint(0, 3)
        if big_peg == 0:
            if big_peg % 2 == 0:
                i = n_cols / 2.0
            else:
                i = n_cols / 2.0 + 1
            if big_peg < 2:
                j = n_rows / 2.0
            else:
                j = n_rows / 2.0 + 1
            
            n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
            pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r * 3))  # BIG PEG
            i = n_cols
            for j in range(1, n_rows + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            j = n_rows
            for i in reversed(range(1, n_cols)):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
        
        elif big_peg == 1:
            if big_peg % 2 == 0:
                i = n_cols / 2.0
            else:
                i = n_cols / 2.0 + 1
            if big_peg < 2:
                j = n_rows / 2.0
            else:
                j = n_rows / 2.0 + 1
            n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
            pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r * 3))   # BIG PEG
            
            j = n_rows
            for i in reversed(range(1, n_cols + 1)):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            i = 1
            for j in reversed(range(1, n_rows)):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
        
        elif big_peg == 3:
            if big_peg % 2 == 0:
                i = n_cols / 2.0
            else:
                i = n_cols / 2.0 + 1
            if big_peg < 2:
                j = n_rows / 2.0
            else:
                j = n_rows / 2.0 + 1
            n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
            pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r * 3)) # BIG PEG
            
            i = 1
            for j in reversed(range(1, n_rows + 1)):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            j = 1
            for i in range(2, n_rows + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
                
        elif big_peg == 2:
            if big_peg % 2 == 0:
                i = n_cols / 2.0
            else:
                i = n_cols / 2.0 + 1
            if big_peg < 2:
                j = n_rows / 2.0
            else:
                j = n_rows / 2.0 + 1
            n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
            pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r * 3))  # BIG PEG
            j = 1
            for i in range(1, n_rows + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            i = n_cols
            for j in range(2, n_rows + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
        
        return pegs
    
    
   
            
