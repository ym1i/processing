

class Triangle():
    
    def __init__(self, side, peg_r):
        self.vertices = []
        self.wraps = []
        self.side = side
        self.r = peg_r
        
    
    def add_vertices(self, v):
        self.vertices.append(v)
        
    
    def wrap(self):
        for i, v in enumerate(self.vertices):
            prev = self.vertices[i - 1]
            next = self.vertices[(i + 1) % len(self.vertices)]
            a_prev = PVector.sub(prev, v).heading()
            a_next = PVector.sub(next, v).heading()
            start = a_prev + HALF_PI
            stop =  a_next - HALF_PI
            stop = stop + TAU if start > stop else stop
            r = self.r / 1.5
            
            for i in range(20):
                a = map(i, 0, 19, start, stop)
                self.wraps.append(PVector(v.x + r * cos(a), v.y + r * sin(a)))   
        
    
    def render(self, c, sw=1, no_fill=True, no_stroke=False):
        noFill() if no_fill else fill(c)
        noStroke() if no_stroke else stroke(0)
        strokeWeight(sw)
        beginShape()
        for v in self.wraps:
            vertex(v.x, v.y)
        endShape(CLOSE)
