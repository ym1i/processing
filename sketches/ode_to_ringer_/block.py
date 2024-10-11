from peg import Peg
from wrapper import Wrapper


class Block(Wrapper):
    
    def __init__(self, pegs, id, n_cols, n_rows, palette):
        self.pegs = pegs
        self.element_id = id
        self.vertices = []
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.grid_length = width / (self.n_cols + 1)
        self.r = width / (self.n_cols + 1) / 2
        self.palette = palette
    
                                
    def wrap(self, start, stop):
        offset = self.grid_length / 2
        j = start
        for i in range(self.n_cols):
            id = j * self.n_cols + i
            if i % 2 == 0:
                x1 = i * self.grid_length + offset
                x2 = (i + 1) * self.grid_length + offset
                y1 = j * self.grid_length + offset
                y2 = (j + 1) * self.grid_length + offset
                self.element_id.append(id)
            else:
                x1 = i * self.grid_length + offset
                x2 = (i + 1) * self.grid_length + offset
                y1 = (j + 1) * self.grid_length + offset
                y2 = j * self.grid_length + offset
            self.vertices.append(PVector(x1, y1))
            self.vertices.append(PVector(x2, y1))
            self.vertices.append(PVector(x2, y2))
            
        for i in reversed(range(self.n_cols)):
            if i % 2 == 0:
                x1 = (i + 1) * self.grid_length + offset
                x2 = i * self.grid_length + offset
                y1 = (j + 2) * self.grid_length + offset
                y2 = (j + 3) * self.grid_length + offset
            else:
                x1 = (i + 1) * self.grid_length + offset
                x2 = i * self.grid_length + offset
                y1 = (j + 3) * self.grid_length + offset
                y2 = (j + 2) * self.grid_length + offset
            self.vertices.append(PVector(x1, y1))
            self.vertices.append(PVector(x2, y1))
            self.vertices.append(PVector(x2, y2))
                    
