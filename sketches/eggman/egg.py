from palette import Palette


class Egg():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.palette = Palette()
    
    def crack(self):
        n = 20
        
        # Split
        splitter = []
        pivot_1 = PVector(self.x - 0.75 * self.r, self.y)
        pivot_2 = PVector(self.x - 0.25 * self.r, self.y)
        pivot_3 = PVector(self.x + 0.25 * self.r, self.y)
        pivot_4 = PVector(self.x + 0.75 * self.r, self.y)
        r = self.r / 4
        
        for i in range(n):
            a = map(i, 0, n - 1, PI, TAU)
            splitter.append(PVector(pivot_1.x + r * cos(a), pivot_1.y + r * sin(a)))
        for i in range(n):
            a = map(i, 0, n - 1, PI, 0)
            splitter.append(PVector(pivot_2.x + r * cos(a), pivot_2.y + r * sin(a)))
        for i in range(n):
            a = map(i, 0, n - 1, PI, TAU)
            splitter.append(PVector(pivot_3.x + r * cos(a), pivot_3.y + r * sin(a)))
        for i in range(n):
            a = map(i, 0, n - 1, PI, 0)
            splitter.append(PVector(pivot_4.x + r * cos(a), pivot_4.y + r * sin(a)))
            
        # Make parts
        part_1 = []
        part_2 = [] 
        
        for v in splitter:
            part_1.append(v.copy())
            part_2.append(v.copy())
        for i in range(4 * n):
            a = map(i, 0, 4 * n - 1, TAU, PI)
            part_1.append(PVector(self.x + self.r * cos(a), self.y + self.r * sin(a)))
            b = map(i, 0, 4 * n - 1, 0, PI)
            part_2.append(PVector(self.x + self.r * cos(b), self.y + self.r * sin(b)))
            
        # Init CONNECTOR
        connector_1 = []
        connector_2 = []
        
        for v in splitter:
            connector_1.append(v.copy())
            connector_2.append(v.copy())
        
        # Colors for connector
        colors = []
        for v in splitter:
            colors.append(self.palette.random_color())
        
        # Instance variables
        self.splitter = splitter
        self.pivot_1 = pivot_1
        self.pivot_2 = pivot_2
        self.pivot_3 = pivot_3
        self.pivot_4 = pivot_4
        self.part_1 = part_1
        self.part_2 = part_2
        self.connector_1 = connector_1
        self.connector_2 = connector_2
        self.colors = colors
        self.v1 = PVector(0, -1)
        self.v2 = PVector(0, 1)
    
            
    def move(self):
        # Move and Stop PART_1 and PART_2
        center = PVector(self.x, self.y)
        rest = 100
        
        # Set velocity according to the position of PART_1 and PART_2
        if center.y - self.part_1[40].y > rest:
            # self.v1.mult(-1)
            self.v1.mult(0)
            self.move_connector()
        elif center.y - self.part_1[40].y < 0:
            self.v1.mult(-1)
            self.reset_colors()
            
        if self.part_2[40].y - center.y  > rest:
            # self.v2.mult(-1)
            self.v2.mult(0)
        elif self.part_2[40].y - center.y < 0:
            self.v2.mult(-1)

        # Move Part_1, PART_2, CONNECTOR_1, CONNECTOR_2
        for i, v in enumerate(self.part_1):
            v.add(self.v1)
        for i, v in enumerate(self.part_2):
            v.add(self.v2) 
        for i in range(len(self.splitter)):
            self.connector_1[i].add(self.v1)
            self.connector_2[i].add(self.v2)
            
    
    def move_connector(self):
        # Move CONNECTOR when PART_1 reaches the target
        center = PVector(self.x, self.y)
        target_1 = []
        target_2 = []
        n = len(self.connector_1)
        r = self.r * 0.4
        for i in range(n):
            a1 = map(i, 0, n-1, PI, TAU)
            target_1.append(PVector(center.x + r * cos(a1), center.y + r * sin(a1)))
            a2 = map(i, 0, n-1, PI, 0)
            target_2.append(PVector(center.x + r * cos(a2), center.y + r * sin(a2)))
        
        for i, v in enumerate(self.connector_1):
            # u = PVector.sub(center, v)
            u = PVector.sub(target_1[i], v)
            u.mult(0.03)
            v.add(u)
        for i, v in enumerate(self.connector_2):
            # u = PVector.sub(center, v)
            u = PVector.sub(target_2[i], v)
            u.mult(0.03)
            v.add(u)
             
    
    def reset_colors(self):
        self.colors = []
        for v in self.splitter:
            self.colors.append(self.palette.random_color())
        
    
    def render(self):
        strokeWeight(1)
        fill(self.colors[0])
        beginShape()
        for v in self.part_1:
            vertex(v.x, v.y)
        endShape()
        
        beginShape()
        for v in self.part_2:
            vertex(v.x, v.y)
        endShape()
        
        self.render_connector()
        # self.render_dot()
                
    
    
    def render_connector(self):
        beginShape(QUAD_STRIP)
        for i, _ in enumerate(self.splitter):
            fill(self.colors[i])
            vertex(self.connector_1[i].x, self.connector_1[i].y)
            vertex(self.connector_2[i].x, self.connector_2[i].y)
        endShape(CLOSE)
    
        
    def static_move(self):
        r1 = random(50, 150)
        r2 = random(-150, -50)
        self.offset_1 = PVector(0, -150)
        self.offset_2 = PVector(0, 150)
        for v in self.part_1:
            v.add(self.offset_1)
        for v in self.part_2:
            v.add(self.offset_2)
    
    
    def render_dot(self):
        fill(self.palette.random_color())
        p1 = self.pivot_1.copy().add(self.offset_2)
        p2 = self.pivot_2.copy().add(self.offset_1)
        p3 = self.pivot_3.copy().add(self.offset_2)
        p4 = self.pivot_4.copy().add(self.offset_1)
        r = 50
        ellipse(p1.x, p1.y, r, r)
        ellipse(p2.x, p2.y, r, r)
        ellipse(p3.x, p3.y, r, r)
        ellipse(p4.x, p4.y, r, r)    
        
