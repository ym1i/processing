from fragment import Fragment
from geometry import square, circle, triangle, pentagon, hexagon, heptagon, octagon, decagon


class Frammenti():
    
    def __init__(self, x, y, w, h, type, decay, palette):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.center = PVector(x + w /2, y + h / 2)
        self.type = type
        self.decay = decay
        self.palette = palette
        self.fragments = []
        
        self.initial_shape()
        
        
    def render(self):
        if random(1) < 0.75:
            r = random(1)
            if r < 0.5:
                noStroke()
            elif r < 0.75:
                strokeWeight(3)
            else:
                strokeWeight(1)
                
            for fragment in self.fragments:
                fill(self.palette.random_color())
                fragment.render() 
        else:
            noFill()
            r = random(1)
            if r < 0.5:
                strokeWeight(8)
            elif r < 0.8:
                strokeWeight(3)
            else:
                strokeWeight(1)
            for fragment in self.fragments:
                stroke(self.palette.random_color())
                fragment.render()
        
    def initial_shape(self):
        fragment = Fragment()
        if self.type == 'rect':
            fragment.set_vertices(square(self.x, self.y, self.w, self.h))
        elif self.type == 'circle':
            fragment.set_vertices(circle(self.center, self.w / 2, self.w / 8))
        elif self.type == 'triangle':
            fragment.set_vertices(triangle(self.center, self.w / 2, rotation=True))
        elif self.type == 'pentagon':
            fragment.set_vertices(pentagon(self.center, self.w / 2, rotation=True))
        elif self.type == 'hexagon':
            fragment.set_vertices(hexagon(self.center, self.w / 2, rotation=True))
        elif self.type == 'heptagon':
            fragment.set_vertices(heptagon(self.center, self.w / 2, rotation=True))
        elif self.type == 'octagon':
            fragment.set_vertices(octagon(self.center, self.w / 2, rotation=True))
        elif self.type == 'decagon':
            fragment.set_vertices(decagon(self.center, self.w / 2, rotation=True))

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
            
            
            
    
            
