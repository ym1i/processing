
class Palette():
    def __init__(self, n_colors=30):
        self.colors = []
        self.n_colors = n_colors
        
   
    def random_color(self):
        return self.colors[int(random(len(self.colors)))]
    
    
    def mantel_colors(self):
        self.colors = [color(216, 29, 3), color(16, 25, 157), color(28, 126, 79), color(246, 165, 2), color(239, 212, 191), color(226, 224, 239), color(5, 4, 0)]
