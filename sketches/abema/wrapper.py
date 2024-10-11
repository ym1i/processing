

class Wrapper():
    
    def __init__(self):
        self.vertices = []
        
    
    def ameba_wrap(self, pegs):
        for i, cur in enumerate(pegs):
            if cur == pegs[0]:
                prev = pegs[-1]
                next = pegs[i + 1]
            if cur == pegs[-1]:
                prev = pegs[i - 1]
                next = pegs[0]
            else:
                prev = pegs[i - 1]
                next = pegs[i + 1]
                
            v1 = PVector.sub(prev.center, cur.center)
            v2 = PVector.sub(next.center, cur.center)
            ark_start = v1.heading()
            ark_stop = v2.heading()
            d1 = v1.mag() # distance between current peg and previous peg, use this as the radius of the ark
            d2 = v2.mag() # distance between current peg and next peg, use this as the radius of the ark
            steps = 20
            
            if i % 2 == 1: 
                ark_stop = ark_stop + TAU if ark_start > ark_stop else ark_stop # ark clockwise
            elif i % 2 == 0:
                ark_stop = ark_stop - TAU if ark_start < ark_stop else ark_stop # ark counter clockwise
            
            for j in range(steps):
                a = map(j, 0, steps - 1, ark_start, ark_stop)
                r = map(j, 0, steps - 1, d1 / 2, d2 / 2)
                self.vertices.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
    
            
    def wrap(self, pegs):
        for i, cur in enumerate(pegs):
            prev = pegs[(i - 1) % len(pegs)] 
            next = pegs[(i + 1) % len(pegs)]
            v1 = PVector.sub(prev.center, cur.center)
            v2 = PVector.sub(next.center, cur.center)
            ark_start = v1.heading() + HALF_PI 
            ark_stop = v2.heading() - HALF_PI 
            ark_stop = ark_stop + TAU if ark_start > ark_stop else ark_stop # ark clockwise
            padding = 80
            steps = 20
            
            for j in range(steps):
                a = map(j, 0, steps - 1, ark_start, ark_stop)
                r = cur.r + padding
                self.vertices.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
     
        
    def grid_wrap(self, pegs, n_rows, n_cols, toggle=False, even=False):
       
        # TOP ROW
        row = 0
        for col in range(n_cols):
            cur = pegs[col]
            prev = pegs[col - 1]
            next = pegs[col + 1]
            if col == 0:
                prev = pegs[col + (row + 1) * n_cols]
            elif col == n_cols - 1:
                next = pegs[col + (row + 1) * n_cols]
            
            self.ark(prev, cur, next, col, toggle)
        
        # RIGHT COLUMN
        col = n_cols - 1 
        for row in range(1, n_rows):
            cur = pegs[(row * n_cols) + col]
            prev = pegs[(row - 1) * n_cols + col]
            if row == n_rows - 1:
                next = pegs[(row * n_cols) + (col - 1)]
            else:
                next = pegs[(row + 1) * n_cols + col] 
            
            if even:
                row += 1
            self.ark(prev, cur, next, row, toggle)    
            
        # BOTTOM ROW
        row = n_rows - 1
        for col in reversed(range(n_cols - 1)):
            cur = pegs[(row * n_cols) + col]
            prev = pegs[(row * n_cols) + (col + 1)]
            next = pegs[(row * n_cols) + (col - 1)]
            if col == 0:
                next = pegs[(row - 1) * n_cols + col]
            
            if even:
                col += 1
            self.ark(prev, cur, next, col, toggle) 
           
        # LEFT COLUMN
        col = 0
        for row in reversed(range(n_rows - 1)):
            cur = pegs[(row * n_cols) + col]
            prev = pegs[(row + 1) * n_cols + col]
            next = pegs[(row - 1) * n_cols + col]
            if row == n_rows - 1:
                prev = pegs[(row * n_cols) + (col + 1)]
            elif row == 0:
                # next = pegs[row * n_cols + col + 1] 
                continue
            
            self.ark(prev, cur, next, row, toggle) 
             
    
    def ark(self, prev, cur, next, col, toggle=False):
        v1 = PVector.sub(prev.center, cur.center)
        v2 = PVector.sub(next.center, cur.center)
        ark_start = v1.heading()
        ark_stop = v2.heading()
        d1 = v1.mag() # distance between current peg and previous peg, use this as the radius of the ark
        d2 = v2.mag() # distance between current peg and next peg, use this as the radius of the ark
        steps = 20
        
        
        if toggle: # for change of the direction of the clock
            col += 1
        if col % 2 == 0: # if even col, then arc clockwise
            ark_stop = ark_stop + TAU if ark_start > ark_stop else ark_stop 
        elif col % 2 == 1: # if odd col, then arc counter clockwise
            ark_stop = ark_stop - TAU if ark_start < ark_stop else ark_stop 
        
        for k in range(steps):
            a = map(k, 0, steps - 1, ark_start, ark_stop)
            r = map(k, 0, steps - 1, d1 / 2, d2 / 2)
            self.vertices.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
    
    
    def render(self, c, sw=1, no_stroke=False, curve=False):
        fill(c)
        stroke(0)
        strokeWeight(sw)
        if no_stroke:
            noStroke()
        beginShape()
        for i, v in enumerate(self.vertices):
            if curve:
                if v == self.vertices[0] or v == self.vertices[-1]:
                    curveVertex(v.x, v.y)
                curveVertex(v.x, v.y)
            else:
                vertex(v.x, v.y)
        endShape(CLOSE)
        
        
        
