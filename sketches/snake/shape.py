from palette import Palette


class Shape():
    
    def __init__(self, pos, w, palette):
        self.init_pos = pos
        self.cur = pos
        self.w = w
        self.vertices = []
        self.palette = palette
        
        for i in range(4):
            self.create()
        self.finish()
        
    
    def create(self):
        
        # go down
        n = 10
        for i in range(n):
            dy = 10
            x = self.cur.x
            y = self.cur.y + dy
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
        
        # semi-circle(1)
        n = 15
        r = self.w * 0.5
        offset = 0.1
        pivot = self.cur.copy().add(PVector(r, 0))
        for i in range(n):
            a = map(i, 0, n-1, PI-offset, offset)
            x = pivot.x + r * cos(a)
            y = pivot.y + r * sin(a)
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
            
        # semi-circle(2)
        n = 20
        r = self.w 
        pivot = self.cur.copy().add(PVector(r, 0))
        for i in range(n):
            a = map(i, 0, n-1, PI+offset, TAU)
            x = pivot.x + r * cos(a)
            y = pivot.y + r * sin(a)
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
            
            
    def finish(self):
        n = 35
        r = self.w * 2.5
        pivot = self.cur.copy().add(PVector(-r, 0))
        for i in range(n):
            a = map(i, 0, n-1, 0, PI-0.2)
            x = pivot.x + r * cos(a)
            y = pivot.y + r * sin(a)
            self.cur = PVector(x, y)
            self.vertices.append(self.cur.copy())
    
    def render(self):
        fill(self.palette.random_color())
        n = 100
        
        # FROM TOP TO THE INITIAL POSITION
        beginShape(QUAD_STRIP)
        for i in range(n):
            x = self.init_pos.x
            y = map(i, 0, n-1, self.init_pos.y - 10 * n, self.init_pos.y + 20)
            vertex(x - self.w * 0.5, y)
            vertex(x + self.w * 0.5, y)
        endShape()
            
        
        # MAIN
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
        
        
        # FROM CUR TO THE BOTTOM
        # beginShape(QUAD_STRIP)
        # for i in range(n):
        #     x = self.cur.x
        #     y = map(i, 0, n-1, self.cur.y, self.cur.y + 10 * n)
        #     vertex(x - self.w * 0.5, y)
        #     vertex(x + self.w * 0.5, y)
        # endShape()

        
