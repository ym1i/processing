

class Petal():
    
    def __init__(self, pos, rx, ry, colour):
        self.pos = pos
        self.rx = rx
        self.ry = ry
        self.colour = colour
        self.verts = []
        
        self.make_petal()
        
    
    def make_petal(self):
        n = 100
        nx_scale = self.rx * 0.5
        ny_scale = self.ry * 0.5
        noise_step = 0.002
        
        # ELLIPSE (https://rikeilabo.com/ellipse)
        for i in range(n):
            theta = map(i, 0, n-1, 0, TAU)
            x = self.pos.x + self.rx * cos(theta)
            y = self.pos.y + self.ry * sin(theta)
            nx = map(noise(x * noise_step, y * noise_step), 0, 1, -nx_scale, nx_scale)
            ny = map(noise(x * noise_step, y * noise_step), 0, 1, -ny_scale, ny_scale)
            self.verts.append(PVector(x + nx, y + ny))      
    
    
    def render(self):
        fill(self.colour)
        strokeWeight(1)
        beginShape()
        for v in self.verts:
            vertex(v.x, v.y)
        endShape()
