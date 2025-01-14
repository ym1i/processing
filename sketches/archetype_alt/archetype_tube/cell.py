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
