

class Cell():
    
    def __init__(self, x, y, w, h, partition_w, partition_h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sections = []
        self.partition_w = partition_w
        self.partition_h = partition_h
        
    
    def make_partitions(self):
        self.sections.append(InnerSection(self.x, self.y, self.partition_w, self.partition_h))
        self.sections.append(InnerSection(self.x, self.y + self.partition_h, self.partition_w, self.h - self.partition_h))
        self.sections.append(InnerSection(self.x + self.partition_w, self.y, self.w - self.partition_w, self.partition_h))
        self.sections.append(InnerSection(self.x + self.partition_w, self.y + self.partition_h, self.w - self.partition_w, self.h - self.partition_h))
    
        
    def render(self):
        # noStroke()
        # fill(self.palette.random_color())
        noFill()
        stroke(255, 0, 0)
        strokeWeight(3)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
        
    def render_sections(self):
        for section in self.sections:
            noFill()
            stroke(0)
            strokeWeight(2)
            rectMode(CORNER)
            rect(section.x, section.y, section.w, section.h)
            
            
class InnerSection():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = color(random(255), random(255), random(255))
        
    def render(self):
        noFill()
        stroke(0)
        strokeWeight(1)
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
