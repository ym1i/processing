

class Wrapper():
    
    def __init__(self, pegs, plt):
        self.pegs = pegs
        self.verts = []
        self.plt = plt
        
        self.wrap()
    
    
    def wrap(self):
        for i, peg in enumerate(self.pegs):
            cur = peg
            prev = self.pegs[i-1]
            next = self.pegs[(i+1) % len(self.pegs)]
            steps = 20
            
            # Prev to Cur
            v = PVector.sub(prev.loc, cur.loc)
            theta = v.heading() + HALF_PI
            x = cur.loc.x * cur.r * 1.2 * cos(theta)
            y = cur.loc.y * cur.r * 1.2 * sin(theta)
            v1 = PVector(x, y)
            
            # Cur to Next
            cur2next = PVector.sub(next.loc, cur.loc)
            theta = cur2next.heading() - HALF_PI
            x = cur.loc.x + cur.r * 1.2 * cos(theta)
            y = cur.loc.y + cur.r * 1.2 * sin(theta)
            v2 = PVector(x, y)
            x = next.loc.x + next.r * 1.2 * cos(theta)
            y = next.loc.y + next.r * 1.2 * sin(theta)
            v3 = PVector(x, y)
            
            # Ark between v1 and v2
            a1 = PVector.sub(v1, cur.loc).heading()
            a2 = PVector.sub(v2, cur.loc).heading()
            for i in range(steps):
                a = map(i, 0, steps-1, a1, a2)
                x = cur.loc.x + cur.r * 1.2 * cos(a)
                y = cur.loc.y + cur.r * 1.2 * sin(a)
                self.verts.append(PVector(x, y))
                                  
            # Line between v2 and v3
            dv = cur2next.copy().div(steps)
            for i in range(steps):
                self.verts.append(v2.copy().add(dv.copy().mult(i+1)))
            # self.verts.append(v3)
                
        
    def render(self):
        noFill()
        beginShape()
        for v in self.verts:
            vertex(v.x, v.y)
        endShape(CLOSE)
