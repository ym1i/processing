from peg import Peg


class PegSystem():
    
    def __init__(self, n_grid, body_color, background_color, peg_color_1, peg_color_2):
        self.pegs = []
        self.n_grid = n_grid
        self.body_color = body_color
        self.background_color = background_color
        self.peg_color_1 = peg_color_1
        self.peg_color_2 = peg_color_2 
        
        self.grid_layout(n_grid)
        
    
    def add_peg(self, x, y, z, r, style, c1, c2):
        self.pegs.append(Peg(x, y, z, r, style, c1, c2))
        
        
    def render(self):
        self.box()
        for peg in self.pegs:
            peg.render()
            
        
    def grid_layout(self, n_grid):
        w = width / (n_grid + 1)
        h = height / (n_grid + 1)
        d = width / (n_grid + 1)
        r = w * random(0.05, 0.3)
        offset = width / 2
        
        for i in range(n_grid):    
            for j in range(n_grid):
                for k in range(n_grid):
                    if random(1) < 0.1:
                        continue
            
                    style = 'sphere'
                    x = w * (i + 1) - offset
                    y = h * (j + 1) - offset
                    z = d * (k + 1) - offset
                    self.add_peg(x, y, z, 50, style, self.peg_color_1, self.peg_color_2)
    
    def box(self):
        noFill()
        stroke(0)
        
        # TOP
        beginShape(QUADS)
        noFill()
        vertex(-width / 2, -height / 2, width / 2)
        vertex(width / 2, -height / 2, width / 2)
        vertex(width / 2, -height / 2, -width / 2)
        vertex(-width / 2, -height / 2, -width / 2)
        endShape()
        # BOTTOM
        beginShape(QUADS)
        # fill(color(45, 132, 194))
        vertex(-width / 2, height / 2, width / 2) 
        vertex(width / 2, height / 2, width / 2)
        vertex(width / 2, height / 2, -width / 2)
        vertex(-width / 2, height / 2, -width / 2)
        endShape()
        # # FACE
        noFill()
        vertex(-width / 2, height / 2, width / 2)
        vertex(width / 2, height / 2, width / 2)
        vertex(width / 2, -height / 2, width / 2)
        vertex(-width / 2, -height / 2, width / 2)
        # # vertex(-width / 2, height / 2, width / 2)
        endShape()
        # BACk
        beginShape(QUADS)
        noFill()
        # fill(color(45, 132, 194))
        vertex(-width / 2, height / 2, -width / 2)
        vertex(width / 2, height / 2, -width / 2)
        vertex(width / 2, -height / 2, -width / 2)
        vertex(-width / 2, -height / 2, -width / 2)
        endShape()
  
        # # RIGHT
        # vertex(width / 2, height / 2, width / 2)
        # vertex(width / 2, height / 2, -width / 2)
        # vertex(width / 2, -height / 2, -width / 2)
        # vertex(width / 2, -height / 2, width / 2)
    
        # LEFT
        beginShape(QUADS)
        noFill()
        # fill(color(45, 132, 194))
        vertex(-width / 2, height / 2, width / 2)
        vertex(-width / 2, height / 2, -width / 2)
        vertex(-width / 2, -height / 2, -width / 2)
        vertex(-width / 2, -height / 2, width / 2)
        endShape()
    
            
