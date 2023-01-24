from cell import Cell
from cell import Partition


class Section():
    
    def __init__(self, x, y, w, h, palette):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cells = []
        self.palette = palette
        
        
    def make_cells(self):
        n_cols = int(random(1, self.w / 50))
        n_rows = int(random(1, self.h / 50))
        cell_w = self.w / n_cols
        cell_h = self.h / n_rows
        
        for row in range(n_rows):
            for col in range(n_cols):
                self.cells.append(Cell(self.x + cell_w * col, self.y + cell_h * row, cell_w, cell_h))
                
        
    def make_partitions_v(self, n_split, palette):
        partitions = []
        offset = self.h / 10
        h = self.h
        y = self.y
        for i in range(n_split):
            if i == n_split - 1:
                _height = h
            else:
                _height = random(offset, h - offset)
            partitions.append(Section(self.x, y, self.w, _height, palette))
            y += _height
            h -= _height
            if h < offset and i != n_split - 1:
                partitions.append(Section(self.x, y, self.w, h, palette))
                break
        
        return partitions
   
   
    def make_partitions_h(self, n_split, palette):
        partitions = []
        offset = self.w / 10
        w = self.w
        x = self.x
        for i in range(n_split):
            if i == n_split - 1:
                _width = w
            else:
                _width = random(offset, w - offset)
            partitions.append(Section(x, self.y, _width, self.h, palette))
            x += _width
            w -= _width
            if w < offset and i != n_split - 1:
                partitions.append(Section(x, self.y, w, self.h, palette))
                break
        
        return partitions
    
    
    def split_cell(self):
        n_partitions = 0
        n_split = int(random(5))
        
        for i in range(n_split):
            if i == 0:
                if random(1) > 0.5:
                    w = 0
                    h = random(self.cells[0].h / 10, self.cells[0].h - self.cells[0].h / 10)
                else:
                    w = random(self.cells[0].w / 10, self.cells[0].w - self.cells[0].w / 10)
                    h = 0
                    
                for cell in self.cells:
                    if w == 0:
                        cell.partitions.append(Partition(cell.x, cell.y, cell.w, h))
                        cell.partitions.append(Partition(cell.x, cell.y + h, cell.w, cell.h - h))
                    else:
                        cell.partitions.append(Partition(cell.x, cell.y, w, cell.h))
                        cell.partitions.append(Partition(cell.x + w, cell.y, cell.w - w, cell.h))
                n_partitions += 2
                continue
            
            id = int(random(n_partitions))    # pick random partition in cell
            p = self.cells[0].partitions[id]
            if (i % 2) == 0:
                w = 0
                h = random(p.h / 10, p.h - p.h / 10)
            else:
                w = random(p.w / 10, p.w - p.w / 10)
                h = 0
            
            for cell in self.cells:
                p = cell.partitions[id]
                if w == 0:
                    cell.partitions.append(Partition(p.x, p.y, p.w, h))
                    cell.partitions.append(Partition(p.x, p.y + h, p.w, p.h - h))
                else:
                    cell.partitions.append(Partition(p.x, p.y, w, p.h))
                    cell.partitions.append(Partition(p.x + w, p.y, p.w - w, p.h))
            n_partitions += 2
        
        
    def render(self):
        # noFill()
        # stroke(255, 0, 0)
        # strokeWeight(10)
        noStroke()
        fill(self.palette.random_color())
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)    
    
    
    def pprint(self):
        for cell in self.cells:
            print '-' * 100
            print 'cell: (x:{}, y:{}, w:{}, h:{})'.format(cell.x, cell.y, cell.w, cell.h)
            print ' ' * 100
            for p in cell.partitions:
                print 'part: (x:{}, y:{}, w:{}, h:{})'.format(p.x, p.y, p.w, p.h)
        print '=' * 100
        print ' ' * 100
            
            
        
