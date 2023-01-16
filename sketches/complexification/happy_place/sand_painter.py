
class SandPainter(object):
    
    def __init__(self, c):
        self.c = c
        self.rad = random(PI)
        self.g = random(0.01, 0.1)
        
    
    def render(self, x, y, ox, oy):
        stroke(red(self.c), green(self.c), blue(self.c), 28)
        point(ox + (x - ox) * sin(self.rad), oy + (y - oy) * sin(self.rad))
        
        self.g += random(-0.050, 0.050)
        maxg = 0.22
        if self.g < -maxg:
            self.g = -maxg
        if self.g > maxg:
            self.g = maxg    
        w = self.g / 10
        
        for i in range(11):
            a = 0.1 - i / 110
            stroke(red(self.c), green(self.c), blue(self.c), 256 * a)
            point(ox + (x - ox) * sin(self.rad + sin(i * w)), oy + (y - oy) * sin(self.rad + sin(i * w)))
            point(ox + (x - ox) * sin(self.rad - sin(i * w)), oy + (y - oy) * sin(self.rad - sin(i * w)))
