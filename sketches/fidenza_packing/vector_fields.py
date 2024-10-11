from cell import Cell


class VectorFields():
    
    def __init__(self, width, height, grid_size, step_size):
        self.grid_size = grid_size
        self.step_size = step_size
        self.n_cols = width / grid_size
        self.n_rows = height / grid_size
        
        self.grid = [[0 for i in range(self.n_cols)] for j in range(self.n_rows)]
        self.prev_1 = self.grid[0][0]
        self.prev_2 = self.grid[0][0]
        
        for j in range(self.n_rows):
            for i in range(self.n_cols):
                vec = self.add_vector(i, j)
                self.grid[j][i] = Cell(i * self.grid_size, j * self.grid_size, vec)
                
    
    def add_vector(self, i, j):
        noise_value = noise(i * 0.005, j * 0.005)
        angle = map(noise_value, 0, 1, 0, TWO_PI)
        # _x = map(i, 0, self.n_cols, -TWO_PI, TWO_PI)
        # _y = map(j, 0, self.n_rows, -TWO_PI, TWO_PI)
        # _x = map(i, 0, n_cols, 0, TWO_PI)
        # _y = map(j, 0, n_rows, 0, TWO_PI)
        
        # x = _y
        # y = -_x
        # x = PI * sin(_y)
        # y = _x 
        # x = log(abs(_y))
        # y = log(abs(_x))
        # x = sin(_y) + cos(_y)
        # y = sin(_x) + cos(_x)
        
        # angle = PVector(x, y).heading()
        
        return PVector(self.step_size * cos(angle), self.step_size * sin(angle))
        
        
    def render_shape(self, start_x, start_y, n_steps, palette):
        i = int(start_x / self.grid_size) 
        j = int(start_y / self.grid_size)
        visited = [] 
        
        # COLLIDE/OVERLAP checking
        # if self.grid[j][i].checked:
        #     return
        # else: 
        #     self.grid[j][i].checked = True
        #     visited.append(self.grid[j][i])
        
        x = self.grid[j][i].x
        y = self.grid[j][i].y
        # w = 5
        w = random(3, 10)
        # noStroke()
        fill(palette.random_color())
        
        beginShape(QUAD_STRIP)
        for n in range(n_steps):
            if n == 99:
                print 'N: {}'.format(n)
            # vertex(x, y)
            i = constrain(int(x / self.grid_size), 0, self.n_cols - 1)
            j = constrain(int(y / self.grid_size), 0, self.n_rows - 1)
            
            vec = self.grid[j][i].vec
            theta = vec.heading()
            x1 = x + w * cos(theta - HALF_PI)
            y1 = y + w * sin(theta - HALF_PI)
            x2 = x + w * cos(theta + HALF_PI)
            y2 = y + w * sin(theta + HALF_PI)
            
            v1 = PVector(x1, y1)
            v2 = PVector(x2, y2)
            v = PVector.sub(v2, v1)
            steps = int(w * 2 / self.grid_size) if w > 5 else 1
            u = v.copy().div(steps)
            
            for i in range(1, steps):
                dv = v1.copy().add(u.copy().mult(i))
                _i = constrain(int(dv.x / self.grid_size), 0, self.n_cols - 1)
                _j = constrain(int(dv.y / self.grid_size), 0, self.n_rows - 1)
                if self.grid[_j][_i].checked and self.grid[_j][_i] not in visited:
                    return
                else:
                    self.grid[_j][_i].checked = True
                    visited.append(self.grid[_j][_i])
        
            # COLLIDE/OVERLAP checking
            i1 = constrain(int(x1 / self.grid_size), 0, self.n_cols - 1)
            j1 = constrain(int(y1 / self.grid_size), 0, self.n_rows - 1)
            i2 = constrain(int(x2 / self.grid_size), 0, self.n_cols - 1)
            j2 = constrain(int(y2 / self.grid_size), 0, self.n_rows - 1)
            
            if not self.grid[j1][i1].checked and not self.grid[j2][i2].checked: 
                vertex(x1, y1) 
                vertex(x2, y2)        
                self.grid[j1][i1].checked = True
                self.grid[j2][i2].checked = True
                visited.append(self.grid[j1][i1])
                visited.append(self.grid[j2][i2])
            elif self.grid[j1][i1] in visited or self.grid[j2][i2] in visited:
                x = x + vec.x
                y = y + vec.y
                continue
            else:
                break
            
            x = x + vec.x
            y = y + vec.y
        endShape()
    
    
    def render_line(self, start_x, start_y, n_steps):
        i = int(start_x / self.grid_size) 
        j = int(start_y / self.grid_size)
        x = self.grid[j][i].x
        y = self.grid[j][i].y
        
        noFill()
        beginShape()
        for _ in range(n_steps):
            vertex(x, y)
            i = int(x / self.grid_size) 
            j = int(y / self.grid_size)
            i = constrain(i, 0, self.n_cols - 1)
            j = constrain(j, 0, self.n_rows - 1)
            
            vec = self.grid[j][i].vec
            x = x + vec.x
            y = y + vec.y
        endShape()
    
    
    def render_vector_fields(self):
        beginShape(LINES)
        for j in range(self.n_rows):
            for i in range(self.n_cols):
                x = self.grid[j][i].x
                y = self.grid[j][i].y
                vx = self.grid[j][i].vec.x
                vy = self.grid[j][i].vec.y
                stroke(0)
                vertex(x, y)
                vertex(x + vx, y + vy)
                
                fill(255, 0, 0)
                noStroke()
                ellipse(x + vx, y + vy, 2, 2)
                noFill()    
        endShape()
        
        
