
class TravelerHenon(object):
    
    def __init__(self, s, a, dim, colors, num_pal):
        self.x = random(0, 1)
        self.y = random(0, 1)
        self.d = sqrt(sq(self.x) + sq(self.y))
        self.offset_x = random(1)
        self.offset_y = random(1)
        self.s = s
        self.a = a
        self.dim = dim
        self.c = colors[int(num_pal * self.d) % num_pal]
        
        
    def draw(self):
        t = self.x * cos(self.a) - (self.y - sq(self.x)) * sin(self.a)
        self.y = self.x * sin(self.a) + (self.y - sq(self.x)) * cos(self.a)
        self.x = t
        fuzz_x = random(-0.004, 0.004)
        fuzz_y = random(-0.004, 0.004)
        px = fuzz_x + (self.x / self.s + self.offset_x) * self.dim
        py = fuzz_y + (self.y / self.s + self.offset_y) * self.dim
        
        if px > 0 and px < self.dim and py > 0 and py < self.dim:
            stroke(red(self.c), green(self.c), blue(self.c), 56)
            point((self.x / self.s + .5) * self.dim, (self.y / self.s + .5) * self.dim)
            
        
    def create_particle(self, colors, num_pal):
        self.x = random(0, 1)
        self.y = random(0, 1)
        self.d = sqrt(sq(self.x) + sq(self.y))
        self.out_of_bounds = 0
        idx = int(num_pal * self.d) % num_pal
        self.c = colors[idx]
        
    def update_params(self, a, s):
        self.a = a
        self.s = s
        
        
