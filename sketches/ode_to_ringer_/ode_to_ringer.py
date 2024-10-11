from random import random, randint, shuffle
from peg import Peg
from element import Element
from zigzag import Zigzag
from block import Block
from wrapper import Wrapper


class OdeToRinger():
    
    def __init__(self, palette):
        self.pegs = []
        self.n_cols = 9
        self.n_rows = 9
        self.palette = palette
        
        self.grid_layout()
        self.create_element()
        
    
    def add_peg(self, x, y, r, style):
        self.pegs.append(Peg(x, y, r, style))
        
    
    def render(self):
        base_colors = [color(19, 222, 0), color(255,255,0), color(255, 0, 113), color(0, 149, 185)]
        
        self.base.render(no_fill=False, peg_fill=False, ribon=False, fill_color=base_colors[randint(0, 3)], peg_color=color(0, 0, 0))
        for i, item in enumerate(self.z):
            item.render(no_fill=False, peg_fill=True, ribon=False, fill_color=self.palette.random_color(), peg_color=self.palette.random_color())
        
        # for i in range(20):
        #     r = randint(0, len(self.z) - 1)
        #     self.z[r].render(no_fill=False, peg_fill=True, ribon=False, fill_color=self.palette.random_color(), peg_color=self.palette.random_color())
                
        # self.bloc.render(no_fill=False, peg_fill=True, ribon=False, fill_color=self.palette.random_color(), peg_color=self.palette.random_color())

    
    def grid_layout(self):
        grid_width = width / (self.n_cols + 1)
        grid_height = width / (self.n_rows + 1)
        r = grid_width * 0.5
        for j in range(1, self.n_rows + 1):                
            for i in range(1, self.n_cols + 1):
                self.add_peg(grid_width * i, grid_height * j, r, 'solid')
                
    
    def create_element(self):
        base_id = [i for i in range(len(self.pegs))]
        self.z = []
                
        self.base = Element(self.pegs, base_id, self.n_cols, self.n_rows, self.palette)
        self.base.wrap()
        
        for i in range(self.n_cols - 1):
            _zigzag = Zigzag(self.pegs, [], self.n_cols, self.n_rows, self.palette)
            _zigzag.wrap_2nn(1, 1, i, i + 1)
            self.z.append(_zigzag)
            
            _zigzag_v = Zigzag(self.pegs, [], self.n_cols, self.n_rows, self.palette)
            _zigzag_v.wrap_2nn_v(1, 1, i, i + 1)
            self.z.append(_zigzag_v)
            # bloc = Block(self.pegs, [], self.n_cols, self.n_rows, self.palette)
            # bloc.wrap(i, i + 2)
            # self.z.append(bloc)
            
        
        # self.bloc = Block(self.pegs, [], self.n_cols, self.n_rows, self.palette)
        # self.bloc.wrap(1, 3)
        # self.z.append(self.bloc)
        
    
    def pprint(self):
        pass
        
        
