from blob import Blob


class Element():
    
    def __init__(self, pegs, pegs_to_wrap, n_cols, n_rows, palette):
        self.pegs = pegs
        self.pegs_to_wrap = pegs_to_wrap
        self.n_rows = n_cols
        self.n_cols = n_rows
        self.palette = palette
        self.wrapper = []
        
        self.blob = Blob(pegs, pegs_to_wrap, n_rows, n_cols)
        
    
    def render(self):
        self.blob.render(self.palette.random_color())
        
        # beginShape()
        # fill(self.palette.random_color())
        # # noFill()
        # stroke(0)
        # strokeWeight(1)
        # for v in self.wrapper:
        #     vertex(v.x, v.y)
        # endShape(CLOSE)
            
            
        for peg in self.pegs:
            peg.render(self.palette.random_color())
            
    
    def wrap(self):
        for i, peg in enumerate(self.pegs_to_wrap):
            prev_i = self.pegs_to_wrap[(i - 1) % len(self.pegs_to_wrap)]
            next_i = self.pegs_to_wrap[(i + 1) % len(self.pegs_to_wrap)]
            cur = self.pegs[peg]
            prev = self.pegs[prev_i]
            next = self.pegs[next_i]            
            
            a_prev = PVector.sub(prev.vec, cur.vec).heading()
            a_next = PVector.sub(next.vec, cur.vec).heading()
            
            padding = 5
            r = cur.r + padding
            
            start = a_prev + HALF_PI
            stop = a_next - HALF_PI
            stop = stop + TAU if stop < start else stop
            stop = stop + TAU if stop < start else stop
            
            for i in range(20):
                a = map(i, 0, 19, start, stop)
                self.wrapper.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
                
                

            
    
                
        
                
                
            
    
            
            


























                
