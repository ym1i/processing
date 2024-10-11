

class DeformedCircle():
    
    def __init__(self, x, y, r, c, s, n):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.vertices = []
        self.scale = s
        self.n_points = n
       
         
    def set_vertices(self):
        resolution = 0.002
        
        for i in range(self.n_points):
            a = map(i, 0, self.n_points - 1, 0, TAU)
            x = self.x + self.r  * cos(a)
            y = self.y + self.r  * sin(a)
            n = map(noise(x * resolution, y * resolution), 0, 1, -self.scale, self.scale)
            self.vertices.append(PVector(x + n, y + n))
            
    
    def render(self):
        fill(self.c)
        stroke(0)
        strokeWeight(1)
        beginShape()
        for v in self.vertices:
            curveVertex(v.x, v.y)
            if v == self.vertices[0] or v == self.vertices[-1]:
                curveVertex(v.x, v.y)
        endShape(CLOSE)
        
    def super_circle(self, inner_circle, palette):
        fill(self.c)
        stroke(0)
        strokeWeight(1)
        beginShape(QUAD_STRIP)
        for i, v in enumerate(self.vertices):
            fill(palette.random_color())
            vertex(v.x, v.y)
            vertex(inner_circle.vertices[i].x, inner_circle.vertices[i].y)
        endShape(CLOSE)    
    
    
