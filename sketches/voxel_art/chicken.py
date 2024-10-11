from primitives import vox


class Chicken():
    def __init__(self, x, y, z, palette):
        self.x = x
        self.y = y
        self.z = z
        self.w = 300
        self.h = 500
        self.d = 300
        self.palette = palette
        
    
    def render(self):
        self.body()
        self.legs(self.x + self.w / 2, self.y + self.h, self.z + 0.5 * self.d, self.w / 7, self.h / 3, self.w / 7)
        
        
    def body(self):
        dx = self.w / 10
        dy = self.h / 10
        dd = self.d / 10
        fill(self.palette.white)
        noStroke()
        vox(self.x, self.y, self.z, self.w, self.h, self.d)
        vox(self.x + (2 * dx), self.y + (7 * dy), self.z + self.d, self.w, 2 * dy, 3 * dd) # wing
        vox(self.x + self.w, self.y + (6 * dy), self.z, 4 * dx, 4 * dy, self.d) # tail
        vox(self.x + self.w + (4 * dx), self.y + (6 * dy), self.z + dd, 2 * dx, 4 * dy, 6 * dd) # tail
        fill(self.palette.black)
        vox(self.x + (2 * dx), self.y + (2 * dx), self.z + self.d, dx, dx, 1) # eye
        
        
    def legs(self, x, y, z, w, h, d):
        dx = w / 10
        dy = h / 10
        dd = d / 10
        fill(self.palette.colors[1])
        vox(x, y, z + 1.5 * d, w, h, d)
        # vox(x - d, y + h, z - d, 3 * w, w, 3 * w)
        vox(x, y, z - 1.5 * d , w, h, d)
        # vox(x - d, y + h, z - (2 * d), 3 * w, w, 3 * w)
        
        
