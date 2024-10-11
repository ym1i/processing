from cell import Cell
from palette import Palette


class CellController():
    
    def __init__(self, dirs):
        self.cells = []
        self.dirs = dirs

        margin = 100
        self.border_top = 50
        self.border_bottom = height - margin
        self.border_left = 50
        self.border_right = width - margin
        self.count = 0
        
        
    def add_cell(self, _cell):
        self.cells.append(_cell)
        self.cur = _cell
        
    def new_cell(self, _prev):
        prev_i = self.dirs.index(_prev.dir)
        if prev_i == 0:
            # GO EAST
            x = _prev.part1.x + _prev.part1_w + 10
            y = _prev.part1.y
            w = _prev.part1_w * 2
            h = _prev.part1_h
            if x + w >= self.border_right + w * 0.5:
                noLoop()
                return False
        elif prev_i == 1:
            # GO SOUTH
            x = _prev.part2.x
            y = _prev.part2.y + _prev.part2_h + 10
            w = _prev.part2_w
            h = _prev.part2_h * 2
            if y + h >= self.border_bottom + h * 0.5:
                noLoop()
                return False
        elif prev_i == 2:
            # GO WEST 
            x = _prev.part2.x - _prev.part2_w * 2 - 10
            y = _prev.part2.y
            w = _prev.part2_w * 2
            h = _prev.part2_h
            if x <= self.border_left:
                noLoop()
                return False
        elif prev_i == 3:
            # GO NORTH 
            x = _prev.part1.x
            y = _prev.part1.y - _prev.part1_h * 2 - 10
            w = _prev.part1_w
            h = _prev.part1_h * 2
            if y <= self.border_top:
                noLoop()
                return False
        
        next = Cell(x, y, w, h, self.dirs[(prev_i + 1) % len(self.dirs)])
        self.add_cell(next)
        
        
    def update(self):
        if self.cur.dir == 'east':
            self.cur.go_east(self.border_right)
            self.border_top = self.cur.y + self.cur.h + 10
        elif self.cur.dir == 'west':
            self.cur.go_west(self.border_left)
            self.border_bottom = self.cur.y - self.cur.h - 10
        elif self.cur.dir == 'south':
            self.cur.go_south(self.border_bottom)
            self.border_right = self.cur.x - self.cur.w - 10
        elif self.cur.dir == 'north':
            self.cur.go_north(self.border_top)
            self.border_left = self.cur.x + self.cur.w + 10
        
        if self.cur.stop:
            self.new_cell(self.cur)
        
            
    def render(self):
        for c in self.cells:
            c.render()
