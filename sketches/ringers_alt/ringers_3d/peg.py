
class Peg():
    
    def __init__(self, x, y, z, r, style, color_1, color_2):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.style = style
        self.color_1 = color_1
        self.color_2 = color_2
        

    def render(self):
        fill(self.color_1)
        noStroke()
        pushMatrix()
        translate(self.x, self.y, self.z)
        sphere(self.r)
        popMatrix()
    
                    
    def sphere(self):
        beginShape()
        
        for i in range(100):
            a1 = map(i, 0, 100, 0, PI)
            
            for j in range(100):
                a2 = map(j, 0, 100, 0, TWO_PI)
                x = self.x + cos(a2) * self.r * sin(a1)
                y = self.y + sin(a2) * self.r * sin(a1)
                z = self.z + cos(a1) * self.r
                vertex(x, y, z)
                    
        endShape(CLOSE)
