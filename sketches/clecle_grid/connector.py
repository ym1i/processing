

class Connector():
    
    def __init__(self, el1, el2, color ,plt):
        self.element_1 = el1
        self.element_2 = el2
        self.pos = PVector((el1.pos.x + el2.pos.x) * 0.5, el1.pos.y)
        self.verts = []
        self.color = color
        self.plt = plt
        
        self.connect()
        
    
    def connect(self):
        x = self.element_1.pos.x + self.element_1.r * cos(self.element_1.theta1)
        y = self.element_1.pos.y + self.element_1.r * sin(self.element_1.theta1)
        self.verts.append(PVector(x, y))
        x = self.element_1.pos.x + self.element_1.r * cos(self.element_1.theta4)
        y = self.element_1.pos.y + self.element_1.r * sin(self.element_1.theta4)
        self.verts.append(PVector(x, y))
        x = self.element_2.pos.x + self.element_2.r * cos(self.element_2.theta3)
        y = self.element_2.pos.y + self.element_2.r * sin(self.element_2.theta3)
        self.verts.append(PVector(x, y))
        x = self.element_2.pos.x + self.element_2.r * cos(self.element_2.theta2)
        y = self.element_2.pos.y + self.element_2.r * sin(self.element_2.theta2)
        self.verts.append(PVector(x, y))
        
    
    def connect_mesh(self):
        x1 = self.element_1.pos.x + self.element_1.r * cos(self.element_1.theta1)
        y1 = self.element_1.pos.y + self.element_1.r * sin(self.element_1.theta1)
        v1 = PVector(x1, y1)
        x2 = self.element_1.pos.x + self.element_1.r * cos(self.element_1.theta4)
        y2 = self.element_1.pos.y + self.element_1.r * sin(self.element_1.theta4)
        v2 = PVector(x2, y2)
        x3 = self.element_2.pos.x + self.element_2.r * cos(self.element_2.theta2)
        y3 = self.element_2.pos.y + self.element_2.r * sin(self.element_2.theta2)
        v3 = PVector(x3, y3)
        x4 = self.element_2.pos.x + self.element_2.r * cos(self.element_2.theta3)
        y4 = self.element_2.pos.y + self.element_2.r * sin(self.element_2.theta3)
        v4 = PVector(x4, y4)
        
        n = 15
        v1_2 = PVector.sub(v2, v1)
        dv1_2 = v1_2.copy().div(n)
        v3_4 = PVector.sub(v4, v3)
        dv3_4 = v3_4.copy().div(n)
        
        self.verts.append(v1)
        self.verts.append(v3)
        for i in range(n):
            self.verts.append(v1.copy().add(dv1_2.copy().mult(i+1)))
            self.verts.append(v3.copy().add(dv3_4.copy().mult(i+1)))
        self.verts.append(v2)
        self.verts.append(v4)
        
                
    def update(self):
        self.verts = []
        self.connect()
        # self.connect_mesh()
            
    
    def render(self):
        fill(255)
        beginShape()
        for v in self.verts:
            vertex(v.x, v.y)
        endShape(CLOSE)
        
        
        # RECT WITH PADDING
        fill(self.color)
        beginShape()
        for v in self.verts:
            u = PVector.sub(v, self.pos)
            du = u.copy().mult(0.5)
            vertex(self.pos.x + du.x, self.pos.y + du.y)
        endShape(CLOSE)
        
        
        # MESH
        # noFill()
        # strokeWeight(1)
        # beginShape(QUAD_STRIP)
        # for v in self.verts:
        #     vertex(v.x, v.y)
        # endShape(CLOSE)
        
