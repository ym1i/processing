
class Palette():
    def __init__(self):
        self.colors = []
        self.white = color(255, 255, 255)
        self.black = color(0, 0, 0)
        self.grey = color(128, 128, 128)
        self.red = color(255, 0, 0)
        self.green = color(0, 255, 0)
        self.blue = color(0, 0, 255)
        
        self.atmosphere()
        
    def random_color(self):
        return self.colors[int(random(len(self.colors)))]
    
    def spider_king(self):
        self.colors = [color(242, 219, 188), color(230, 63, 71), color(237, 129, 126), color(1, 121, 156), color(0, 103, 73)]
        
    
    def mono(self):
        self.colors.extend([color(217, 63, 29), color(227, 147, 124), color(230, 204, 167)])
            
    
    def golid_colors(self):
        self.colors.extend([color(231, 94, 96), color(249, 190, 82), color(89,180,180), color(197,149,197)])
    
    
    def mantel_colors(self):
        self.colors.extend([color(216, 29, 3), color(16, 25, 157), color(28, 126, 79), color(246, 165, 2), 
                            color(239, 212, 191), color(226, 224, 239), color(5, 4, 0)])
        
    def ruby(self):
        self.colors = [color(203, 88, 84), color(103, 30, 28)]
        
    def atmosphere(self):
        self.colors = [color(77, 106, 152), color(54, 73, 105)]
    
