
class Peg():
    
    def __init__(self, x, y, r, style, color_1, color_2):
        self.x = x
        self.y = y
        self.r = r
        self.style = style
        self.color_1 = color_1
        self.color_2 = color_2
    
            
    def render(self):
        fill(self.color_1)
        stroke(0)
        
        if self.style == 'solid':
            ellipse(self.x, self.y, self.r * 2, self.r * 2)
        elif self.style == 'bulls_1':
            self.bulls_eye(self.x, self.y, self.r, 2)
        elif self.style == 'bulls_2':
            self.bulls_eye(self.x, self.y, self.r, 3)
        elif self.style == 'bulls_3':
            self.bulls_eye(self.x, self.y, self.r, 4)
        elif self.style == 'recursive_2':
            self.recursive(2)
        elif self.style == 'recursive_3':
            self.recursive(3)
                    
                    
    def bulls_eye(self, x, y, r, n):
        for i in range(n):
            diameter = r * 2 * pow(0.6, i)
            if i % 2 == 0:
                fill(self.color_1)
                ellipse(x, y, diameter, diameter)
            else:
                fill(self.color_2)
                ellipse(x, y, diameter, diameter)
    
    def recursive(self, n):
        grid = self.r * 2 / n
        start_x = self.x - self.r
        start_y = self.y - self.r
        for j in range(n):
            for i in range(n):
                x = start_x + i * grid + grid / 2
                y = start_y + j * grid + grid / 2
                r = grid * 0.3
                rand = random(1)
                if rand < 0.7:
                    fill(self.color_1)
                    ellipse(x, y, r * 2, r * 2)
                elif rand < 0.8:
                    self.bulls_eye(x, y, r, 2)
                elif rand < 0.9:
                    self.bulls_eye(x, y, r, 3)
                else:
                    self.bulls_eye(x, y, r, 4)
