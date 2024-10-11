from petal import Petal
from buds import Buds

class Flower():
    
    def __init__(self, plt):
        self.petals = []
        self.buds = []
        self.plt = plt
        self.colour = plt.random_color()
        r = red(self.colour)
        g = green(self.colour)
        b = blue(self.colour)
        self.colour = color(r, g, b, 150)
        
        self.make_petals()
        self.make_buds()
        
        
    def make_petals(self):
        pos = PVector(400, 200)
        rx = 200
        ry = 100
        self.petals.append(Petal(pos, rx, ry, self.colour))
        pos = PVector(600, 400)
        rx = 120
        ry = 220
        self.petals.append(Petal(pos, rx, ry, self.colour))
        pos = PVector(400, 600)
        rx = 220
        ry = 120
        self.petals.append(Petal(pos, rx, ry, self.colour))
        pos = PVector(200, 400)
        rx = 100
        ry = 200
        self.petals.append(Petal(pos, rx, ry, self.colour))
        
    
    def make_buds(self):
        pos = PVector(400, 400)
        r = 100
        colour = color(255, 255, 255)
        self.buds.append(Buds(pos, r, colour))
            
        
    def render(self):
        for bud in self.buds:
            bud.render()
        for petal in self.petals:
            petal.render()
        
       
        

        
