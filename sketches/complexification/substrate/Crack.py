import SandPainter

class Crack(object):

    def __init__(self, dim_x, dim_y, crack_grid, make_crack):
        pprint('__init__()')
        self.x = 0
        self.y = 0
        self.t = 0
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.crack_grid = crack_grid
        self.sand_painter = SandPainter.SandPainter(512)
        self.make_crack = make_crack
        
        self.find_start()
        
        
    def find_start(self):
        pprint('find_start()')
        # pick random points
        x = 0
        y = 0
        
        # shift unyil crack is found
        found = False
        timeout = 0
        
        while not found or timeout > 1000:
            x = int(random(self.dim_x))
            y = int(random(self.dim_y))
            
            if self.crack_grid[y * self.dim_x + x] < 10000:
                found = True
                
        if found:
            # start crack
            a = self.crack_grid[y * self.dim_x + x]
            if random(100) < 50:
                a -= 90 + int(random(-2, 2.1))
            else:
                a += 90 + int(random(-2, 2.1))
                
            self.start_crack(x, y, a)
        else:
            print('timeout: ', timeout)
            
    def start_crack(self, x, y, t):
        pprint('start_crack()')
        self.x = x
        self.y = y
        self.t = t
        self.x += 0.61 * cos(t * PI / 180)
        self.y += 0.61 * sin(t * PI / 180)
        
    def move(self):
        pprint('move()')
        # continue cracking
        self.x += 0.42 * cos(self.t * PI / 180)
        self.y += 0.42 * sin(self.t * PI / 180)
        
        # bound check
        z = 0.33
        cx = int(self.x + random(-z, z))
        cy = int(self.y + random(-z, z))
        
        # draw sand painter
        self.region_color()
        
        # draw black crack
        stroke(0, 85)
        point(self.x + random(-z, z), self.y + random(-z, z))
        
        if cx >= 0 and cx < self.dim_x and cy >= 0 and cy < self.dim_y:
            # safe to check
            if self.crack_grid[cy * self.dim_x + cx] > 10000 or abs(self.crack_grid[cy * self.dim_x + cx] - self.t) < 5:
                self.crack_grid[cy * self.dim_x + cx] = int(self.t)
            elif abs(self.crack_grid[cy * self.dim_x + cx] - self.t) > 2:
                # crack encountered (not self), stop cracking
                self.find_start()
                self.make_crack()
            else:
                # out of bounds, stop cracking
                self.find_start()
                self.make_crack()
                
        
    def region_color(self):
        print('region_color()')
        # startchecking one step away
        rx = self.x
        ry = self.y
        open_space = True
        
        # find extents of open space
        while open_space:
            # move perpendicular to the crack
            rx += 0.81 * sin(self.t * PI / 180)
            ry += 0.81 * cos(self.t * PI / 180)
            cx = int(rx)
            cy = int(ry)
            if cx >= 0 and cx < self.dim_x and cy >= 0 and cy < self.dim_y:
                # safe to check
                if self.crack_grid[cy * self.dim_x + cx] > 10000:
                    pass
                else:
                    open_space = False
            else:
                open_space = False
        # draw sand painter
        self.sand_painter.render(rx, ry, self.x, self.y)
        
        
def pprint(arg):
    print '> {} | Crack.py'.format(arg)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
