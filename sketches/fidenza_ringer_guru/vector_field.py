from random import randint
from grid import Grid
from element import Element
from palette import Palette


class VectorField():
    
    def __init__(self, width, height, grid_size, step_size):
        self.grid_size = grid_size
        self.step_size = step_size
        self.n_cols = width / grid_size
        self.n_rows = height / grid_size
        self.palette = Palette()
        self.grid = [[0 for i in range(self.n_cols)] for j in range(self.n_rows)]
        self.elements = []
        
    def add_vector(self, i, j, step_size):
        noise_value = noise(i * 0.01, j * 0.01) # perlin noise works best between 0.005 < step < 0.03
        angle = map(noise_value, 0, 1, -TAU, TAU)
        
        start = 0
        # start = -TAU
        stop = TAU
        _x = map(i, 0, self.n_cols, start, stop)
        _y = map(j, 0, self.n_rows, start, stop)
        
        x = _y
        y = -_x
        
        # x = PI * sin(_y)          
        # y = _x 
        # x = log(abs(_y))         
        # y = log(abs(_x))
        # x = sin(_y) + cos(_y)     
        # y = sin(_x) + cos(_x)
        
        angle = PVector(x, y).heading()
        
        vec = PVector(step_size * cos(angle), step_size * sin(angle))
        inv = PVector(step_size * cos(angle + PI), step_size * sin(angle + PI))
        
        return vec, inv
    
    
    def create_field(self, step_size=40):
         for j in range(self.n_rows):
            for i in range(self.n_cols):
                vec, inv = self.add_vector(i, j, step_size)
                self.grid[j][i] = Grid(i * self.grid_size, j * self.grid_size, vec, inv)
        
    
    def create_element(self, ix, iy, n_steps):
        element = Element(self.palette)
        backward, checked = self.travel_backward(ix, iy, n_steps)
        forward, checked = self.travel_forward(ix, iy, n_steps)
        
        if checked:
            return False
        
        for v in reversed(backward):
            # r = randint(10, 30)
            r = randint(50, 80)
            element.add_peg(PVector(v.x, v.y), r)
        for v in forward:
            if v == forward[0]:
                continue
            # r = randint(10, 30)
            r = randint(50, 80)
            element.add_peg(PVector(v.x, v.y), r)
      
        if len(element.pegs) % 2 == 0:
              element.pegs.pop(-1)
        
        return element
            
            
    def travel_forward(self, ix, iy, n_steps):
        vertices = []
        checked = False
        i = int(ix / self.grid_size) 
        j = int(iy / self.grid_size)
        x = self.grid[j][i].x
        y = self.grid[j][i].y
        
        for c in range(n_steps):
            r = randint(15, 25)
            vertices.append(PVector(x, y))
            i = int(x / self.grid_size) 
            j = int(y / self.grid_size)    
            i = constrain(i, 0, self.n_cols - 1)
            j = constrain(j, 0, self.n_rows - 1)
            
            if self.grid[j][i].checked:
                checked = True
                return vertices, checked
            
            vec = self.grid[j][i].vec
            x = x + vec.x
            y = y + vec.y
            
            if x < 10 or x > width - 10 or y < 10 or y > height - 10:
                if c < 3:
                    checked = True
                break
        return vertices, checked
    
    
    def travel_backward(self, ix, iy, n_steps):
        vertices = []
        checked = False
        i = int(ix / self.grid_size) 
        j = int(iy / self.grid_size)
        x = self.grid[j][i].x
        y = self.grid[j][i].y
        
        for c in range(n_steps):
            r = randint(15, 25)
            vertices.append(PVector(x, y))
            i = int(x / self.grid_size) 
            j = int(y / self.grid_size)    
            i = constrain(i, 0, self.n_cols - 1)
            j = constrain(j, 0, self.n_rows - 1)
            
            if self.grid[j][i].checked:
                checked = True
                return vertices, checked
            
            inv = self.grid[j][i].inv
            x = x + inv.x
            y = y + inv.y
            
            if x < 10 or x > width - 10 or y < 10 or y > height - 10:
                if c < 3:
                    checked = True
                break
        
        return vertices, checked
    
    
    def render_grid(self):
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                # stroke(self.palette.random_color())
                stroke(0)
                strokeWeight(1)
                if random(0, 1) < 0.2:
                    rect(self.grid[j][i].x, self.grid[j][i].y, self.grid_size, self.grid_size)
    
    
