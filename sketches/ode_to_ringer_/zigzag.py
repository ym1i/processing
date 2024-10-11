from peg import Peg
from wrapper import Wrapper


class Zigzag(Wrapper):
    
    def __init__(self, pegs, id, n_cols, n_rows, palette):
        self.pegs = pegs
        self.element_id = id
        self.vertices = []
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.r = width / (self.n_cols + 1) / 2
        self.palette = palette
                        
    
    def wrap_3_1(self, start, stop):
        for j in range(start, stop + 1):
            if j % 2 == 0:
               for i in range(self.n_cols): 
                   id = j * self.n_cols + i
                   if i % 3 == 0:
                       self.ark(PI, TAU, id, self.r, deformed=True)
                       self.element_id.append(id)
                   elif i % 3 == 1:
                       self.ark(PI, HALF_PI, id, self.r, deformed=True)
                   elif i % 3 == 2:
                       self.ark(HALF_PI, 0, id, self.r, deformed=True)
            elif j % 2 == 1:
                for i in reversed(range(self.n_cols)):
                    id = j * self.n_cols + i
                    if i % 3 == 0:
                        self.ark(TAU, PI, id, self.r, deformed=True)
                    elif i % 3 == 1:
                        self.ark(HALF_PI, PI, id, self.r, deformed=True)
                        self.element_id.append(id)
                    elif i % 3 == 2:
                        self.ark(0, HALF_PI, id, self.r, deformed=True)
                        self.element_id.append(id)
                        
    def wrap_3_1a(self, start, stop):
        for j in range(start, stop + 1):
            if j % 2 == 0:
               for i in range(self.n_cols): 
                   id = j * self.n_cols + i
                   if i % 3 == 0:
                       self.ark(PI, TAU, id, self.r, deformed=True)
                       self.element_id.append(id)
                   elif i % 3 == 1:
                       self.ark(PI, HALF_PI, id, self.r, deformed=True)
                   elif i % 3 == 2:
                       self.ark(HALF_PI, 0, id, self.r, deformed=True)
            elif j % 2 == 1:
                for i in reversed(range(self.n_cols)):
                    id = j * self.n_cols + i
                    if i % 3 == 0:
                        self.ark(0, PI, id, self.r, deformed=True)
                        self.element_id.append(id)
                    elif i % 3 == 1:
                        self.ark(3 * HALF_PI, PI, id, self.r, deformed=True)
                    elif i % 3 == 2:
                        self.ark(TAU, 3 * HALF_PI, id, self.r, deformed=True)
    
                                
    def wrap_2nn(self, top, bottom, start, stop):
        j = start
        for i in range(self.n_cols):
            if i % 2 == 0:
                id = j * self.n_cols + i
                self.ark(PI, TAU, id, self.r, deformed=True)
                for k in range(top):
                    self.element_id.append(id + k * self.n_cols)
            elif i % 2 == 1:
                id = (j + (top - 1)) * self.n_cols + i
                self.ark(PI, 0, id, self.r, deformed=True)
        j = stop
        for i in reversed(range(self.n_cols)):
            if i % 2 == 0:
                id = (j - (bottom - 1)) * self.n_cols + i
                self.ark(TAU, PI, id, self.r, deformed=True)
            elif i % 2 == 1:
                id = j * self.n_cols + i
                self.ark(0, PI, id, self.r, deformed=True)
                for k in range(bottom):
                    self.element_id.append(id - k * self.n_cols)
                    
                    
    def wrap_2nn_v(self, left, right, start, stop):
        i = start
        for j in range(self.n_rows):
            if j % 2 == 0:
                id = j * self.n_rows + i
                self.ark(1.5 * PI, HALF_PI, id, self.r, deformed=True)
                for k in range(left):
                    self.element_id.append(id + k)
            elif j % 2 == 1:
                id = j * self.n_cols + (left - 1) + i
                self.ark(- HALF_PI, HALF_PI, id, self.r, deformed=True)
        i = stop
        for j in reversed(range(self.n_rows)):
            if j % 2 == 0:
                id = j * self.n_cols + i - (right - 1)
                self.ark(HALF_PI, 1.5 * PI, id, self.r, deformed=True)
            elif j % 2 == 1:
                id = j * self.n_cols + i
                self.ark(HALF_PI, - HALF_PI, id, self.r, deformed=True)
                for k in range(right):
                    self.element_id.append(id - k)
                    
                    
    def weave_2nn(self, top, bottom, start, stop):
        j = start
        for i in range(self.n_cols):
            if i % 2 == 0:
                id = j * self.n_cols + i
                self.ark(PI, TAU, id, self.r, deformed=True)
                for k in range(top):
                    self.element_id.append(id + k * self.n_cols)
            elif i % 2 == 1:
                id = (j + top) * self.n_cols + i
                self.ark(PI, 0, id, self.r, deformed=True)
        j = stop
        for i in reversed(range(self.n_cols)):
            if i % 2 == 0:
                id = (j - bottom) * self.n_cols + i
                self.ark(TAU, PI, id, self.r, deformed=True)
            elif i % 2 == 1:
                id = j * self.n_cols + i
                self.ark(0, PI, id, self.r, deformed=True)
                for k in range(bottom):
                    self.element_id.append(id - k * self.n_cols)
                    
    
    def diagonal(self):
        for i in range(self.n_cols):
            id = (i * self.n_cols) + i
            if i % 2 == 0:
                self.ark(-3 * QUARTER_PI, QUARTER_PI, id, self.r * sqrt(2), deformed=True)
            else:
                self.ark(5 * QUARTER_PI, QUARTER_PI, id, self.r * sqrt(2), deformed=True)
                self.element_id.append(id)
        for i in reversed(range(self.n_cols)):
            j = i - 2
            if j >= 0:
                id = j * self.n_cols + i
                if i % 2 == 0:
                    self.ark(QUARTER_PI, 5 * QUARTER_PI, id, self.r * sqrt(2), deformed=True)
                else:
                    self.ark(QUARTER_PI, -3 * QUARTER_PI, id, self.r * sqrt(2), deformed=True)
                    self.element_id.append(id)
                    
    
    def ark(self, theta_1, theta_2, peg_id, r, deformed=False):
        grid_width = width / (self.n_cols + 1)
        grid_height = height / (self.n_rows + 1)
        r = r
        delta = PI / 20
        deform_scale = grid_width / 4 
        resolution = 0.002
        n_points = 10 
        
        for i in range(n_points):
            if theta_2 > theta_1:
                theta = map(i, 0, n_points - 1, theta_1 + delta, theta_2 - delta)
            else:
                theta = map(i, 0, n_points - 1, theta_1 - delta, theta_2 + delta)
            x = self.pegs[peg_id].x + r * cos(theta)
            y = self.pegs[peg_id].y + r * sin(theta)
            n = map(noise(x * resolution, y * resolution), 0, 1, -deform_scale, deform_scale)
            if deformed:
                self.vertices.append(PVector(x + n, y + n))
            else:
                self.vertices.append(PVector(x, y))
            
