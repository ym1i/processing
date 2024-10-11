from palette import Palette


class Splitter():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.center = PVector(x, y)
        self.palette = Palette()
        
        self.deformed_circle = self.__deformed_circle()
        self.__split4()
        
        
    def __split(self):
        splitter = []
        n_points = 100
        i = int(random(n_points / 2))
        j = (i + (n_points / 2)) % n_points
        u1 = PVector.sub(self.deformed_circle[i], self.center).mult(0.5)
        u2 = PVector.sub(self.deformed_circle[j], self.center).mult(0.5)
        pivot1 = self.center.copy().add(u1)
        pivot2 = self.center.copy().add(u2)
        r1 = u1.mag()
        r2 = u2.mag()
        a1 = u1.heading()
        a2 = u2.heading()
        
        for _i in range(n_points):
            a = map(_i, 0, n_points - 1, a1, a1 + PI)
            splitter.append(PVector(pivot1.x + r1 * cos(a), pivot1.y + r1 * sin(a)))
        for _j in range(n_points):
            a = map(_j, 0, n_points - 1, a2 + PI, a2)
            splitter.append(PVector(pivot2.x + r2 * cos(a), pivot2.y + r2 * sin(a)))
        
        print 'i: {} | j: {}'.format(i, j)
        # make partition by splitter
        section1 = []
        section2 = []
        connector = []
        w1 = u1.copy().rotate(HALF_PI)
        w2 = u1.copy().rotate(-HALF_PI)
        w1.normalize().mult(60)
        w2.normalize().mult(60)
        for _i, v in enumerate(splitter):
            section1.append(v.copy().add(w1))
            section2.append(v.copy().add(w2))
            if _i % 2 == 0:
                connector.append(v.copy().add(w1))
                connector.append(v.copy().add(w2))
        
        for _i in reversed(range(i, i + (n_points / 2))):
            section1.append(self.deformed_circle[_i].copy().add(w1))
        
        for _j in range(j, j + (n_points / 2)):
            _j %= n_points
            section2.append(self.deformed_circle[_j].copy().add(w2))
            
        self.splitter = []
        self.splitter.append(splitter)
        self.sections = []
        self.sections.append(section1)
        self.sections.append(section2)
        self.connectors = []
        self.connectors.append(connector)
    
    
    def __split3(self):
        splitter1 = []
        splitter2 = []
        splitter3 = []
        points = 99
        i = int(random(points / 3))
        j = (i + (points / 3)) % points
        k = (j + (points / 3)) % points
        u1 = PVector.sub(self.deformed_circle[i], self.center).mult(0.5)
        u2 = PVector.sub(self.deformed_circle[j], self.center).mult(0.5)
        u3 = PVector.sub(self.deformed_circle[k], self.center).mult(0.5)
        pivot1 = self.center.copy().add(u1)
        pivot2 = self.center.copy().add(u2)
        pivot3 = self.center.copy().add(u3)
        r = u1.mag()
        a1 = u1.heading()
        a2 = u2.heading()
        a3 = u3.heading()       
                    
        n = 70
        for _i in range(n):
            a = map(_i, 0, n - 1, a1, a1 + PI)
            splitter1.append(PVector(pivot1.x + r * cos(a), pivot1.y + r * sin(a)))
        for _j in range(n):
            a = map(_j, 0, n - 1, a2, a2 + PI)
            splitter2.append(PVector(pivot2.x + r * cos(a), pivot2.y + r * sin(a)))
        for _k in range(n):
            a = map(_k, 0, n - 1, a3, a3 + PI)
            splitter3.append(PVector(pivot3.x + r * cos(a), pivot3.y + r * sin(a)))
            
        section1 = []
        section2 = []
        section3 = []
        connector1 = []
        connector2 = []
        connector3 = []
        w1 = u1.copy().rotate(-HALF_PI / 2)
        w2 = u2.copy().rotate(-HALF_PI / 2)
        w3 = u3.copy().rotate(-HALF_PI / 2)
        w1.normalize().mult(12)
        w2.normalize().mult(12)
        w3.normalize().mult(12)
        
        for v in splitter1:
            section1.append(v.copy().add(w1))
        for v in reversed(splitter3):    
            section1.append(v.copy().add(w1))
        for _i in range(k, points):
            section1.append(self.deformed_circle[_i].copy().add(w1))
        for _i in range(i + 1):
            section1.append(self.deformed_circle[_i].copy().add(w1))
            
        for v in splitter2:
            section2.append(v.copy().add(w2))
        for v in reversed(splitter1):    
            section2.append(v.copy().add(w2))
        for _i in range(i, j + 1):
            section2.append(self.deformed_circle[_i].copy().add(w2))
            
        for v in splitter3:
            section3.append(v.copy().add(w3))
        for v in reversed(splitter2):    
            section3.append(v.copy().add(w3))
        for _i in range(j, k + 1):
            section3.append(self.deformed_circle[_i].copy().add(w3))
            
        # connectors
        for v in splitter1:
            connector1.append(v.copy().add(w1))
            connector1.append(v.copy().add(w2))
        for v in splitter2:
            connector2.append(v.copy().add(w2))
            connector2.append(v.copy().add(w3))
            
        for v in splitter3:
            connector3.append(v.copy().add(w3))
            connector3.append(v.copy().add(w1))
        
        
        self.p1 = i
        self.p2 = j
        self.p3 = k
        
        self.sections = []
        self.sections.append(section1)
        self.sections.append(section2)
        self.sections.append(section3)
        
        self.connectors = []
        self.connectors.append(connector1)
        self.connectors.append(connector2)
        self.connectors.append(connector3)
        
    
    def __split4(self):
        splitter1 = []
        n_points = 100
        
        i = int(random(n_points / 4))
        j = i + n_points / 4
        k = j + n_points / 4
        l = k + n_points / 4
        
        p1 = self.deformed_circle[i]
        p2 = self.deformed_circle[j]
        p3 = self.deformed_circle[k]
        p4 = self.deformed_circle[l]
    
        u1 = PVector.sub(p1, self.center).mult(0.5)
        u2 = PVector.sub(p3, self.center).mult(0.5)
        pivot1 = self.center.copy().add(u1)
        pivot2 = self.center.copy().add(u2)
   
        r = u1.mag()
        a1 = u1.heading()
        a2 = u2.heading()
        
        for _i in range(n_points):
            a = map(_i, 0, n_points - 1, a1, a1 + PI)
            splitter1.append(PVector(pivot1.x + r * cos(a), pivot1.y + r * sin(a)))
        for _j in range(n_points):
            a = map(_j, 0, n_points - 1, a2 + PI, a2)
            splitter1.append(PVector(pivot2.x + r * cos(a), pivot2.y + r * sin(a)))
            
        splitter4 = []
        u4 = PVector.sub(p1, self.center)
        pivot4 = p4.copy().add(u4)
        r4 = u4.mag()
        a4 = PVector.sub(p1, pivot4).heading()
        for _i in range(n_points):
            a = map(_i, 0, n_points + 2, a4, a4 + HALF_PI)
            splitter4.append(PVector(pivot4.x + r4 * cos(a), pivot4.y + r4 * sin(a)))
            
        splitter3 = []
        u3 = PVector.sub(p3, self.center)
        pivot3 = p2.copy().add(u3)
        r3 = u3.mag()
        a3 = PVector.sub(p3, pivot3).heading()
        for _i in range(n_points):
            a = map(_i, 0, n_points - 2, a3, a3 + HALF_PI)
            splitter3.append(PVector(pivot3.x + r3 * cos(a), pivot3.y + r3 * sin(a)))
        
        # print 'i: {} | j: {} | k: {} | l: {}'.format(i, j, k, l)
        # make partition by splitter
        section1 = []
        section2 = []
        section3 = []
        section4 = []
        connector = []
        w1 = u1.copy().rotate(HALF_PI)
        w2 = u1.copy().rotate(-HALF_PI)
        w1.normalize().mult(60)
        w2.normalize().mult(60)
        for _i, v in enumerate(splitter1):
            # section1.append(v)
            # section2.append(v)
            if _i % 2 == 0:
                connector.append(v)
                connector.append(v)
            
        
        # SECTION 1
        for v in splitter1:
            section1.append(v)
        for v in splitter3:
            section1.append(v)
        for _i in reversed(range(i, j)):
            section1.append(self.deformed_circle[_i])
        
        # SECTION 2
        for v in splitter1:
            section2.append(v)
        for _i in range(k, l):
            section2.append(self.deformed_circle[_i])
        for v in reversed(splitter4):
            section2.append(v)
        
        # SECTION 3
        for v in splitter3:
            section3.append(v)
        for _i in range(j, k):
            section3.append(self.deformed_circle[_i])
        
        # SECTION 4
        for v in splitter4:
            section4.append(v)
        for _i in range(l, n_points):
            section4.append(self.deformed_circle[_i])
        for _i in range(i):
            section4.append(self.deformed_circle[_i])
            
        self.splitter = []
        self.splitter.append(splitter1)
        self.sections = []
        self.sections.append(section1)
        self.sections.append(section2)
        self.sections.append(section3)
        self.sections.append(section4)
        self.connectors = []
        self.connectors.append(connector)
        self.pivots = []
        self.pivots.append(pivot1)
        self.pivots.append(pivot2)
        self.pivots.append(pivot3)
        self.pivots.append(pivot4)
        self.rad = r
        
    
    def __deformed_circle(self):
        vertices = []
        resolution = 0.002
        noise_scale = self.r / 10
        n_points = 100
        
        for i in range(n_points):
            a = map(i, 0, n_points - 1, 0, TAU)
            x = self.x + self.r * cos(a)
            y = self.y + self.r * sin(a)
            n = map(noise(x * resolution, y * resolution), 0, 1, -noise_scale, noise_scale)
            n = 0
            vertices.append(PVector(x + n, y + n))
        
        return vertices
    
    
    def render(self):
        
        # self.__split4()
        
        for section in self.sections:
            fill(self.palette.random_color())
            strokeWeight(0.3)
            beginShape()
            for v in section:
                vertex(v.x, v.y)
            endShape(CLOSE)
                
            
        # r = PVector.sub(self.center, self.pivots[0]).mag()
        # self.render_circle_around_pivot(self.pivots[0], r * 0.8)
        # self.render_circle_around_pivot(self.pivots[1], r * 0.8)
        
        # for connector in self.connectors:
        #     beginShape(QUAD_STRIP)
        #     fill(self.palette.random_color())
        #     for v in connector:
        #         # fill(self.palette.random_color())
        #         vertex(v.x, v.y)
        #     endShape()
    
    
    def render_circle_around_pivot(self, pivot, r):
        fill(self.palette.random_color())
        ellipse(pivot.x, pivot.y, r * 2, r * 2)
        
    
    
    def render_triangle(self):
        fill(self.palette.random_color())
        beginShape()
        vertex(self.deformed_circle[self.p1].x, self.deformed_circle[self.p1].y)
        vertex(self.deformed_circle[self.p2].x, self.deformed_circle[self.p2].y)
        vertex(self.center.x, self.center.y)
        endShape()
        
        fill(self.palette.random_color())
        beginShape()
        vertex(self.deformed_circle[self.p2].x, self.deformed_circle[self.p2].y)
        vertex(self.deformed_circle[self.p3].x, self.deformed_circle[self.p3].y)
        vertex(self.center.x, self.center.y)
        endShape()
        
        fill(self.palette.random_color())
        beginShape()
        vertex(self.deformed_circle[self.p3].x, self.deformed_circle[self.p3].y)
        vertex(self.deformed_circle[self.p1].x, self.deformed_circle[self.p1].y)
        vertex(self.center.x, self.center.y)
        endShape()
        
        
        
                
