from peg import Peg


class Wrapper():
    
    def __init__(self, pegs, id, n_cols, n_rows, palette):
        self.pegs = pegs
        self.element_id = id
        self.vertices = []
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.palette = palette
            
    
    def wrap(self):
        n_wrapped = len(self.element_id)
        scale = 1
        
        for i in range(n_wrapped):
            cur_peg = self.pegs[self.element_id[i]]
            next_peg = self.pegs[self.element_id[(i + 1) % n_wrapped]]
            theta = PVector.sub(next_peg.center, cur_peg.center).heading()
            cur_tangent = PVector(cur_peg.x + scale * cur_peg.r * sin(theta), cur_peg.y - scale * cur_peg.r * cos(theta))
            next_tangent = PVector(next_peg.x + scale *  next_peg.r * sin(theta), next_peg.y - scale * next_peg.r * cos(theta))
                    
            intervals = []
            d = PVector.dist(cur_tangent, next_tangent)
            n_intervals = int(d / 10)
            u = PVector.sub(next_tangent, cur_tangent).div(n_intervals)
        
            for k in range(n_intervals - 1):
                interval = cur_tangent.copy().add(u.copy().mult(k + 1))
                intervals.append(interval)
            
            # round the corner
            if i == 0:
                first_tangent = cur_tangent.copy()
            if i == n_wrapped - 1:
                last_tangent = next_tangent.copy()
            if i != 0:
                a1 = PVector.sub(prev_tangent, cur_peg.center).heading()
                a2 = PVector.sub(cur_tangent, cur_peg.center).heading()
                if a2 < a1:
                        a2 += TWO_PI 
                steps = int(map(a2 - a1, 0, TWO_PI, 0, 30))     
                for k in range(steps):
                    a = map(k, 0, steps - 1, a1, a2)
                    self.vertices.append(PVector(cur_peg.x + scale * cur_peg.r * cos(a), cur_peg.y + scale * cur_peg.r * sin(a)))
            for interval in intervals:
                self.vertices.append(interval)
        
            prev_tangent = next_tangent.copy()
        
        # round the first and last tangents
        a1 = PVector.sub(last_tangent, self.pegs[self.element_id[0]].center).heading()
        a2 = PVector.sub(first_tangent, self.pegs[self.element_id[0]].center).heading()
        if a2 < a1:
            a2 += TWO_PI
        steps = int(map(a2 - a1, 0, TWO_PI, 0, 30))
        for k in range(steps):
            a = map(k, 0, steps - 1, a1, a2)
            self.vertices.append(PVector(self.pegs[self.element_id[0]].x + scale * self.pegs[self.element_id[0]].r * cos(a), self.pegs[self.element_id[0]].y + scale * self.pegs[self.element_id[0]].r * sin(a)))
        
        
    def render(self, no_fill, peg_fill, ribon, fill_color, peg_color):
        beginShape()
        strokeWeight(5)
        stroke(0)
        
        if no_fill:
            noFill()
        else:        
            fill(fill_color) 
            
        for v in self.vertices:
            vertex(v.x, v.y)
            
        endShape()
        
        if ribon:
            beginShape(QUAD_STRIP)
            
            fill(self.palette.random_color())
            stroke(0)
            strokeWeight(2)
            w = 10 # string width
            for i, v in enumerate(self.vertices):
                fill(self.palette.random_color()) 
                if i == 0:
                    theta = PVector.sub(v, self.vertices[-1]).heading()
                    first_v1 = PVector(v.x + w * cos(theta - HALF_PI), v.y + w * sin(theta - HALF_PI))
                    first_v2 = PVector(v.x + w * cos(theta + HALF_PI), v.y + w * sin(theta + HALF_PI))
                else:
                    theta = PVector.sub(v, self.vertices[i - 1]).heading()
                v1 = PVector(v.x + w * cos(theta - HALF_PI), v.y + w * sin(theta - HALF_PI))
                v2 = PVector(v.x + w * cos(theta + HALF_PI), v.y + w * sin(theta + HALF_PI))
                
                vertex(v1.x, v1.y)
                vertex(v2.x, v2.y)
            
            vertex(first_v1.x, first_v1.y)
            vertex(first_v2.x, first_v2.y)
                
            endShape()
            
        # render pegs
        if peg_fill:
            for id in self.element_id:
                self.pegs[id].render(peg_color, peg_color)
    
