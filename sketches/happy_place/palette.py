
class Palette(object):
    
    def __init__(self, max_pal):
        self.good_colors = []
        self.max_pal = max_pal
        self.num_pal = 0
        # self.take_colors(img_file)
        
   
    def some_color(self):
        return self.good_colors[int(random(self.num_pal))]
    
    
    def take_colors(self, img_file):
        img = loadImage(img_file)
        image(img, 0, 0)
        
        for x in range(img.width):
            for y in range(img.height):
                c = get(x, y)
                if c not in self.good_colors:
                    if self.num_pal < self.max_pal:
                        self.good_colors.append(c)
                        self.num_pal += 1
    
