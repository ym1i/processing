from palette import Palette


class Splitter():
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.palette = Palette()

        
    def split(self):
        
        # SPLIT_1 -------------------------------------------------------
        
        splitter_1 = []
        r = self.w / 2
        pivot_1a = PVector(self.x + r, self.y + self.h)
        pivot_1b = PVector(self.x + r, self.y)
        n = 30
        
        for i in range(n):
            a = map(i, 0, n - 1, PI, 1.5 * PI)
            splitter_1.append(PVector(pivot_1a.x + r * cos(a), pivot_1a.y + r * sin(a)))
        
        for i in range(n):
            a = map(i, 0, n - 1, HALF_PI, 0)
            splitter_1.append(PVector(pivot_1b.x + r * cos(a), pivot_1b.y + r * sin(a)))
            
        part_1a = []
        part_1b = []
        
        for v in splitter_1:
            part_1a.append(v.copy())
            part_1b.append(v.copy())
            
        for i in range(2 * n):
            x1 = map(i, 0, 2 * n - 1, self.x + self.w, self.x)
            y1 = self.y
            part_1a.append(PVector(x1, y1))
            x2 = self.x + self.w
            y2 = map(i, 0, 2 * n - 1, self.y, self.y + self.h)
            part_1b.append(PVector(x2, y2))
             
        for i in range(2 * n):
            x1 = self.x
            y1 = map(i, 0, 2 * n - 1, self.y, self.y + self.h)
            part_1a.append(PVector(x1, y1))
            x2 = map(i, 0, 2 * n - 1, self.x + self.w, self.x)
            y2 = self.y + self.h
            part_1b.append(PVector(x2, y2))
    
    
        # SPLIT_2a--------------------------------------------------------------
        pivot_2a = PVector(self.x + 1.5 * r, self.y + self.h)
        pivot_2b = PVector(self.x + 1.5 * r, self.y)
        splitter_2a = []
        n2 = 0
        
        for i in range(n):
            a = map(i, 0, n - 1, PI, 1.5 * PI)
            splitter_2a.append(PVector(pivot_2a.x + r * cos(a), pivot_2a.y + r * sin(a)))
            
        for i in range(n):
            a = map(i, 0, n - 1, HALF_PI, 0)
            x = pivot_2b.x + r * cos(a)
            y = pivot_2b.y + r * sin(a)
            if x < self.x + self.w:
                splitter_2a.append(PVector(x, y))
            else:
                splitter_2a.append(PVector(self.x + self.w, y))
                n2 = n + i
                break
        
        part_2a = []
        for v in splitter_2a:
            part_2a.append(v.copy())
    
        for i in range(n2):
            x = self.x + self.w
            y = map(i, 0, n2 - 1, splitter_2a[-1].y, self.y + self.h)
            part_2a.append(PVector(x, y))
        for i in range(n2):
            x = map(i, 0, n2 - 1, self.x + self.w, splitter_2a[0].x)
            y = self.y + self.h
            part_2a.append(PVector(x, y))
       
        
        # SPLIT_2b ---------------------------------------------------------------
        pivot_2c = PVector(self.x + 0.5 * r, self.y + self.h)
        pivot_2d = PVector(self.x + 0.5 * r, self.y)
        splitter_2b = []
        n0 = 0
        y_cache = 0
        
        for i in range(n):
            a = map(i, 0, n - 1, PI, 1.5 * PI)
            x = pivot_2c.x + r * cos(a)
            y = pivot_2c.y + r * sin(a)
            if x >= self.x:
                splitter_2b.append(PVector(x, y))
                n0 += 1
            else:
                y_cache = y
        splitter_2b.insert(0, PVector(self.x, y_cache))
        
        for i in range(n):
            a = map(i, 0, n - 1, HALF_PI, 0)
            splitter_2b.append(PVector(pivot_2d.x + r * cos(a), pivot_2d.y + r * sin(a)))
        n0 += n
        
        part_2b = []
        for v in splitter_2b:
            part_2b.append(v.copy())
            
        for i in range(n0):
            x = map(i, 0, n0 - 1, splitter_2b[-1].x, self.x)
            y = self.y
            part_2b.append(PVector(x, y))
        for i in range(n0):
            x = self.x
            y = map(i, 0, n0 - 1, self.y, splitter_2b[0].y)
            part_2b.append(PVector(x, y))
            
        
        self.part_1a = part_1a
        self.part_1b = part_1b
        self.part_2a = part_2a
        self.part_2b = part_2b
        self.splitter_1 = splitter_1
        self.splitter_2a = splitter_2a
        self.splitter_2b = splitter_2b
        
        
        # SPLIT_3
        # pivot_3 = PVector(self.x + self.w, self.y + self.h)
        # splitter_3 = []
        # n3 = 0
        
        # for i in range(n):
        #     a = map(i, 0, n - 1, PI, 1.5 * PI)
        #     splitter_3.append(PVector(pivot_3.x + r * cos(a), pivot_3.y + r * sin(a)))
        
        # part_4 = []
        # for v in splitter_3:
        #     part_4.append(v.copy())
            
        # for i in range(n):
        #     x = self.x + self.w
        #     y = map(i, 0, n - 1, splitter_3[-1].y, self.y + self.h)
        #     part_4.append(PVector(x, y))
        # for i in range(n2):
        #     x = map(i, 0, n - 1, self.x + self.w, splitter_3[0].x)
        #     y = self.y + self.h
        #     part_4.append(PVector(x, y))
        
        # self.part_4 = part_4
        # self.splitter_3 = splitter_3
        
       
    def move(self):
        offset_1 = PVector(8, 8)
        offset_2 = PVector(-8, -8)
        
        for v in self.part_1b:
            v.add(offset_1)
            
        # for v in self.splitter_2a:
        #     v.add(offset_1)
        for v in self.part_2a:
            v.add(offset_1)
            # v.add(offset_1.copy().mult(2))
        
        # for v in self.splitter_3:
        #     v.add(offset_1)
        # for v in self.part_4:
        #     v.add(offset_1)
            # v.add(offset_1.copy().mult(2))
        
        
        for v in self.part_1a:
            v.add(offset_2)
        for v in self.part_2b:
            v.add(offset_2)
    
    
    def render(self):
        strokeWeight(2)
        fill(self.palette.random_color())
        beginShape()
        for v in self.part_1a:
            vertex(v.x, v.y)
        endShape(CLOSE)  
    
        fill(self.palette.random_color())
        beginShape()
        for v in self.part_1b:
            vertex(v.x, v.y)
        endShape(CLOSE)  
        
        fill(self.palette.random_color())
        beginShape()
        for v in self.part_2a:
            vertex(v.x, v.y)
        endShape(CLOSE) 
        
        fill(self.palette.random_color())
        beginShape()
        for v in self.part_2b:
            vertex(v.x, v.y)
        endShape(CLOSE) 
        
        
        self.render_connector()
        self.render_dot()
        
    
    def render_connector(self):
        
        # fill(self.palette.random_color())
        beginShape(QUAD_STRIP)
        for i, v in enumerate(self.splitter_1):
            fill(self.palette.random_color())
            vertex(v.x, v.y)
            # vertex(self.part_1a[i].x, self.part_1a[i].y)
            vertex(self.part_1b[i].x, self.part_1b[i].y)
        endShape(CLOSE)
        
        # fill(self.palette.random_color())
        beginShape(QUAD_STRIP)
        for i, v in enumerate(self.splitter_1):
            fill(self.palette.random_color())
            vertex(v.x, v.y)
            vertex(self.part_1a[i].x, self.part_1a[i].y)
            # vertex(self.part_1b[i].x, self.part_1b[i].y)
        endShape(CLOSE)
        
        fill(self.palette.random_color())
        beginShape(QUAD_STRIP)
        for i, v in enumerate(self.splitter_2a):
            # fill(self.palette.random_color())
            vertex(v.x, v.y)
            vertex(self.part_2a[i].x, self.part_2a[i].y)
        endShape(CLOSE) 
        
        fill(self.palette.random_color())
        beginShape(QUAD_STRIP)
        for i, v in enumerate(self.splitter_2b):
            # fill(self.palette.random_color())
            vertex(v.x, v.y)
            vertex(self.part_2b[i].x, self.part_2b[i].y)
        endShape(CLOSE) 
        
    
    def render_dot(self):
        for j in range(1):
            fill(self.palette.random_color())
            for i, v in enumerate(self.splitter_2a):
                if i % 4 == 0:
                    u = PVector.sub(self.part_2a[i], v)
                    # u = PVector.sub(PVector(self.x + self.w, self.y + self.h), v)
                    u.normalize().mult(60 * (j + 1))
                    r = 20
                    # strokeWeight(1)
                    # fill(self.palette.random_color())
                    if (v.x + u.x < self.x + self.w - r / 2) and (v.y + u.y < self.y + self.h - r / 2):
                        ellipse(v.x + u.x, v.y + u.y, r, r)
        
        for j in range(1):
            fill(self.palette.random_color())
            for i, v in enumerate(self.splitter_2b):
                if i % 4 == 0:
                    u = PVector.sub(self.part_2b[i], v)
                    u.normalize().mult(60 * (j + 1))
                    r = 20
                    # fill(self.palette.random_color())
                    if (v.x + u.x > self.x + r / 2) and (v.y + u.y > self.y + r / 2):
                        ellipse(v.x + u.x, v.y + u.y, r, r)
        

        

        
        
        
    
   
