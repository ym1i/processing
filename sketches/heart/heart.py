from circle import Circle


class Heart():
    
    def __init__(self, plt):
        self.plt = plt
        self.make_love()
        
    
    def make_love(self):
        # CIRCLE
        fill1 = self.plt.random_color()
        fill2 = self.plt.random_color()
        fill3 = self.plt.random_color()
        pos1 = PVector(400, 400)
        pos2 = PVector(600, 400)
        pos3 = PVector(200, 400)
        r = 100
        self.circle1 = Circle(pos1, r, fill1, self.plt)
        self.circle2 = Circle(pos2, r, fill2, self.plt)
        self.circle3 = Circle(pos3, r, fill3, self.plt)
        
        # SEMI CIRCLE
        vertices = []
        x = (self.circle1.pos.x + self.circle2.pos.x) * 0.5
        y = (self.circle1.pos.y + self.circle2.pos.y) * 0.5
        r = self.circle1.r * 2
        n = 100
        for i in range(n):
            a = map(i, 0, n, 0, PI)
            vertices.append(PVector(x + r * cos(a), y + r * sin(a)))
            
        # SPLIT CIRCLE1
        # self.circle1.split()
            
        self.vertices = vertices
        self.fill1 = fill1
        self.fill2 = fill2
        self.fill3 = fill3
                        
            
    def render(self):
        # noStroke()
            
        # SEMI CIRCLE LARGE
        self.render_circle(pivot=PVector(400, 400), r=300, start=TAU, stop=PI, fill_color=self.plt.random_color())
        self.render_circle(pivot=PVector(400, 400), r=300, start=PI, stop=0, fill_color=self.plt.random_color())
         
        
        # SEMI CIRCLE MID 
        self.render_circle(pivot=PVector(500, 400), r=200, start=PI, stop=0, fill_color=self.fill2)
        self.render_circle(pivot=PVector(300, 400), r=200, start=TAU, stop=PI, fill_color=self.fill3)
        
        # CIRCLES    
        self.circle1.render()
        self.circle2.render()
        self.circle3.render()
        # self.circle1.render_semi_circle()
        
        # STROKE
        # self.render_circle(pivot=PVector(400, 400), r=280, start=0, stop=PI, fill_color=self.fill3, no_fill=True, no_stroke=False)
        
        
        
    def render_circle(self, pivot, r, start, stop, fill_color, no_fill=False, no_stroke=True):
        if no_fill:
            noFill()
        else:
            fill(fill_color)
        if no_stroke:
            noStroke()
        else:
            strokeWeight(1)
            stroke(0)
        pivot = pivot
        r = r
        n = 100
        beginShape()
        for i in range(n):
            a = map(i, 0, n, start, stop)
            vertex(pivot.x + r * cos(a), pivot.y + r * sin(a))
        endShape()
        
        
        
