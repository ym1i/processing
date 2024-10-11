from peg import Peg
from wrapper import Wrapper


class Rainbow(Wrapper):
    
    def __init__(self, pegs, id, n_cols, n_rows, palette):
        self.pegs = pegs
        self.element_id = id
        self.vertices = []
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.r = width / (self.n_cols + 1) / 2
        self.palette = palette
                    
    
    def rainbow(self, n_layers, start):
        j = start
        # for i in range(self.n_cols):
        #     if i % 2 == 0:
        #         id = j * self.n_cols + i
        #         self.ark(PI, TAU, id, self.r,deformed=True)
        #         self.element_id.append(id)
        #     elif i % 2 == 1:
        #         id = j * self.n_cols + i
        #         self.ark(PI, 0, id, self.r, deformed=True)
        
        for i in reversed(range(self.n_cols)):
            if i % 2 == 0:
                id = j * self.n_cols + i
                self.ark(TAU, PI, id, self.r * 0.8 ,deformed=True)
            elif i % 2 == 1:
                id = j * self.n_cols + i
                self.ark(0, PI, id, self.r * 1.2, deformed=True)
        
        for i in range(self.n_cols):
            if i % 2 == 0:
                id = j * self.n_cols + i
                self.ark(PI, TAU, id, self.r * 0.6, deformed=True)
                self.element_id.append(id)
            elif i % 2 == 1:
                id = j * self.n_cols + i
                self.ark(PI, 0, id, self.r * 1.4, deformed=True)
        
        for i in reversed(range(self.n_cols)):
            if i % 2 == 0:
                id = j * self.n_cols + i
                self.ark(TAU, PI, id, self.r * 0.4 ,deformed=True)
            elif i % 2 == 1:
                id = j * self.n_cols + i
                self.ark(0, PI, id, self.r * 1.6, deformed=True)
                
        # for i in reversed(range(self.n_cols)):
        #     if i % 2 == 0:
        #         id = j * self.n_cols + i
        #         self.ark(TAU, PI, id, self.r * 0.6,deformed=True)
        #     elif i % 2 == 1:
        #         id = j * self.n_cols + i
        #         self.ark(0, PI, id, self.r * 1.4, deformed=True)
        
            
    
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
    
    
    def render(self, no_fill, peg_fill, ribon, fill_color, peg_color):
        beginShape()
        strokeWeight(5)
        stroke(fill_color)
    
        
        if no_fill:
            noFill()
        else:
            fill(fill_color)
            noFill()    
            # fill(self.palette.random_color())
            
        for v in self.vertices:
            vertex(v.x, v.y)
            
        endShape()
        
        if ribon:
            beginShape(QUAD_STRIP)
            
            fill(self.palette.random_color())
            stroke(0)
            strokeWeight(2)
            w = 10 # string width
            for i, v in enumerate(self.vertices):
                fill(self.palette.random_color()) 
                if i == 0:
                    theta = PVector.sub(v, self.vertices[-1]).heading()
                    first_v1 = PVector(v.x + w * cos(theta - HALF_PI), v.y + w * sin(theta - HALF_PI))
                    first_v2 = PVector(v.x + w * cos(theta + HALF_PI), v.y + w * sin(theta + HALF_PI))
                else:
                    theta = PVector.sub(v, self.vertices[i - 1]).heading()
                v1 = PVector(v.x + w * cos(theta - HALF_PI), v.y + w * sin(theta - HALF_PI))
                v2 = PVector(v.x + w * cos(theta + HALF_PI), v.y + w * sin(theta + HALF_PI))
                
                vertex(v1.x, v1.y)
                vertex(v2.x, v2.y)
            
            vertex(first_v1.x, first_v1.y)
            vertex(first_v2.x, first_v2.y)
                
            endShape()
            
        # render pegs
        if peg_fill:
            for id in self.element_id:
                self.pegs[id].render(peg_color, peg_color)
    
            
