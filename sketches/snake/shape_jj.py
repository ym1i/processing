from palette import Palette


class ShapeJJ():
    
    def __init__(self, pos, w, palette):
        self.cur = pos
        self.w = w
        self.vertices = []
        self.palette = palette
        
        self.create()
        
    
    def create(self):
        
        # go down
        n = 100
        for i in range(n):
            dy = 10
            x = self.cur.x
            y = map(i, 0, n-1, self.cur.y - dy * 100, self.cur.y)
            self.vertices.append(PVector(x, y))
        
        # go down
        n = 10
        for i in range(n):
            dy = 10
            x = self.cur.x
            y = self.cur.y + dy
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
        
        # semi-circle(1)
        n = 20
        r = self.w * 2.5
        offset = 0.1
        pivot = self.cur.copy().add(PVector(r, 0))
        for i in range(n):
            a = map(i, 0, n-1, PI-offset, 0+offset)
            x = pivot.x + r * cos(a)
            y = pivot.y + r * sin(a)
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
            
        # go up
        n = 100
        for i in range(n):
            dy = 10
            x = self.cur.x
            y = self.cur.y - dy
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
            
            
    def render(self):
        fill(self.palette.random_color())
        # noStroke()
        # noFill()
        beginShape(QUAD_STRIP)
        for i, v in enumerate(self.vertices):
            if v == self.vertices[0] or v == self.vertices[-1]:
                continue
            # fill(self.palette.random_color())
            prev = self.vertices[i-1]
            next = self.vertices[i+1]
            theta = PVector.sub(next, prev).heading()
            r = self.w * 0.5
            v1 = PVector(v.x + r * cos(theta + HALF_PI), v.y + r * sin(theta + HALF_PI))
            v2 = PVector(v.x + r * cos(theta - HALF_PI), v.y + r * sin(theta - HALF_PI))
            vertex(v1.x, v1.y)
            vertex(v2.x, v2.y)
        endShape(CLOSE)
