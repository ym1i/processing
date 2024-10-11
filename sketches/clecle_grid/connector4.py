

class Connector4():
    
    def __init__(self, el1, el2, el3, el4, color, plt):
        self.element_1 = el1
        self.element_2 = el2
        self.element_3 = el3
        self.element_4 = el4
        self.pos = PVector((el1.pos.x + el2.pos.x) * 0.5, (el1.pos.y + el3.pos.y) * 0.5)
        self.verts = []
        self.color = color
        self.plt = plt
        
        self.connect()
        
    
    def connect(self):
        x = self.element_1.pos.x + self.element_1.r * cos(self.element_1.theta1)
        y = self.element_1.pos.y + self.element_1.r * sin(self.element_1.theta1)
        self.verts.append(PVector(x, y))
        x = self.element_2.pos.x + self.element_2.r * cos(self.element_2.theta2)
        y = self.element_2.pos.y + self.element_2.r * sin(self.element_2.theta2)
        self.verts.append(PVector(x, y))
        x = self.element_3.pos.x + self.element_3.r * cos(self.element_3.theta3)
        y = self.element_3.pos.y + self.element_3.r * sin(self.element_3.theta3)
        self.verts.append(PVector(x, y))
        x = self.element_4.pos.x + self.element_4.r * cos(self.element_4.theta4)
        y = self.element_4.pos.y + self.element_4.r * sin(self.element_4.theta4)
        self.verts.append(PVector(x, y))
        
    
    def update(self):
        self.verts = []
        self.connect()
            
    
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
