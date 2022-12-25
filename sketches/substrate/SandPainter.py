
class SandPainter(object):
    
    def __init__(self, max_pal, img_file='okcomputer.jpg'):
        pprint('__init__()')
        
        self.g = random(0.01, 0.1)
        self.num_pal = 0
        self.max_pal = max_pal
        self.good_color = []
        self.take_color(img_file)
        self.c = self.some_color()
        
    def render(self, x, y, ox, oy):
        pprint('render()')
        # modulate gain
        self.g += random(-0.05, 0.05)
        max_g = 1.0
        if self.g < 0:
            self.g = 0
        if self.g > max_g:
            self.g = max_g
            
        # calculate granins by distance
        # grains = int(sqrt((ox - x) * (ox - x) + (oy - y) * (oy - y)))
        grains = 64
        
        # lay down grains of sand (transparent pixels)
        w = self.g / (grains - 1)
        for i in range(grains):
            a = 0.1 - i / grains * 10
            stroke(red(self.c), green(self.c), blue(self.c), a * 256)
            point(ox + (x - ox) * sin(sin(i * w)), oy + (y - oy) * sin(sin(i * w)))
            
    def some_color(self):
        return self.good_color[int(random(self.num_pal))]
    
    
    def take_color(self, img_file):
        pprint('take_color()')
        
        img = loadImage(img_file)
        image(img, 0, 0)
        
        for x in range(img.width):
            for y in range(img.height):
                c = get(x, y)
                exists = False
                for n in range(self.num_pal):
                    if c == self.good_color[n]:
                        exists = True
                        break
                if not exists:
                    if self.num_pal < self.max_pal:
                        self.good_color.append(c)
                        self.num_pal += 1  
            
            
def pprint(arg):
    print '> {} | SandPainter.py'.format(arg)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
