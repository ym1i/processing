

class Wrap():
    
    def __init__(self, pegs, layout, style, body_color):
        self.pegs = pegs
        self.layout = layout
        self.style = style
        self.body_color = body_color
        
        
    def mushroom(self):
        if self.layout == 'grid_3':
            grid = 3
        elif self.layout == 'grid_4':
            grid = 4
        elif self.layout == 'grid_5':
            grid = 5
            
        if grid % 2 == 0:
            top = 0 if random(1) < 0.5 else grid - 1
        else:
            rand = random(1)
            if rand < 0.33:
                top = 0
            elif rand < 0.66:
                top = grid / 2
            else:
                top = grid - 1    
                
        beginShape()
        fill(self.body_color)
        strokeWeight(2)
        r = self.pegs[0].r
        offset = r * cos(PI/4)
        
        if top == 0:
            # left top corner
            left = grid * (grid - 1)
            right = grid - 1
            
            vertex(self.pegs[top].x - r, self.pegs[top].y)
            vertex(self.pegs[left].x - r, self.pegs[left].y)
            
            vertex(self.pegs[left].x + offset, self.pegs[left].y + offset)
            vertex(self.pegs[right].x + offset, self.pegs[right].y + offset)
            
            vertex(self.pegs[right].x, self.pegs[right].y - r)
            vertex(self.pegs[top].x, self.pegs[top].y - r)
            
        elif top == grid - 1:
            # right top corner
            left = 0
            right = (grid * grid) - 1
            
            vertex(self.pegs[top].x, self.pegs[top].y - r)
            vertex(self.pegs[left].x, self.pegs[left].y - r)
            
            vertex(self.pegs[left].x - offset, self.pegs[left].y + offset)
            vertex(self.pegs[right].x - offset, self.pegs[right].y + offset)
            
            vertex(self.pegs[right].x + r, self.pegs[right].y)
            vertex(self.pegs[top].x + r, self.pegs[top].y)
            
        else:
            # middle top
            left = grid * int(grid / 2)
            right = grid * int(grid / 2) + (grid - 1)
                
            vertex(self.pegs[top].x - offset, self.pegs[top].y - offset)
            vertex(self.pegs[left].x - offset, self.pegs[left].y - offset)
            
            vertex(self.pegs[left].x, self.pegs[left].y + r)
            vertex(self.pegs[right].x, self.pegs[right].y + r)
            
            vertex(self.pegs[right].x + offset, self.pegs[right].y - offset)
            vertex(self.pegs[top].x + offset, self.pegs[top].y - offset)
        
        endShape(CLOSE)
        
         # change PEG style at some positions
        self.pegs[top].style = 'bulls_3'
        self.pegs[left].style = 'bulls_3'
        self.pegs[right].style = 'bulls_3'
        
        # remove some PEGs at random
        protected = [top, left, right]    
        rand = int(random(len(self.pegs) * 0.8))
        for i in range(rand):
            id = int(random(len(self.pegs)))
            if id not in protected:
                self.pegs[id].style = 'none' 
               
    
        
    def bird(self):
        grid = 10
        r = self.pegs[0].r
        offset = r * cos(PI/4)
        fill(self.body_color)
        strokeWeight(2)
        
        beginShape()
        vertex(self.pegs[(grid - 1) * grid + 3].x - offset, self.pegs[(grid - 1) * grid + 3].y - offset)
        vertex(self.pegs[(grid - 4) * grid + 4].x + offset, self.pegs[(grid - 4) * grid + 4].y + offset)
        vertex(self.pegs[(grid - 4) * grid + 4].x, self.pegs[(grid - 4) * grid + 4].y - r)
        vertex(self.pegs[(grid - 4) * grid + 3].x, self.pegs[(grid - 4) * grid + 3].y - r)
        vertex(self.pegs[(grid - 4) * grid + 3].x - offset, self.pegs[(grid - 4) * grid + 3].y - offset)
        vertex(self.pegs[(grid - 3) * grid + 0].x + offset, self.pegs[(grid - 3) * grid + 0].y + offset)
        vertex(self.pegs[(grid - 3) * grid + 0].x - offset, self.pegs[(grid - 3) * grid + 0].y - offset)
        vertex(self.pegs[(grid - 5) * grid + 2].x - offset, self.pegs[(grid - 5) * grid + 2].y - offset)
        vertex(self.pegs[(grid - 7) * grid + 3].x - r, self.pegs[(grid - 7) * grid + 3].y)
        vertex(self.pegs[(grid - 7) * grid + 3].x - offset, self.pegs[(grid - 7) * grid + 3].y - offset)
        vertex(self.pegs[(grid - 8) * grid + 4].x - offset, self.pegs[(grid - 8) * grid + 4].y - offset)
        vertex(self.pegs[(grid - 8) * grid + 4].x, self.pegs[(grid - 8) * grid + 4].y - r)
        vertex(self.pegs[(grid - 8) * grid + 6].x, self.pegs[(grid - 8) * grid + 6].y - r)
        vertex(self.pegs[(grid - 8) * grid + 6].x + offset, self.pegs[(grid - 8) * grid + 6].y - offset)
        vertex(self.pegs[(grid - 7) * grid + 7].x + offset, self.pegs[(grid - 7) * grid + 7].y - offset)
        vertex(self.pegs[(grid - 7) * grid + 7].x + r, self.pegs[(grid - 7) * grid + 7].y)
        vertex(self.pegs[(grid - 5) * grid + 7].x + r, self.pegs[(grid - 5) * grid + 7].y)
        vertex(self.pegs[(grid - 2) * grid + 6].x + r, self.pegs[(grid - 2) * grid + 6].y)
        vertex(self.pegs[(grid - 2) * grid + 6].x + offset, self.pegs[(grid - 2) * grid + 6].y - offset)
        vertex(self.pegs[(grid - 1) * grid + 8].x + offset, self.pegs[(grid - 1) * grid + 8].y - offset)
        vertex(self.pegs[(grid - 1) * grid + 8].x, self.pegs[(grid - 1) * grid + 8].y + r)
        vertex(self.pegs[(grid - 1) * grid + 3].x, self.pegs[(grid - 1) * grid + 3].y + r)
        endShape(CLOSE)
        
        # change PEG style at some positions
        self.pegs[(grid - 3) * grid + 0].style = 'bulls_3'
        self.pegs[(grid - 1) * grid + 3].style = 'bulls_3'
        self.pegs[(grid - 1) * grid + 8].style = 'bulls_3'
        self.pegs[(grid - 2) * grid + 6].style = 'bulls_3'
        
        # remove some PEGs at random
        protected = [(grid - 1) * grid + 3, (grid - 4) * grid + 4, (grid - 4) * grid + 3, (grid - 3) * grid,
                     (grid - 5) * grid + 2, (grid - 7) * grid + 3, (grid - 8) * grid + 4, (grid - 8) * grid + 6,
                     (grid - 7) * grid + 7, (grid - 5) * grid + 7, (grid - 2) * grid + 6, (grid - 1) * grid + 8]
            
        r = random(len(self.pegs) / 5)
        for i in range(10):
            id = int(random(len(self.pegs)))
            if id not in protected:
                self.pegs[id].style = 'none' 
               
    
    def normal_wrap(self):
        prob = 0.6
        wrapped = []
        for peg in self.pegs:
            if random(1) < prob:
                wrapped.append(peg)
        if not wrapped:
            wrapped.append(self.pegs[0])
        
        # Find edges
        left_top = 0
        left_bottom = 0
        right_top = 0
        right_bottom = 0
        left_most = 0
        right_most = 0
        top_most = 0
        bottom_most = 0
        
        
        for i, peg in enumerate(wrapped):
            if peg.x <= wrapped[left_top].x and peg.y <= wrapped[left_top].y:
                left_top = i
            if peg.x <= wrapped[left_bottom].x and peg.y >= wrapped[left_bottom].y:
                left_bottom = i
            if peg.x >= wrapped[right_top].x and peg.y <= wrapped[right_top].y:
                right_top = i
            if peg.x >= wrapped[right_bottom].x and peg.y >= wrapped[right_bottom].y:
                right_bottom = i
            if peg.x < wrapped[left_most].x:
                left_most = i
            if peg.x > wrapped[right_most].x:
                right_most = i
            if peg.y < wrapped[top_most].y:
                top_most = i
            if peg.y > wrapped[bottom_most].y:
                bottom_most = i
                
        beginShape()
        fill(self.body_color)
        strokeWeight(2)
        r = wrapped[0].r
        offset = r * cos(PI/4)
        
        vertex(wrapped[left_top].x - r, wrapped[left_top].y)
        vertex(wrapped[left_most].x - r, wrapped[left_most].y)
        vertex(wrapped[left_bottom].x - r, wrapped[left_bottom].y)
        
        if wrapped[left_bottom].y < wrapped[bottom_most].y:
            vertex(wrapped[left_bottom].x - offset, wrapped[left_bottom].y + offset)
            vertex(wrapped[bottom_most].x - offset, wrapped[bottom_most].y + offset)
            vertex(wrapped[bottom_most].x, wrapped[bottom_most].y + r)
        else:    
            vertex(wrapped[left_bottom].x, wrapped[left_bottom].y + r)
            vertex(wrapped[bottom_most].x, wrapped[bottom_most].y + r)
        
        
        if wrapped[bottom_most].y > wrapped[right_bottom].y:
            vertex(wrapped[bottom_most].x + offset, wrapped[bottom_most].y + offset)
            vertex(wrapped[right_bottom].x + offset, wrapped[right_bottom].y + offset)
            vertex(wrapped[right_bottom].x + r, wrapped[right_bottom].y)
        else:
            vertex(wrapped[right_bottom].x, wrapped[right_bottom].y + r)
            vertex(wrapped[right_bottom].x + r, wrapped[right_bottom].y)
    
        
        if wrapped[right_bottom].x < wrapped[right_most].x:
            vertex(wrapped[right_bottom].x + offset, wrapped[right_bottom].y + offset)
            vertex(wrapped[right_most].x + offset, wrapped[right_most].y + offset)
            vertex(wrapped[right_most].x + r, wrapped[right_most].y)
        else:
            vertex(wrapped[right_most].x + r, wrapped[right_most].y)
        
        if wrapped[right_most].x > wrapped[right_top].x:
            vertex(wrapped[right_most].x + offset, wrapped[right_most].y - offset)
            vertex(wrapped[right_top].x + offset, wrapped[right_top].y - offset)
            vertex(wrapped[right_top].x, wrapped[right_top].y - r)
        else:
            vertex(wrapped[right_top].x + r, wrapped[right_top].y)
            vertex(wrapped[right_top].x, wrapped[right_top].y - r)
        
        if wrapped[right_top].y > wrapped[top_most].y:
            vertex(wrapped[right_top].x + offset, wrapped[right_top].y - offset)
            vertex(wrapped[top_most].x + offset, wrapped[top_most].y - offset)
            vertex(wrapped[top_most].x, wrapped[top_most].y - r)
        else:
            vertex(wrapped[right_top].x, wrapped[right_top].y - r)
            vertex(wrapped[top_most].x, wrapped[top_most].y - r)
        
        if wrapped[top_most].y < wrapped[left_top].y:
            vertex(wrapped[top_most].x - offset, wrapped[top_most].y - offset)
            vertex(wrapped[left_top].x - offset, wrapped[left_top].y - offset)
        else:
            vertex(wrapped[left_top].x, wrapped[left_top].y - r)
        
        endShape(CLOSE)
