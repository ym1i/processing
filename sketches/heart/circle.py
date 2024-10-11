
class Circle():
    
    def __init__(self, pos, r, color, plt):
        self.pos = pos
        self.r = r
        self.vertices = []
        self.plt = plt
        self.color = color
        
        self.set_vertices()
        
    
    def set_vertices(self):
        n = 100
        for i in range(n):
            a = map(i, 0, n, 0, TAU)
            x = self.pos.x + self.r * cos(a)
            y = self.pos.y + self.r * sin(a)
            self.vertices.append(PVector(x, y))
            
    
    def split(self):
        n = 50
        part1 = []
        part2 = []
        theta = PI
        
        for i , v in enumerate(self.vertices):
            if i < n:
                part1.append(v)
        
        pivot = self.vertices[n]
        pivot.add(PVector(self.r * cos(-theta), self.r * sin(-theta)))
        for i in range(n):
            a = map(i, 0, n, 0, TAU - theta)
            part2.append(PVector(pivot.x + self.r * cos(a), pivot.y + self.r * sin(a)))
                
        self.part1 = part1
        self.part2 = part2
        
    
    def render(self):
        fill(self.color)
        beginShape()
        for v in self.vertices:
            vertex(v.x, v.y)
        endShape(CLOSE)
        
    def render_semi_circle(self):
        fill(self.color)
        beginShape()
        for v in self.part1:
            vertex(v.x, v.y)
        endShape(CLOSE)
        beginShape()
        for v in self.part2:
            vertex(v.x, v.y)
        endShape(CLOSE)
