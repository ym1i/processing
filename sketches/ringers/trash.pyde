  # def w_rap(self):
    #     n_pegs = len(self.pegs)
    #     n_wrap = n_pegs
    #     start = int(random(n_pegs))
    #     current = start
    #     prev = -99
        
    #     beginShape(QUAD)
    #     fill(self.colors[2])
    #     vertex(self.pegs[current].x, self.pegs[current].y)
        
    #     while n_wrap > 0:
    #         r = random(1)
    #         if r < 0.125:
    #             next = current - 1
    #         elif r < 0.25:
    #             next = current + self.n_rows - 1
    #         elif r < 0.375:
    #             next = current + self.n_rows
    #         elif r < 0.5:
    #             next = current + self.n_rows + 1
    #         elif r < 0.625:
    #             next = current + 1
    #         elif r < 0.75:
    #             next = current - self.n_rows + 1
    #         elif r < 0.875:
    #             next = current - self.n_rows
    #         else:
    #             next = current - self.n_rows - 1
            
    #         next %= n_pegs
    #         if next == prev:
    #             continue
        
    #         # vertex(self.pegs[current].x, self.pegs[current].y)
    #         vertex(self.pegs[next].x, self.pegs[next].y)
            
    #         if next == start:
    #             break
            
    #         prev = current
    #         current = next
    #         n_wrap -= 1
            
    #     endShape(CLOSE)
    
    # -------------------------------------------------------------------------------------------------
    
    # def w_rap(self):
    #     prob = random(0.5, 1)
    #     wrapped = []
    #     for peg in self.pegs:
    #         if random(1) < 0.9:
    #             wrapped.append(peg)
    #     if not wrapped:
    #         wrapped.append(self.pegs[0])
        
    #     beginShape()
    #     fill(self.colors[2])
    #     strokeWeight(2)
        
    #     offset = self.pegs[0].r
        
    #     # Find Pegs in the same column (LEFT most column in the wrapped section), and vertex() downward
    #     current = wrapped[0]
    #     vertex(current.x - offset, current.y)
    #     target = [peg for peg in wrapped if peg.x == current.x]
    #     if target:
    #         for peg in target:
    #             if peg.y > current.y:
    #                 current = peg    
    #                 vertex(current.x - offset, current.y)        
    #     vertex(current.x, current.y + offset)
        
    #     # Find the bottom of the next right column recursively from the current position
    #     next = current
    #     current_x = current.x
    #     while True:
    #         if current_x + self.col_width >= width:
    #             break
    #         next_col = [peg for peg in wrapped if peg.x == current.x + self.col_width]
    #         if next_col:
    #             next = next_col[0]
    #             for peg in next_col:
    #                 if peg.y > next.y:
    #                     next = peg
                
    #             # FOR SMOOTH WRAP CURVE
    #             if next.y > current.y:
    #                 vertex(current.x - current.r * cos(PI/4), current.y + current.r * sin(PI/4))
    #                 vertex(next.x - next.r * cos(PI/4), next.y + next.r * sin(PI/4))
    #             elif next.y < current.y:
    #                 vertex(current.x + current.r * cos(PI/4), current.y + current.r * sin(PI/4))
    #                 vertex(next.x + next.r * cos(PI/4), next.y + next.r * sin(PI/4))
                
    #             vertex(next.x, next.y + offset)
    #             current = next
    #             current_x = next.x
    #         else:
    #             current_x += self.col_width
                
    #     # Find Pegs in the same column (right most column in the wrapped section), and vertex() upward
    #     current = next
    #     vertex(current.x + offset, current.y)
    #     target = [peg for peg in wrapped if peg.x == current.x]
    #     if target:
    #         for peg in target:
    #             if peg.y < current.y:
    #                 current = peg
    #                 vertex(current.x + offset, current.y)
                    
    #     # Find the TOP of the next left column recursively from the current position
    #     vertex(current.x, current.y - offset)
    #     while True:
    #         if current.x - self.col_width <= 0:
    #             break
    #         next_col = [peg for peg in wrapped if peg.x == current.x - self.col_width]
    #         if next_col:
    #             next = next_col[0]
    #             for peg in next_col:
    #                 if peg.y < next.y:
    #                     next = peg
                        
    #             # FOR SMOOTH WRAP CURVE
    #             if next.y > current.y:
    #                 vertex(current.x - current.r * cos(PI/4), current.y - current.r * sin(PI/4))
    #                 vertex(next.x - next.r * cos(PI/4), next.y - next.r * sin(PI/4))
    #             elif next.y < current.y:
    #                 vertex(current.x + current.r * cos(PI/4), current.y - current.r * sin(PI/4))
    #                 vertex(next.x + next.r * cos(PI/4), next.y - next.r * sin(PI/4))
                        
    #             vertex(next.x, next.y - offset)
    #             current = next
    #         else:
    #             current.x -= self.col_width
        
    #     vertex(wrapped[0].x, wrapped[0].y - offset)
        
    #     endShape(CLOSE)
