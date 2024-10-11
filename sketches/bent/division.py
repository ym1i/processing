

class Division():
    
    def __init__(self, x, y, side, direction, primary_color, shade_color):
        self.x = x
        self.y = y
        self.side = side
        self.direction = direction
        self.vertices = []
        self.tiles = []
        self.bent = False
        self.primary_color = primary_color
        self.shade_color = shade_color
        
        self.set_vertices()
        
        
    def set_vertices(self):
        self.vertices.append(PVector(self.x, self.y))
        self.vertices.append(PVector(self.x, self.y + self.side))
        _x = self.x + self.side * cos(radians(30)) if self.direction == 'right' else self.x - self.side * cos(radians(30))
        self.vertices.append(PVector(_x, self.y + self.side * sin(radians(30))))
        
    
    def tile(self):
        side_1 = PVector.sub(self.vertices[2], self.vertices[0]).div(10)
        side_2 = PVector.sub(self.vertices[2], self.vertices[1]).div(10)
        v1 = side_1.copy().mult(2)
        v2 = side_1.copy().mult(8)
        v3 = side_2.copy().mult(8)
        v4 = side_2.copy().mult(2)
        self.tiles.append(self.vertices[0].copy().add(v1))
        self.tiles.append(self.vertices[0].copy().add(v2))
        self.tiles.append(self.vertices[1].copy().add(v3))
        self.tiles.append(self.vertices[1].copy().add(v4))
        
        
    def bend(self, side):
        self.bent = True
        v = PVector.sub(self.vertices[1], self.vertices[0]).div(10)
        v1 = v.copy().mult(8)
        v2 = v.copy().mult(2)
    
        if side == 'right':
            self.tiles[2] = self.vertices[0].copy().add(v1)
            self.tiles[3] = self.vertices[0].copy().add(v2)
        elif side == 'left':
            self.tiles[0] = self.vertices[0].copy().add(v1)
            self.tiles[1] = self.vertices[0].copy().add(v2)
        
        
    def render(self):
        # fill(self.primary_color) if self.bent else fill(self.shade_color)
        # noStroke()
        noFill()
        beginShape()
        for v in self.vertices:
            vertex(v.x, v.y)
        endShape(CLOSE)
        
        
    def render_tile(self):
        fill(self.shade_color) if self.bent else fill(self.primary_color)
        # noStroke()
        beginShape(QUADS)
        for v in self.tiles:
            vertex(v.x, v.y)
        endShape()

















        
