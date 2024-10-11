from random import random, randint, shuffle
from peg import Peg
from frammenti import Frammenti
from wrap import Wrap
from cover import Cover


class SoMuchPain():
    
    def __init__(self, palette):
        self.pegs = []
        self.n_cols = 3
        self.n_rows = 3
        self.grid_width = width / (self.n_cols + 1)
        self.grid_height = height / (self.n_rows + 1)
        self.palette = palette
        
        self.pegs_to_wrap = []
        self.main_wrap = Wrap(self.palette)
        self.element_1 = []
        self.element_2 = []
        self.element_3 = []
        self.element_1_wrap = Wrap(palette)
        self.element_2_wrap = Wrap(palette)
        self.element_3_wrap = Wrap(palette)
        
        self.grid_layout()
        self.select_pegs_to_wrap()
        self.pprint()
            
        
    def add_peg(self, x, y, r, style):
        self.pegs.append(Peg(x, y, r, style))
        
    
    def grid_layout(self):
        r = self.grid_width * 0.3
        for j in range(1, self.n_rows + 1):                
            for i in range(1, self.n_cols + 1):
                self.add_peg(self.grid_width * i, self.grid_height * j, r, 'solid')
    
    
    def select_pegs_to_wrap(self):
        n = self.n_cols * self.n_rows - 1
        visited = []
        current = randint(0, n - 1)
        self.pegs_to_wrap.append(current)
        visited.append(current)
        
        for i in range(n - 1):
            next, visited, complete = self.pick_neighbor(current, visited)
            if not complete:
                break
            self.pegs_to_wrap.append(next)
            current = next
        
        if len(self.pegs_to_wrap) == 1:
            self.pegs_to_wrap.append((current + 1) % len(self.pegs))
            
        self.element_1 = self.pegs_to_wrap[0:len(self.pegs_to_wrap)]
        # self.element_2 = [self.pegs_to_wrap[randint(0, len(self.pegs_to_wrap) - 1)]]
        
        # el_1 = min(4, len(self.pegs_to_wrap))
        # self.element_1 = self.pegs_to_wrap[:el_1]
       
        # if el_1 < len(self.pegs_to_wrap):
        #     self.element_2 = self.pegs_to_wrap[el_1:len(self.pegs_to_wrap)]
        # else:
        #     self.element_2.append(self.element_1[-1])
        
        # self.element_3.append(self.element_2[-1])
        # if el_1 + 1 < len(self.pegs_to_wrap):
        #     self.element_3.append(self.pegs_to_wrap[el_1 + 1])
        # else:
        #     self.element_3.append(self.element_2[-1])    
        
    
    def render(self):
        # Pick 2 different colors for element body
        c1 = randint(0, len(self.palette.colors) - 1)
        c2 = randint(0, len(self.palette.colors) - 1)
        while c1 == c2:
            c1 = randint(0, len(self.palette.colors) - 1)
            c2 = randint(0, len(self.palette.colors) - 1)
        
        self.element_wrapping(self.element_1, self.element_1_wrap)
        self.element_1_wrap.render(no_fill=False, ribon=True, fill_color=self.palette.colors[c1])
        # self.element_wrapping(self.element_2, self.element_2_wrap)
        # self.element_2_wrap.render(no_fill=False, ribon=False, fill_color=self.palette.colors[c2])
        # self.element_wrapping(self.element_3, self.element_3_wrap)
        # self.element_3_wrap.render(no_fill=False, ribon=False, fill_color=self.palette.random_color())
        
        # Frammenti
        frammenti_1 = Frammenti(200, 200, 400, 400, self.element_1_wrap.vertices,'custom', 'no', self.palette)
        for i in range(5):
            frammenti_1.split()
        frammenti_1.render() 
        
        # frammenti_2 = Frammenti(200, 200, 400, 400, self.element_2_wrap.vertices,'custom', 'no', self.palette)
        # for i in range(2):
        #     frammenti_2.split()
        # frammenti_2.render() 

        
        # Wrap selected pegs and render wrap string
        self.wrapping()
        self.main_wrap.render(no_fill=False, ribon=False, fill_color=self.palette.random_color())
        
        self.element_1_wrap.render(no_fill=True, ribon=True, fill_color=self.palette.colors[c1])
    
            
        # Render Pegs in Wrapped    
        for id in self.pegs_to_wrap:
            self.pegs[id].render(self.palette.random_color(), self.palette.random_color)
        
        
    def wrapping(self):
        n_wrapped = len(self.pegs_to_wrap)
        scale = 1
        
        for i in range(n_wrapped):
            cur_peg = self.pegs[self.pegs_to_wrap[i]]
            next_peg = self.pegs[self.pegs_to_wrap[(i + 1) % n_wrapped]]
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
                    self.main_wrap.add_vertex(PVector(cur_peg.x + scale * cur_peg.r * cos(a), cur_peg.y + scale * cur_peg.r * sin(a)))
            for interval in intervals:
                self.main_wrap.add_vertex(interval)
        
            prev_tangent = next_tangent.copy()
        
        # round the first and last tangents
        a1 = PVector.sub(last_tangent, self.pegs[self.pegs_to_wrap[0]].center).heading()
        a2 = PVector.sub(first_tangent, self.pegs[self.pegs_to_wrap[0]].center).heading()
        if a2 < a1:
            a2 += TWO_PI
        steps = int(map(a2 - a1, 0, TWO_PI, 0, 30))
        for k in range(steps):
            a = map(k, 0, steps - 1, a1, a2)
            self.main_wrap.add_vertex(PVector(self.pegs[self.pegs_to_wrap[0]].x + scale * self.pegs[self.pegs_to_wrap[0]].r * cos(a), self.pegs[self.pegs_to_wrap[0]].y + scale * self.pegs[self.pegs_to_wrap[0]].r * sin(a)))
        
    
    def element_wrapping(self, elements, wrap):
        r = self.grid_width / 2
        sorted_pegs = []
        for j in range(self.n_rows):
            sorted_pegs.append(sorted([peg for peg in elements if peg in range(j * self.n_rows, j * self.n_rows + self.n_cols)]))
    
        cur = sorted(elements)[0]
        cur_row = cur / self.n_rows
        
        # start at CUR, go RIGHT to the right edge in the same row
        
        wrap.add_vertex(PVector(self.pegs[cur].x, self.pegs[cur].y - r))
        for i in sorted_pegs[cur_row]:
            if i != cur:
                wrap.add_vertex(PVector(self.pegs[i].x, self.pegs[i].y - r))
                cur = i
                
        # ROUND the courner
        self.round_corner(1.5 * PI, TWO_PI, cur, wrap)
                
        # go DOWN along the RIGHT edge
        for j in range(cur_row, self.n_rows):
            if sorted_pegs[j]:
                next = sorted_pegs[j][-1]
            
                if cur % self.n_cols == next % self.n_cols:
                    # SAME COL, just go DOWN
                    wrap.add_vertex(PVector(self.pegs[next].x + r, self.pegs[next].y))
                    cur = next
                elif cur % self.n_cols < next % self.n_cols:
                    # go 1 COL RIGHT 1 ROW DOWN, then go RIGHT to the right edge in the row reacing to NEXT
                    
                    # ROUND the corner
                    self.round_corner(PI, HALF_PI, cur + 1, wrap)
                    
                    cur += self.n_cols + 1
                    for i in range(cur, next + 1):
                        wrap.add_vertex(PVector(self.pegs[i].x, self.pegs[i].y - r))
                    
                    cur = next        
                    # ROUND the corner
                    self.round_corner(1.5 * PI, TWO_PI, cur, wrap)
                    
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                    dcol = cur % self.n_cols - next % self.n_cols
                    # go LEFT several cols in the current row until the NEXT is located just at left bottom
                    
                    # ROUND the corner
                    self.round_corner(0, HALF_PI, cur, wrap)
                    
                    for i in range(dcol - 1):
                        cur -= 1
                        wrap.add_vertex(PVector(self.pegs[cur].x, self.pegs[cur].y + r))
                        
                    # ROUND the corner
                    self.round_corner(1.5 * PI, PI, cur + self.n_cols, wrap)
                    wrap.add_vertex(PVector(self.pegs[next].x + r, self.pegs[next].y))
                    cur = next
                    
        # start at CUR, go LEFT to the left edge in the same row
        
        # ROUND the corner
        self.round_corner(0, HALF_PI, cur, wrap)
        
        cur_row = cur / self.n_rows
        for i in reversed(sorted_pegs[cur_row]):
            if i != cur:
                # self.element_wrap.add_vertex(PVector(self.pegs[i].x, self.pegs[i].y + r))
                wrap.add_vertex(PVector(self.pegs[i].x, self.pegs[i].y + r))
                cur = i
                
        # ROUND the corner
        self.round_corner(HALF_PI, PI, cur, wrap)
                
        # go UP along the LEFT edge
        for j in reversed(range(cur_row)):
            if sorted_pegs[j]:
                next = sorted_pegs[j][0]
                if cur % self.n_cols == next % self.n_cols:
                    # go UP in the SAME column
                    # vertex(self.pegs[next].x - r, self.pegs[next].y)
                    # self.element_wrap.add_vertex(PVector(self.pegs[next].x - r, self.pegs[next].y))
                    wrap.add_vertex(PVector(self.pegs[next].x - r, self.pegs[next].y))
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                     # go up 1 COL LEFT and 1 ROW UP, then go LEFT to the left edge in the same row ([cur_row - 1])
                     
                     # ROUND the corner
                     self.round_corner(TWO_PI, 1.5 * PI, cur - 1, wrap)
                     
                     cur = cur - self.n_cols - 1
                     for i in reversed(range(next, cur + 1)):
                        # vertex(self.pegs[i].x, self.pegs[i].y + r)
                        # self.element_wrap.add_vertex(PVector(self.pegs[i].x, self.pegs[i].y + r))
                        wrap.add_vertex(PVector(self.pegs[i].x, self.pegs[i].y + r))
                     cur = next
                     
                     # ROUND the corner
                     self.round_corner(HALF_PI, PI, cur, wrap)
                     
                elif cur % self.n_cols < next % self.n_cols:
                    dcol = next % self.n_cols - cur % self.n_cols
                    # go RIGHT DCOLs in CUR_ROW until the NEXT is at 1 COL RIGHT and 1 ROW UP
                    
                    # ROUND the corner
                    self.round_corner(PI, 1.5 * PI, cur, wrap)
                    
                    for i in range(dcol - 1):
                        cur += 1
                        # vertex(self.pegs[cur].x, self.pegs[cur].y - r)
                        # self.element_wrap.add_vertex(PVector(self.pegs[cur].x, self.pegs[cur].y - r))
                        wrap.add_vertex(PVector(self.pegs[cur].x, self.pegs[cur].y - r))
                        
                    # ROUND the corner
                    self.round_corner(HALF_PI, 0, cur - self.n_cols, wrap)
                            
                    # vertex(self.pegs[next].x - r, self.pegs[next].y)
                    # self.element_wrap.add_vertex(PVector(self.pegs[next].x - r, self.pegs[next].y))
                    wrap.add_vertex(PVector(self.pegs[next].x - r, self.pegs[next].y))
                    cur = next
            
        # # ROUND the corner
        self.round_corner(PI, 1.5 * PI, cur, wrap)
        # endShape()
    
    
    def round_corner(self, theta_1, theta_2, peg_id, wrap):
        delta = PI / 20
        for i in range(10):
            if theta_2 > theta_1:
                theta = map(i, 0, 9, theta_1 + delta, theta_2 - delta)
            else:
                theta = map(i, 0, 9, theta_1 - delta, theta_2 + delta)
            # theta = map(i, 0, 9, theta_1, theta_2)
            x = self.pegs[peg_id].x + self.grid_width / 2 * cos(theta)
            y = self.pegs[peg_id].y + self.grid_width / 2 * sin(theta)
            # vertex(x, y)
            # self.element_wrap.add_vertex(PVector(x, y))
            wrap.add_vertex(PVector(x, y))
        
    
    def pick_neighbor(self, current, visited):
        count = 0
        while count < 9999:
            r = noise(current, count)
            if r < 0.125:
                next = current - self.n_cols - 1
            elif r < 0.25:
                next = current - self.n_cols
            elif r < 0.375:
                next = current - self.n_cols + 1
            elif r < 0.5:
                next = current - 1
            elif r < 0.625:
                next = current + 1
            elif r < 0.75:
                next = current + self.n_cols - 1
            elif r < 0.875:
                next = current + self.n_cols
            else:
                next = current + self.n_cols + 1
                
            next %= self.n_cols * self.n_rows
            
            d = PVector.dist(self.pegs[current].center, self.pegs[next].center)
            if d < self.grid_width * sqrt(2) + 2 and next not in visited:
                break
            count += 1
        
        if count == 9999:
            print 'it is dead end'
            print 'next: ', next 
            print 'count:', count
            return next, visited, False
        else:
            print 'count:', count
            visited.append(next)
            return next, visited, True
        
    def pprint(self):
        print 'pegs_to_wrap: ', self.pegs_to_wrap
        print 'element_1: ', self.element_1
        print 'element_2: ', self.element_2
        print 'element_3: ', self.element_3
                
                
    # def cover_wrapping(self, j):
    
    #     self.covers.append(Cover(self.palette))
    #     for id in self.element_1:
    #          self.covers[0].add_peg(self.pegs[id])
    #     scale = 1 + j * 0.3
    #     n_covered = len(self.element_1)
        
    #     for i in range(n_covered):
    #         cur_peg = self.pegs[self.element_1[i]]
    #         next_peg = self.pegs[self.element_1[(i + 1) % n_covered]]
    #         theta = PVector.sub(next_peg.center, cur_peg.center).heading()
    #         cur_tangent = PVector(cur_peg.x + scale * cur_peg.r * sin(theta), cur_peg.y - scale * cur_peg.r * cos(theta))
    #         next_tangent = PVector(next_peg.x + scale *  next_peg.r * sin(theta), next_peg.y - scale * next_peg.r * cos(theta))
                    
    #         intervals = []
    #         d = PVector.dist(cur_tangent, next_tangent)
    #         n_intervals = int(d / 10)
    #         u = PVector.sub(next_tangent, cur_tangent).div(n_intervals)
        
    #         for k in range(n_intervals - 1):
    #             interval = cur_tangent.copy().add(u.copy().mult(k + 1))
    #             intervals.append(interval)
            
    #         # round the corner
    #         if i == 0:
    #             first_tangent = cur_tangent.copy()
    #         if i == n_covered - 1:
    #             last_tangent = next_tangent.copy()
    #         if i != 0:
    #             a1 = PVector.sub(prev_tangent, cur_peg.center).heading()
    #             a2 = PVector.sub(cur_tangent, cur_peg.center).heading()
    #             if a2 < a1:
    #                     a2 += TWO_PI 
    #             steps = int(map(a2 - a1, 0, TWO_PI, 0, 30))     
    #             for k in range(steps):
    #                 a = map(k, 0, steps - 1, a1, a2)
    #                 self.covers[j].add_vertex(PVector(cur_peg.x + scale * cur_peg.r * cos(a), cur_peg.y + scale * cur_peg.r * sin(a)))
    #         for interval in intervals:
    #             self.covers[j].add_vertex(interval)
        
    #         prev_tangent = next_tangent.copy()
        
        # round the first and last tangents
        # a1 = PVector.sub(last_tangent, self.pegs[self.element_1[0]].center).heading()
        # a2 = PVector.sub(first_tangent, self.pegs[self.element_1[0]].center).heading()
        # if a2 < a1:
        #     a2 += TWO_PI
        # steps = int(map(a2 - a1, 0, TWO_PI, 0, 30))
        # for k in range(steps):
        #     a = map(k, 0, steps - 1, a1, a2)
        #     self.covers[j].add_vertex(PVector(self.pegs[self.element_1[0]].x + scale * self.pegs[self.element_1[0]].r * cos(a), self.pegs[self.element_1[0]].y + scale * self.pegs[self.element_1[0]].r * sin(a)))
    
    
    # def add_frammenti(self, x, y, w, h, type, decay, palette):
    #     self.pegs.append(Frammenti(x, y, w, h, type, decay, palette))
  
    
      
        
          
            
              
                
                  
                    
                      
                        
                          
                            
                              
                                
                                  
                                    
                                      
                                        
                                          
                                            
                                              
                                                
                                                  
                                                    
                                                      
                                                        
                                                            
    
    # def calc_tangent_for_reverse(self, cur_peg, next_peg ,theta):
    #     if cur_peg.reverse:
    #         if theta == 0 or theta == PI:
    #             theta += 0.3
    #             cur_tangent = PVector(cur_peg.x + cur_peg.r * sin(theta), cur_peg.y + cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x - next_peg.r * sin(theta), next_peg.y - next_peg.r * cos(theta))
    #         elif theta == HALF_PI or theta == - HALF_PI:
    #             theta += 0.3
    #             cur_tangent = PVector(cur_peg.x - cur_peg.r * sin(theta), cur_peg.y - cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x + next_peg.r * sin(theta), next_peg.y + next_peg.r * cos(theta))
    #         elif theta == QUARTER_PI or round(theta, 2) == round(-3 * QUARTER_PI, 2):
    #             cur_tangent = PVector(cur_peg.x - cur_peg.r * sin(theta), cur_peg.y + cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x + next_peg.r * sin(theta), next_peg.y - next_peg.r * cos(theta))    
    #         elif round(theta, 2) == round(3 * QUARTER_PI, 2) or theta == - QUARTER_PI:
    #             cur_tangent = PVector(cur_peg.x - cur_peg.r * sin(theta), cur_peg.y + cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x + next_peg.r * sin(theta), next_peg.y - next_peg.r * cos(theta))
        
    #     if next_peg.reverse:
    #         if theta == 0 or theta == PI:
    #             theta += 0.3
    #             cur_tangent = PVector(cur_peg.x + cur_peg.r * sin(theta), cur_peg.y - cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x - next_peg.r * sin(theta), next_peg.y + next_peg.r * cos(theta))
    #         elif theta == HALF_PI or theta == - HALF_PI:
    #             theta += 0.3
    #             cur_tangent = PVector(cur_peg.x + cur_peg.r * sin(theta), cur_peg.y - cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x - next_peg.r * sin(theta), next_peg.y + next_peg.r * cos(theta))
    #         elif theta == QUARTER_PI or round(theta, 2) == round(-3 * QUARTER_PI, 2):
    #             cur_tangent = PVector(cur_peg.x + cur_peg.r * sin(theta), cur_peg.y - cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x - next_peg.r * sin(theta), next_peg.y + next_peg.r * cos(theta))
    #         elif round(theta, 2) == round(3 * QUARTER_PI, 2) or theta == - QUARTER_PI:
    #             cur_tangent = PVector(cur_peg.x + cur_peg.r * sin(theta), cur_peg.y - cur_peg.r * cos(theta))
    #             next_tangent = PVector(next_peg.x -  next_peg.r * sin(theta), next_peg.y + next_peg.r * cos(theta))
                
    #     return cur_tangent, next_tangent
