
class Cell():
    
    def __init__(self, x, y, z, w, h, d, strategy):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.d = d
        self.partitions = []
        self.strategy = strategy
        self.colors = []
        
    
    def set_colors(self, colors):
        self.colors = colors
    
    
    def render(self):
        for i, partition in enumerate(self.partitions):
            if self.strategy == 'single':
                fill(self.colors[0])
            elif self.strategy == 'random':
                fill(self.colors[i % len(self.colors)])
            elif self.strategy == 'main':
                if random(1) < 0.1:
                    fill(self.colors[int(random(len(self.colors)))])
                else:
                    fill(self.colors[0])
            stroke(0)
            strokeWeight(1)
            rectMode(CORNER)
            rect(partition.x, partition.y, partition.w, partition.h)
            
    def render_3D(self):
        for i, partition in enumerate(self.partitions):
            
            if partition.x + partition.w >= width / 2:
                rand_x = random(30)
            else:
                rand_x = 0 
                
            if partition.y + partition.h >= height / 2 or partition.y <= -height / 2:
                rand_y = random(30)
            else:
                rand_y = 0 
                
            if partition.z + partition.d >= width / 2:
                rand_z = random(30)
            else:
                rand_z = 0 
            
            beginShape(QUADS)
            # FACE
            if self.strategy == 'random':
                fill(self.colors[i % len(self.colors)])
            else:
                fill(self.colors[0])
            vertex(partition.x + rand_x, partition.y + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + partition.h + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + rand_x, partition.y + partition.h + rand_y, partition.z + partition.d + rand_z)
            
            # BOTTOM
            # fill(self.colors[0])
            vertex(partition.x + rand_x, partition.y + rand_y, partition.z + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + rand_y, partition.z + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + partition.h + rand_y, partition.z + rand_z)
            vertex(partition.x + rand_x, partition.y + partition.h + rand_y, partition.z + rand_z)
            
            # LEFT
            # fill(self.colors[0])
            vertex(partition.x + rand_x, partition.y + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + rand_x, partition.y + rand_y, partition.z + rand_z)
            vertex(partition.x + rand_x, partition.y + partition.h + rand_y, partition.z + rand_z)
            vertex(partition.x + rand_x, partition.y + partition.h + rand_y, partition.z + partition.d + rand_z)
            
            # RIGHT
            # fill(self.colors[0])
            vertex(partition.x + partition.w + rand_x, partition.y + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + rand_y, partition.z + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + partition.h + rand_y, partition.z + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + partition.h + rand_y, partition.z + partition.d + rand_z)
            
            # FACE
            # fill(self.colors[0])
            vertex(partition.x + rand_x, partition.y + partition.h + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + rand_x + partition.w, partition.y + partition.h + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + partition.h + rand_y, partition.z + rand_z)
            vertex(partition.x + rand_x, partition.y + partition.h + rand_y, partition.z + rand_z)
            
            # BACK
            # fill(self.colors[0])
            vertex(partition.x + rand_x, partition.y + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + rand_y, partition.z + partition.d + rand_z)
            vertex(partition.x + partition.w + rand_x, partition.y + rand_y, partition.z + rand_z)
            vertex(partition.x + rand_x, partition.y + rand_y, partition.z + rand_z)
            
            endShape()
            
