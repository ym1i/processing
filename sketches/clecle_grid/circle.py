

class Circle():
    
    def __init__(self, pos, r, plt):
        self.pos = pos
        self.r = r
        self.theta1 = random(0, 0.5 * PI)
        self.theta2 = random(0.5 * PI, PI)
        self.theta3 = random(PI, 1.5 * PI)
        self.theta4 = random(1.5 * PI, TAU)
        # self.vel1 = PI * random(0.003, 0.006)
        # self.vel2 = PI * random(0.003, 0.006)
        # self.vel3 = PI * random(0.003, 0.006)
        # self.vel4 = PI * random(0.003, 0.006)
        n = 0.05
        self.vel1 = PI * noise(pos.x * n, pos.y  * n) * 0.01
        self.vel2 = PI * noise(pos.x  * n, pos.y * n) * 0.01
        self.vel3 = PI * noise(pos.x * n, pos.y * n) * 0.01
        self.vel4 = PI * noise(pos.x * n, pos.y * n) * 0.01
        self.verts = []
        self.plt = plt
        self.colour1 = plt.random_color()
        self.colour2 = plt.random_color()
        
        self.init_verts()
    
    
    def init_verts(self):
        n = 30
        for i in range(n):
            a = map(i, 0, n-1, self.theta1, self.theta2)
            self.verts.append(PVector(self.pos.x + self.r * cos(a), self.pos.y + self.r * sin(a)))
        for j in range(n):
            a = map(j, 0, n-1, self.theta3, self.theta4)
            self.verts.append(PVector(self.pos.x + self.r * cos(a), self.pos.y + self.r * sin(a)))
        
        
        
    def update(self):
        # if self.theta1 > PI:
        if self.theta1 > HALF_PI:
            self.vel1 *= -1
            # self.vel1 = -PI * random(0.003, 0.00305)
        elif self.theta1 < 0:
            self.vel1 *= -1
            
        if self.theta2 > PI:
            self.vel2 *= -1
            # self.vel2 = -PI * random(0.006, 0.00605)
        # elif self.theta2 < 0:
        elif self.theta2 < HALF_PI:
            self.vel2 *= -1
            
        # if self.theta3 > TAU:
        if self.theta3 > 1.5 * PI:
            self.vel3 *= -1
            # self.vel3 = -PI * random(0.005, 0.00505)
        elif self.theta3 < PI:
            self.vel3 *= -1
            
        if self.theta4 > TAU:
            self.vel4 *= -1
            # self.vel4 = -PI * random(0.008, 0.00805)
        # elif self.theta4 < PI:
        elif self.theta4 < 1.5 * PI:
            self.vel4 *= -1
            
        self.theta1 += self.vel1
        self.theta2 += self.vel2
        self.theta3 += self.vel3
        self.theta4 += self.vel4
        
        n = 30
        id = 0
        for i in range(n):
            if self.theta1 <= self.theta2:
                a = map(i, 0, n-1, self.theta1, self.theta2)
            else:
                a = map(i, 0, n-1, self.theta2, self.theta1)
            self.verts[id] = PVector(self.pos.x + self.r * cos(a), self.pos.y + self.r * sin(a))
            id += 1
        for j in range(n):
            if self.theta3 <= self.theta4:
                a = map(j, 0, n-1, self.theta3, self.theta4)
            else:
                a = map(j, 0, n-1, self.theta4, self.theta3)
            self.verts[id] = PVector(self.pos.x + self.r * cos(a), self.pos.y + self.r * sin(a))
            id += 1
        
    
    def render(self):
        # noFill()
        fill(255)
        beginShape()
        for v in self.verts:
            vertex(v.x, v.y)
        endShape(CLOSE)
        
        # fill(self.colour)
        # beginShape()
        # for v in self.verts:
        #     u = PVector.sub(v, self.pos)
        #     du = u.copy().div(5)
        #     w = self.pos.copy().add(du.copy().mult(2))
        #     vertex(w.x, w.y)
        # endShape(CLOSE)
        
        # fill(self.colour1)
        # beginShape()
        # for v in self.verts:
        #     theta = PVector.sub(v, self.pos).heading()
        #     r = self.r * 0.6
        #     vertex(self.pos.x + r * cos(theta), self.pos.y + r * sin(theta))
        # endShape(CLOSE)
        
        fill(self.colour2)
        beginShape()
        for v in self.verts:
            theta = PVector.sub(v, self.pos).heading()
            r = self.r * 0.5
            vertex(self.pos.x + r * cos(theta), self.pos.y + r * sin(theta))
        endShape(CLOSE)
        
