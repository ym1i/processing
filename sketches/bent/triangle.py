from division import Division


class Triangle():
    
    def __init__(self, x, y, side, direction, primary_color, primary_shade_color, secondary_color, secondary_shade_color):
        self.x = x
        self.y = y
        self.side = side
        self.bent = False
        self.direction = direction
        self.center = PVector(0, 0)
        self.vertices = []
        self.divisions = []
        self.primary_tiles = []
        self.secondary_tiles = []
        self.primary_color = primary_color
        self.primary_shade_color = primary_shade_color
        self.secondary_color = secondary_color
        self.secondary_shade_color = secondary_shade_color
        
        self.set_vertices()
        
        
    def divide(self):
        opposite = 'right' if self.direction == 'left' else 'left'
        m01 = self.mid_point(self.vertices[0], self.vertices[1])
        m02 = self.mid_point(self.vertices[0], self.vertices[2])
        m12 = self.mid_point(self.vertices[1], self.vertices[2])
        self.divisions.append(Division(self.vertices[0].x, self.vertices[0].y, self.side * 0.5, self.direction, self.primary_color, self.primary_shade_color))
        self.divisions.append(Division(m01.x, m01.y, self.side * 0.5, self.direction, self.primary_color, self.primary_shade_color))
        self.divisions.append(Division(m02.x, m02.y, self.side * 0.5, self.direction, self.primary_color, self.primary_shade_color))
        self.divisions.append(Division(m02.x, m02.y, self.side * 0.5, opposite, self.primary_color, self.primary_shade_color))
        
        
    def tile(self):
        side_1 = PVector.sub(self.vertices[2], self.vertices[0]).div(20)
        side_2 = PVector.sub(self.vertices[2], self.vertices[1]).div(20)
        v1 = side_1.copy().mult(2)
        v2 = side_1.copy().mult(8)
        v3 = side_2.copy().mult(8)
        v4 = side_2.copy().mult(2)
        self.primary_tiles.append(self.vertices[0].copy().add(v1))
        self.primary_tiles.append(self.vertices[0].copy().add(v2))
        self.primary_tiles.append(self.vertices[1].copy().add(v3))
        self.primary_tiles.append(self.vertices[1].copy().add(v4))
        v5 = side_1.copy().mult(12)
        v6 = side_1.copy().mult(18)
        v7 = side_2.copy().mult(18)
        v8 = side_2.copy().mult(12)
        self.primary_tiles.append(self.vertices[0].copy().add(v5))
        self.primary_tiles.append(self.vertices[0].copy().add(v6))
        self.primary_tiles.append(self.vertices[1].copy().add(v7))
        self.primary_tiles.append(self.vertices[1].copy().add(v8))
        v9 = side_1.copy().mult(9)
        v10 = side_1.copy().mult(11)
        v11 = side_2.copy().mult(11)
        v12 = side_2.copy().mult(9)
        self.secondary_tiles.append(self.vertices[0].copy().add(v9))
        self.secondary_tiles.append(self.vertices[0].copy().add(v10))
        self.secondary_tiles.append(self.vertices[1].copy().add(v11))
        self.secondary_tiles.append(self.vertices[1].copy().add(v12))
        
    
    def bend(self, side):
        self.bent = True
        self.primary_tiles = []
        self.secondary_tiles = []
        
        if side == 'left':
            side_1 = PVector.sub(self.vertices[0], self.vertices[1]).div(20)
            side_2 = PVector.sub(self.vertices[0], self.vertices[2]).div(20)
            v1 = side_1.copy().mult(2)
            v2 = side_1.copy().mult(8)
            v3 = side_2.copy().mult(8)
            v4 = side_2.copy().mult(2)
            self.primary_tiles.append(self.vertices[1].copy().add(v1))
            self.primary_tiles.append(self.vertices[1].copy().add(v2))
            self.primary_tiles.append(self.vertices[2].copy().add(v3))
            self.primary_tiles.append(self.vertices[2].copy().add(v4))
            v5 = side_1.copy().mult(12)
            v6 = side_1.copy().mult(18)
            v7 = side_2.copy().mult(18)
            v8 = side_2.copy().mult(12)
            self.primary_tiles.append(self.vertices[1].copy().add(v5))
            self.primary_tiles.append(self.vertices[1].copy().add(v6))
            self.primary_tiles.append(self.vertices[2].copy().add(v7))
            self.primary_tiles.append(self.vertices[2].copy().add(v8))
            v9 = side_1.copy().mult(9)
            v10 = side_1.copy().mult(11)
            v11 = side_2.copy().mult(11)
            v12 = side_2.copy().mult(9)
            self.secondary_tiles.append(self.vertices[1].copy().add(v9))
            self.secondary_tiles.append(self.vertices[1].copy().add(v10))
            self.secondary_tiles.append(self.vertices[2].copy().add(v11))
            self.secondary_tiles.append(self.vertices[2].copy().add(v12))
        else:
            side_1 = PVector.sub(self.vertices[1], self.vertices[0]).div(20)
            side_2 = PVector.sub(self.vertices[1], self.vertices[2]).div(20)
            v1 = side_1.copy().mult(2)
            v2 = side_1.copy().mult(8)
            v3 = side_2.copy().mult(8)
            v4 = side_2.copy().mult(2)
            self.primary_tiles.append(self.vertices[0].copy().add(v1))
            self.primary_tiles.append(self.vertices[0].copy().add(v2))
            self.primary_tiles.append(self.vertices[2].copy().add(v3))
            self.primary_tiles.append(self.vertices[2].copy().add(v4))
            v5 = side_1.copy().mult(12)
            v6 = side_1.copy().mult(18)
            v7 = side_2.copy().mult(18)
            v8 = side_2.copy().mult(12)
            self.primary_tiles.append(self.vertices[0].copy().add(v5))
            self.primary_tiles.append(self.vertices[0].copy().add(v6))
            self.primary_tiles.append(self.vertices[2].copy().add(v7))
            self.primary_tiles.append(self.vertices[2].copy().add(v8))
            v9 = side_1.copy().mult(9)
            v10 = side_1.copy().mult(11)
            v11 = side_2.copy().mult(11)
            v12 = side_2.copy().mult(9)
            self.secondary_tiles.append(self.vertices[0].copy().add(v9))
            self.secondary_tiles.append(self.vertices[0].copy().add(v10))
            self.secondary_tiles.append(self.vertices[2].copy().add(v11))
            self.secondary_tiles.append(self.vertices[2].copy().add(v12))    
        
    
    def mid_point(self, v1, v2):
        return PVector((v1.x + v2.x) * 0.5, (v1.y + v2.y) * 0.5)
    
    
    def set_vertices(self):
        self.vertices.append(PVector(self.x, self.y))
        self.vertices.append(PVector(self.x, self.y + self.side))
        _x = self.x + self.side * cos(radians(30)) if self.direction == 'right' else self.x - self.side * cos(radians(30))
        self.vertices.append(PVector(_x, self.y + self.side * sin(radians(30))))
        
        self.center = PVector((2 * self.x + self.vertices[2].x) / 3, (self.y + self.y + self.side + self.vertices[2].y) / 3)


    def render(self):
        # fill(self.primary_color) if self.bent else fill(self.primary_shade_color)
        # noStroke()
        noFill()
        beginShape()
        for v in self.vertices:
            vertex(v.x, v.y)
        endShape(CLOSE)
        
    
    def render_tile(self):
        beginShape(QUADS)
        # noStroke()
        fill(self.primary_shade_color) if self.bent else fill(self.primary_color)
        for v in self.primary_tiles:
            vertex(v.x, v.y)
        fill(self.secondary_shade_color) if self.bent else fill(self.secondary_color)
        for v in self.secondary_tiles:
            vertex(v.x, v.y)
        endShape()
    
    
