

class Fragment():
    def __init__(self):
        self.vertices = []
        
    @property
    def n_vertices(self):
        return len(self.vertices)
    
        
    def add_vertices(self, v):
        self.vertices.append(v)
        
    def set_vertices(self, vertices):
        self.vertices = vertices
        
    def random_vertices(self):
        v1 = int(random(1, len(self.vertices)))
        v2 = int(random(1, len(self.vertices)))
        while v1 == v2:
            v2 = int(random(1, len(self.vertices)))    
            
        return v1, v2
    
    def mid_point(self, i):
        v1 = self.vertices[i]
        v2 = self.vertices[i - 1]
        m = PVector.add(v1, v2).div(2)
        dv = PVector.sub(v1, v2).div(random(10, 20))
        dv = dv.mult(-1) if random(1) < 0.5 else dv
 
        return m.add(dv)

        
    def render(self):
        beginShape()
        for v in self.vertices:
            vertex(v.x, v.y)
        endShape()
        
