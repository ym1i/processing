
class Section():
    
    def __init__(self, x, y, w, h, pl):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.palette = pl
        
        
    def render(self):
        noStroke()
        fill(self.palette.random_color())
        rectMode(CORNER)
        rect(self.x, self.y, self.w, self.h)
        
    
    def draw_circle(self):
        center = PVector(self.x + self.w/2, self.y + self.h/2)
        r = min(self.w, self.h)
        fill(self.palette.random_color())
        ellipse(center.x, center.y, r, r)
        
        self.rect_in_circle(center.x, center.y, r/2)
        
    def rect_in_circle(self, cx, cy, cr):
        fill(self.palette.random_color())
        rectMode(CENTER)
        rect(cx, cy, cr, cr)
        # beginShape()
        # vertex(cx, cy - cr)
        # vertex(cx + cr, cy)
        # vertex(cx, cy + cr)
        # vertex(cx - cr, cy)
        # endShape()
        
