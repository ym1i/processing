# from fragment import Fragment
# from geometry import square, circle, triangle, pentagon, hexagon, heptagon, octagon, decagon


class Frammenti():
    
    def __init__(self, x, y, vertices, palette):
        self.x = x
        self.y = y
        self.vertices = vertices
        self.palette = palette
        self.fragments = []
        
        self.initial_shape(self.vertices)
        
        
    def render(self):
        strokeWeight(2)
        for fragment in self.fragments:
            fill(self.palette.random_color())
            fragment.render() 
        
        
    def initial_shape(self, vertices):
        fragment = Fragment()    
        fragment.set_vertices(vertices)
        self.fragments.append(fragment)
            
    def split(self):
        next = []
        for fragment in self.fragments:
            # Pick 2 vertices in each fragments
            v1, v2 = fragment.random_vertices() # index
            
            # Find mid points of v1 and v1-1, and v2 and v2-1
            m1 = fragment.mid_point(v1) # PVector
            m2 = fragment.mid_point(v2) # PVector
            
            split_1 = Fragment()
            split_2 = Fragment()
            
            if v1 < v2:
                for i in range(v1, v2):
                    split_1.add_vertices(PVector(fragment.vertices[i].x, fragment.vertices[i].y))
                split_1.add_vertices(m2)
                split_1.add_vertices(m1)
                split_1.add_vertices(PVector(fragment.vertices[v1].x, fragment.vertices[v1].y)) 
                
                for i in range(v2, fragment.n_vertices):
                    split_2.add_vertices(PVector(fragment.vertices[i].x, fragment.vertices[i].y))
                for j in range(v1):
                    split_2.add_vertices(PVector(fragment.vertices[j].x, fragment.vertices[j].y))
                split_2.add_vertices(m1)
                split_2.add_vertices(m2)
                split_2.add_vertices(PVector(fragment.vertices[v2].x, fragment.vertices[v2].y))    
            else:
                for i in range(v2, v1):
                    split_1.add_vertices(PVector(fragment.vertices[i].x, fragment.vertices[i].y))
                split_1.add_vertices(m1)
                split_1.add_vertices(m2)
                split_1.add_vertices(PVector(fragment.vertices[v2].x, fragment.vertices[v2].y)) 
                
                for i in range(v1, fragment.n_vertices):
                    split_2.add_vertices(PVector(fragment.vertices[i].x, fragment.vertices[i].y))
                for j in range(v2):
                    split_2.add_vertices(PVector(fragment.vertices[j].x, fragment.vertices[j].y))
                split_2.add_vertices(m2)
                split_2.add_vertices(m1)
                split_2.add_vertices(PVector(fragment.vertices[v1].x, fragment.vertices[v1].y)) 
                
    
            next.append(split_1)
            next.append(split_2)
        
        self.fragments = next
            
 
    
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
        
            
    
            
