
class Section():
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cells = []
            
        
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
    # def make_partitions_v(self, n_split, strategy, palette):
    #     partitions = []
    #     offset = self.h / 10
    #     h = self.h
    #     y = self.y
    #     for i in range(n_split):
    #         if i == n_split - 1:
    #             _height = h
    #         else:
    #             _height = random(offset, h - offset)
    #         partitions.append(Section(self.x, y, self.w, _height, strategy, palette))
    #         y += _height
    #         h -= _height
    #         if h < offset and i != n_split - 1:
    #             partitions.append(Section(self.x, y, self.w, h, strategy, palette))
    #             break
        
    #     return partitions
   
   
    # def make_partitions_h(self, n_split, strategy, palette):
    #     partitions = []
    #     offset = self.w / 10
    #     w = self.w
    #     x = self.x
    #     for i in range(n_split):
    #         if i == n_split - 1:
    #             _width = w
    #         else:
    #             _width = random(offset, w - offset)
    #         partitions.append(Section(x, self.y, _width, self.h, strategy, palette))
    #         x += _width
    #         w -= _width
    #         if w < offset and i != n_split - 1:
    #             partitions.append(Section(x, self.y, w, self.h, strategy, palette))
    #             break
        
    #     return partitions 
    
        
    # def make_cells(self):
    #     n_cols = int(random(1, self.w / 30))
    #     n_rows = int(random(1, self.h / 30))
    #     cell_w = self.w / n_cols
    #     cell_h = self.h / n_rows
        
    #     for row in range(n_rows):
    #         for col in range(n_cols):
    #             self.cells.append(Cell(self.x + cell_w * col, self.y + cell_h * row, cell_w, cell_h, self.color, self.palette, self, self.strategy))
                
    #     for cell in self.cells:
    #         cell.partitions.append(Partition(cell.x, cell.y, 0, cell.w, cell.h, self.color, self.palette, self, self.strategy))
        
    
    # def split_cell(self):
    #     n_partitions = 0
    #     n_split = int(random(5))
        
    #     for i in range(n_split):
    #         if i == 0:
    #             if random(1) > 0.5:
    #                 w = 0
    #                 h = random(self.cells[0].h / 10, self.cells[0].h - self.cells[0].h / 10)
    #             else:
    #                 w = random(self.cells[0].w / 10, self.cells[0].w - self.cells[0].w / 10)
    #                 h = 0
    #             z = random(10)
                    
    #             for cell in self.cells:
    #                 if w == 0:
    #                     cell.partitions.append(Partition(cell.x, cell.y, z, cell.w, h, self.color, self.palette, self, self.strategy))
    #                     cell.partitions.append(Partition(cell.x, cell.y + h, z, cell.w, cell.h - h, self.color, self.palette, self, self.strategy))
    #                 else:
    #                     cell.partitions.append(Partition(cell.x, cell.y, z, w, cell.h, self.color, self.palette, self, self.strategy))
    #                     cell.partitions.append(Partition(cell.x + w, cell.y, z, cell.w - w, cell.h, self.color, self.palette, self, self.strategy))
    #             n_partitions += 2
    #             continue
            
    #         id = int(random(n_partitions))    # pick random partition in cell
    #         p = self.cells[0].partitions[id]
    #         if (i % 2) == 0:
    #             w = 0
    #             h = random(p.h / 10, p.h - p.h / 10)
    #         else:
    #             w = random(p.w / 10, p.w - p.w / 10)
    #             h = 0
    #         z = random(10)
            
    #         for cell in self.cells:
    #             p = cell.partitions[id]
    #             # pop
    #             cell.partitions.pop(id)
    #             if w == 0:
    #                 cell.partitions.append(Partition(p.x, p.y, z, p.w, h, self.color, self.palette, self, self.strategy))
    #                 cell.partitions.append(Partition(p.x, p.y + h, z, p.w, p.h - h, self.color, self.palette, self, self.strategy))
    #             else:
    #                 cell.partitions.append(Partition(p.x, p.y, z, w, p.h, self.color, self.palette, self, self.strategy))
    #                 cell.partitions.append(Partition(p.x + w, p.y, z, p.w - w, p.h, self.color, self.palette, self, self.strategy))
    #         n_partitions += 1   
         
    #     colors = []
    #     for i in range(len(self.cells[0].partitions)):
    #         colors.append(self.palette.random_color())
            
    #     for cell in self.cells:
    #         cell.set_colors(colors)        
    
