

class Blob():
    
    def __init__(self, base_pegs, ordered_pegs, n_rows, n_cols):
        self.base_pegs = base_pegs
        self.ordered_pegs = ordered_pegs
        self.n_rows = n_rows
        self.n_cols = n_cols
        
        self.sorted_pegs = self.sort_pegs()
        # self.sorted_pegs = [0, 1, 5, 8, 7, 6, 3]
        # self.sorted_pegs = [0, 1, 2, 5, 7, 6, 3]
        # self.sorted_pegs = [0, 1, 2, 5, 8, 7, 3]
        # self.sorted_pegs = [1, 2, 5, 8, 7, 6, 3]
        # self.sorted_pegs = [0, 4, 8, 7, 6, 3]
        # TODO
        # self.sorted_pegs = [0, 1, 2, 5, 6, 3]
        # self.sorted_pegs = [1, 5, 8, 7, 6, 3]
        self.vertices = []
        print 'sorted_pegs | ', self.sorted_pegs
        self.wrap()
        
    
    def sort_pegs(self):
        sorted_pegs = []
        pegs_2d = []
        for i in range(self.n_rows):
            pegs_2d.append(sorted([peg for peg in self.ordered_pegs if peg in range(i * self.n_rows, i * self.n_rows + self.n_cols)]))
        
        cur = sorted(self.ordered_pegs)[0]
        cur_row = cur / self.n_rows
        sorted_pegs.append(cur)
        
        # start at CUR, go RIGHT in cur_row
        for col in pegs_2d[cur_row]:
            if col != cur:
                sorted_pegs.append(col)
                cur = col
        
        # go DOWN along the RIGHT side
        for row in range(cur_row + 1, self.n_rows):
            if pegs_2d[row]:
                next = pegs_2d[row][-1]
                if self.is_same_col(cur, next):
                    sorted_pegs.append(next)
                    cur = next
                elif cur % self.n_cols < next % self.n_cols:
                    # => BOTTOM RIGHT => RIGHT => NEXT
                    cur = cur + self.n_cols + 1
                    for col in range(cur, next + 1):
                        sorted_pegs.append(cur)
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                    # go LEFT in cur_row where NEXT is at BOTTOM LEFT
                    col_to_left = cur % self.n_cols - next % self.n_cols
                    for i in range(col_to_left - 1):
                        cur -= 1
                        sorted_pegs.append(cur)
                    sorted_pegs.append(next)
                    cur = next
    
        # go LEFT in cur_row
        cur_row = cur / self.n_rows
        for col in reversed(pegs_2d[cur_row]):
            if col != cur:
                sorted_pegs.append(col)
                cur = col
        
        # go UP along the LEFT side
        for j in reversed(range(1, cur_row)):
            if pegs_2d[j]:
                next = pegs_2d[j][0]
                if cur % self.n_cols == next % self.n_cols:
                    # go UP in the SAME column
                    sorted_pegs.append(next)
                    cur = next
                elif cur % self.n_cols > next % self.n_cols:
                     # => TOP LEFT => LEFT => NEXT
                     cur = cur - self.n_cols - 1
                     for col in reversed(range(next, cur + 1)):
                         sorted_pegs.append(col)
                     cur = next
                elif cur % self.n_cols < next % self.n_cols:
                    # go RIGHT until the NEXT is at TOP RIGHT
                    col_to_right = next % self.n_cols - cur % self.n_cols
                    for i in range(col_to_right - 1):
                        cur += 1
                        sorted_pegs.append(cur)
                    sorted_pegs.append(next)            
                    cur = next
       
        return sorted_pegs    
    
    
    def wrap(self):
         for i, cur_i in enumerate(self.sorted_pegs):
            prev_i = self.sorted_pegs[(i - 1) % len(self.sorted_pegs)]
            next_i = self.sorted_pegs[(i + 1) % len(self.sorted_pegs)]
            cur = self.base_pegs[cur_i]
            prev = self.base_pegs[prev_i]
            next = self.base_pegs[next_i]
            
            a_prev = PVector.sub(prev.vec, cur.vec).heading()
            a_next = PVector.sub(next.vec, cur.vec).heading()
            r = cur.r + 5
            steps = 20
        
            if not self.is_same_col(cur_i, next_i) and not self.is_same_row(cur_i, next_i) and not self.is_same_col(cur_i, prev_i) and not self.is_same_row(cur_i, prev_i):
                print 'prev: {} | cur : {} | next : {}'.format(prev_i, cur_i, next_i)
            elif not self.is_same_col(cur_i, next_i) and not self.is_same_row(cur_i, next_i):
                print 'cur : {} | next : {}'.format(cur_i, next_i)
                if cur_i + self.n_cols + 1 == next_i:
                    pivot = self.base_pegs[cur_i + 1]
                elif cur_i + self.n_cols - 1 == next_i:
                    pivot = self.base_pegs[cur_i + self.n_cols]
                elif cur_i - self.n_cols - 1 == next_i:
                    pivot = self.base_pegs[cur_i - 1]
                elif cur_i - self.n_cols + 1 == next_i:
                    pivot = self.base_pegs[cur_i - self.n_cols]
                    
                start = a_prev + HALF_PI
                stop = a_next - QUARTER_PI    
                stop = stop + TAU if stop < start else stop
                
                if abs(start - stop) > TAU:
                    start = start - TAU if start > stop else start
                    stop = stop - TAU if start < stop else stop
                
                if abs(start - stop) < 0.02:
                    print 'cur: {} | next: {} | start: {} | stop: {}'.format(cur_i, next_i, start, stop)
                    print 'continue'
                    continue
                
        
                d1 = PVector.sub(pivot.vec, cur.vec).mag()
                d2 = PVector.sub(next.vec, pivot.vec).mag()
                for i in range(steps):
                    a = map(i, 0, steps - 1, start, stop)
                    r = map(i, 0, steps - 1, r, 0.5 * d1)
                    self.vertices.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
                    
                a_cur = PVector.sub(cur.vec, pivot.vec).heading()
                a_next = PVector.sub(next.vec, pivot.vec).heading()
                a_cur = a_cur + TAU if a_cur < a_next else a_cur
                for i in range(steps):
                    a = map(i, 0, steps - 1, a_cur, a_next)
                    r = map(i, 0, steps - 1, 0.5 * d1, 0.5 * d2)
                    self.vertices.append(PVector(pivot.x + r * cos(a), pivot.y + r * sin(a)))
                    
            elif not self.is_same_col(cur_i, prev_i) and not self.is_same_row(cur_i, prev_i):
                print 'cur : {} | prev : {}'.format(cur_i, prev_i)
                if prev_i == cur_i - self.n_cols - 1:
                    pivot = self.base_pegs[cur_i - self.n_cols]
                elif prev_i == cur_i - self.n_cols + 1:
                    pivot = self.base_pegs[cur_i + 1]
                elif prev_i == cur_i + self.n_cols + 1:
                    pivot = self.base_pegs[cur_i + self.n_cols]
                elif prev_i == cur_i + self.n_cols - 1:
                    pivot = self.base_pegs[cur_i - 1]
                    
                start = a_prev + QUARTER_PI
                stop = a_next - HALF_PI
                stop = stop + TAU if stop < start else stop
                d = PVector.sub(pivot.vec, cur.vec).mag()
                for i in range(steps):
                    a = map(i, 0, steps - 1, start, stop)
                    r = map(i, 0, steps - 1, 0.5 * d, r)
                    self.vertices.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
                
            else:
                start = a_prev + HALF_PI
                stop = a_next + 3 * HALF_PI
                if abs(start - stop) > TAU:
                    start = start - TAU if start > stop else start
                    stop = stop - TAU if start < stop else stop
                for i in range(steps):
                    a = map(i, 0, steps - 1, start, stop)
                    self.vertices.append(PVector(cur.x + r * cos(a), cur.y + r * sin(a)))
    
    
    def render(self, c):
        beginShape()
        fill(c)
        stroke(0)
        strokeWeight(1)
        for v in self.vertices:
            vertex(v.x, v.y)
        endShape(CLOSE)
        
    
    def is_same_col(self, i, j):
        return i % self.n_cols == j % self.n_cols
    
    
    def is_same_row(self, i, j):
        return i / self.n_cols == j / self.n_cols
    
    

 # def sort_pegs(self):
    #     pegs_2d = []
    #     pegs_2d_col = []
    #     for i in range(self.n_rows):
    #         pegs_2d.append(sorted([peg for peg in self.ordered_pegs if peg in range(i * self.n_rows, i * self.n_rows + self.n_cols)]))
    #     for i in range(self.n_cols):
    #         pegs_2d_col.append(sorted([peg for peg in self.ordered_pegs if peg % self.n_cols == i]))
            
    #     # print 'pegs_2d_col: ', pegs_2d_col
    #     print 'pegs_2d: ', pegs_2d 
        
    #     sorted_pegs = []
        
    #     for row in range(self.n_rows):
    #         if row == 0 and pegs_2d[row]:
    #             for peg in pegs_2d[row]:
    #                 sorted_pegs.append(peg)
    #         elif row == self.n_rows - 1 and pegs_2d[row]:
    #             for peg in reversed(pegs_2d[row]):
    #                 sorted_pegs.append(peg)
    #         else:
    #             if pegs_2d[row]:
    #                 sorted_pegs.append(pegs_2d[row][-1])
                    
    #     for row in reversed(range(1, self.n_rows -1)):
    #         if not pegs_2d[row][0] in sorted_pegs:
    #             sorted_pegs.append(pegs_2d[row][0])
            
    #     return sorted_pegs
    
    
