from sand_painter import SandPainter


class Friend(object):
    
    def __init__(self, x, y, id, c):
        self.x = x
        self.y = y
        self.vx = random(1)
        self.vy = random(1)
        self.id = id
        self.c = c
        self.connections = []
        self.n_connections = 0
        self.max_connections = 10
        self.len_connections = 10 + int(random(50))
        self.sands = []
        self.n_sands = 3
        
        for i in range(self.n_sands):
            self.sands.append(SandPainter(self.c))
        
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.92
        self.vy *= 0.92
        
        
    def connect_to(self, friend):
        # Connect to Friend
        if self.n_connections < self.max_connections:
            if not self.friend_of(friend):
                # self.connections[self.n_connections] = friend
                self.connections.append(friend)
                self.n_connections += 1
        
        
    def friend_of(self, f):
        for i in range(self.n_connections):
            if self.connections[i] == f:
                return True
        return False
    
    
    def expose(self):
        for dx in range(-2, 3):
            a = 0.5 - abs(dx) / 5.0
            stroke(0, 256 * a)
            point(self.x + dx, self.y)
            stroke(255, 256 * a)
            point(self.x + dx - 1, self.y - 1)
        for dy in range(-2, 3):
            a = 0.5 - abs(dy) / 5.0
            stroke(0, 256 * a)
            point(self.x, self.y + dy)
            stroke(255, 256 * a)
            point(self.x - 1, self.y + dy - 1)
        
    
    def expose_connections(self, friends):
        # Draw connection lines to all friends
        for i in range(self.n_connections):
            friend_x = friends[self.connections[i]].x
            friend_y = friends[self.connections[i]].y
            
            for i in range(self.n_sands):
                self.sands[i].render(self.x, self.y, friend_x, friend_y)
                
    
    def render(self):
        for i in range(int(self.x - self.n_connections), int(self.x + self.n_connections)):
            for j in range(int(self.y - self.n_connections), int(self.y + self.n_connections)):
                stroke(self.c)
                point(i, j)
                
                
    def render_connections(self, friends):
        for i in range(n_connections):
            dx = friends[connections[i]].x - self.x
            dy = friends[connections[i]].y - self.y
            m = int(1 + sqrt(sq(dx) + sq(dy)) / 6)
            
            for j in range(m):
                t = (1 + cos(j * PI / m)) / 2
                px = int(self.x + t * dx)
                py = int(self.y + t * dy)
                stroke(0x333333)
                point(px, py)
                
                
    def find_happy_place(self, friends, n_friends):
        # Get closer to Friend, and further from strangers
        ax = 0
        ay = 0
        
        # find mean average of all friends and non-friends
        for i in range(n_friends):
            if friends[i] is not self:
                dx = friends[i].x - self.x
                dy = friends[i].y - self.y
                d = sqrt(sq(dx) + sq(dy))
                t = atan2(dx, dy)
                
                if i in self.connections:
                    # if friend then attract
                    if d > self.len_connections:
                        ax += 4 * cos(t)
                        ay += 4 * sin(t)
                else:
                    # if not friend then repulse
                    if d < self.len_connections:
                        ax += (self.len_connections - d) * cos(t + PI)
                        ay += (self.len_connections - d) * sin(t + PI)
                
        self.vx += ax
        self.vy += ay
                
                
                
                
                
                
                
                
                
