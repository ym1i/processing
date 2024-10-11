

class Peg():
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vec = PVector(x, y)

    
    def render(self, body_color):
        fill(body_color)
        strokeWeight(3)
        stroke(0)
        self.deformed_circle()
        # ellipse(self.x, self.y, self.r * 1.0, self.r * 1.0)
        
    
    def deformed_circle(self):
        scale = self.r / 2
        resolution = 0.002 * 2
        n_points = 100 / 4
        
        beginShape()
        for i in range(0, n_points):
            a = map(i, 0, n_points - 1, 0, TAU)
            x = self.x + self.r / 2 * cos(a)
            y = self.y + self.r / 2 * sin(a)
            n = map(noise(x * resolution, y * resolution), 0, 1, -scale, scale)
            curveVertex(x + n, y + n)
        endShape(CLOSE)
