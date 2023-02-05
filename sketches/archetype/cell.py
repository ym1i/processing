
class Cell():
    
    def __init__(self, x, y, w, h, strategy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
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
            beginShape(QUADS)
            
            # TOP
            if self.strategy == 'random':
                fill(self.colors[i % len(self.colors)])
            vertex(partition.x, partition.y, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y + partition.h, partition.z + partition.d)
            vertex(partition.x, partition.y + partition.h, partition.z + partition.d)
            
            # BOTTOM
            fill(0)
            vertex(partition.x, partition.y, partition.z)
            vertex(partition.x + partition.w, partition.y, partition.z)
            vertex(partition.x + partition.w, partition.y + partition.h, partition.z)
            vertex(partition.x, partition.y + partition.h, partition.z)
            
            # LEFT
            fill(self.colors[0])
            vertex(partition.x, partition.y, partition.z + partition.d)
            vertex(partition.x, partition.y, partition.z)
            vertex(partition.x, partition.y + partition.h, partition.z)
            vertex(partition.x, partition.y + partition.h, partition.z + partition.d)
            
            # RIGHT
            fill(0)
            vertex(partition.x + partition.w, partition.y, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y, partition.z)
            vertex(partition.x + partition.w, partition.y + partition.h, partition.z)
            vertex(partition.x + partition.w, partition.y + partition.h, partition.z + partition.d)
            
            # FACE
            fill(0)
            vertex(partition.x, partition.y + partition.h, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y + partition.h, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y + partition.h, partition.z)
            vertex(partition.x, partition.y + partition.h, partition.z)
            
            # BACK
            fill(0)
            vertex(partition.x, partition.y, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y, partition.z + partition.d)
            vertex(partition.x + partition.w, partition.y, partition.z)
            vertex(partition.x, partition.y, partition.z)
            
            endShape()
            
