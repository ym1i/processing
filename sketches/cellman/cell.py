from palette import Palette


class Cell():
    
    def __init__(self, x, y, w, h, dir):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.dir = dir
        self.stop = False
    
        self.plt = Palette()
        self.colors = []
        for i in range(10):
            self.colors.append(self.plt.random_color())
        self.fill_1 = self.colors[int(random(0, len(self.colors)))]
        self.fill_2 = self.colors[int(random(0, len(self.colors)))]
        
        self.split()
        
    def split(self):
        if self.dir == 'east' or self.dir == 'west':
            part1 = PVector(self.x, self.y)
            part2 = PVector(self.x + self.w * 0.5, self.y)
            part1_w = self.w * 0.5
            part2_w = self.w * 0.5
            part1_h = self.h
            part2_h = self.h
        elif self.dir == 'north' or self.dir == 'south':
            part1 = PVector(self.x, self.y)
            part2 = PVector(self.x, self.y + self.h * 0.5)
            part1_w = self.w
            part2_w = self.w
            part1_h = self.h * 0.5
            part2_h = self.h * 0.5
        connector1 = []
        connector2 = []
        n_connect = 5
        for i in range(n_connect):
            if self.dir == 'east' or self.dir == 'west':
                y = map(i, 0, n_connect - 1, self.y, self.y + self.h)
                x = self.x + self.w * 0.5
            elif self.dir == 'north' or self.dir == 'south':
                x = map(i, 0, n_connect - 1, self.x, self.x + self.w)
                y = self.y + self.h * 0.5
            connector1.append(PVector(x, y))
            connector2.append(PVector(x, y))
        
        self.part1 = part1
        self.part2 = part2
        self.part1_w = part1_w
        self.part2_w = part2_w
        self.part1_h = part1_h
        self.part2_h = part2_h
        self.connector1 = connector1
        self.connector2 = connector2
        
    
    def go_east(self, border):
        vel = PVector(6, 0)
        if self.part2.x > border:
            vel.mult(0)
            self.stop = True
        self.part2.add(vel)
        for v in self.connector2:
            v.add(vel)
    
    def go_south(self, border):
        vel = PVector(0, 6)
        if self.part2.y > border:
            vel.mult(0)
            self.stop = True
        self.part2.add(vel)
        for v in self.connector2:
            v.add(vel)
    
    def go_west(self, border):
        vel = PVector(-6, 0)
        if self.part1.x < border:
            vel.mult(0)
            self.stop = True
        self.part1.add(vel)
        for v in self.connector1:
            v.add(vel)
            
    def go_north(self, border):
        vel = PVector(0, -6)
        if self.part1.y < border:
            vel.mult(0)
            self.stop = True
        self.part1.add(vel)
        for v in self.connector1:
            v.add(vel)
        
    
    def render(self):
        fill(self.fill_1)
        rect(self.part1.x, self.part1.y, self.part1_w, self.part1_h)
        fill(self.fill_2)
        rect(self.part2.x, self.part2.y, self.part2_w, self.part2_h)
        
        self.render_connector()
    
    
    def render_connector(self):
        
        for i, v in enumerate(self.connector1):
            beginShape()
            fill(self.colors[i])
            if i == len(self.connector1) - 1:
                break
            vertex(self.connector1[i].x, self.connector1[i].y)
            vertex(self.connector2[i].x, self.connector2[i].y)
            vertex(self.connector2[i+1].x, self.connector2[i+1].y)
            vertex(self.connector1[i+1].x, self.connector1[i+1].y)
            endShape(CLOSE)









































        
