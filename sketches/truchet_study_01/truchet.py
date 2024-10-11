from palette import Palette


class Truchet():
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sections = []
        self.connectors = []
        self.splitter = []
        self.palette = Palette()

        
    def split(self):
        r = self.w / 2
        n = 30
        v = PVector(self.x + r, self.y + self.h)
        for i in range(n):
            a = map(i, 0, n - 1, PI, 1.5 * PI)
            self.splitter.append(PVector(v.x + r * cos(a), v.y + r * sin(a)))
        u = PVector(self.x + r, self.y)
        for i in range(n):
            a = map(i, 0, n - 1, HALF_PI, 0)
            self.splitter.append(PVector(u.x + r * cos(a), u.y + r * sin(a)))
            
        part_1 = []
        part_2 = []
        self.offset_1 = PVector(-20, -20)
        self.offset_2 = PVector(20, 20)
        self.connector_2_3 = []
        
        for v in self.splitter:
            part_1.append(v.copy().add(self.offset_1))
            part_2.append(v.copy().add(self.offset_2))
            self.connector_2_3.append(v.copy().add(self.offset_1))
            self.connector_2_3.append(v.copy().add(self.offset_2))
            
        part_1.append(PVector(self.x, self.y).add(self.offset_1))
        part_1.append(PVector(self.x, self.y + self.h).add(self.offset_1))
        part_2.append(PVector(self.x + self.w, self.y + self.h).add(self.offset_2))
        part_2.append(PVector(self.x, self.y + self.h).add(self.offset_2))
        
        self.sections.append(part_1)
        self.sections.append(part_2)
        
    
    def __semi_circle(self, offset):
        self.semi_circle = []
        splitter = []
        connector = []
        part_1 = []
        part_2 = []
        r = self.w / 2
        padding = 80
        x = padding / sq(2)
        offset_2 = PVector(10, 10)
        n = 30
        v = PVector(self.x + r, self.y + self.h)
        v.add(offset)
        for i in range(n):
            a = map(i, 0, n - 1, PI, 1.5 * PI)
            splitter.append(PVector(v.x + (r - padding) * cos(a), v.y + (r - padding) * sin(a)))
            part_1.append(PVector(v.x + (r - padding) * cos(a), v.y + (r - padding) * sin(a)))
            # part_2.append(PVector(v.x + (r - padding) * cos(a), v.y + (r - padding) * sin(a)))
            part_2.append(splitter[i].copy().add(offset_2))
            connector.append(PVector(v.x + (r - padding) * cos(a), v.y + (r - padding) * sin(a)))
            connector.append(splitter[i].copy().add(offset_2))
        
        for i in range(n):
            a = map(i, 0, n - 1, 1.5 * PI, PI)
            part_1.append(PVector(v.x + (r - padding + (padding / 2)) * cos(a), v.y + (r - padding + (padding / 2)) * sin(a)))
            
        part_2.append(v.copy().add(offset_2)) 
        
        self.semi_circle.append(part_1)
        self.semi_circle.append(part_2)
        self.connectors.append(connector)
        
    
    def __trapezoid(self):
        self.trapezoid = []
        top = []
        splitter = []
        connector = []
        part_1 = []
        part_2 = []
        margin = 40
        offset = PVector(0, 10)
        start = 32
        stop = len(self.sections[1]) - 10
        for i in range(start, stop):
            x = self.sections[1][i].x
            y = self.sections[1][i].y + margin
            # self.trapezoid.append(PVector(x, y))
            top.append(PVector(x, y))
            splitter.append(PVector(x, y + 30))
            part_1.append(PVector(x, y + 30))
            part_2.append(PVector(x, y + 30).add(offset))
            connector.append(PVector(x, y + 30))
            connector.append(PVector(x, y + 30).add(offset))
        
        for v in reversed(top):
            part_1.append(v)
        
        part_2.append(PVector(part_2[-1].x, self.y + self.h + offset.y))
        part_2.append(PVector(part_2[0].x, self.y + self.h + offset.y))
            
        self.trapezoid.append(part_1)
        self.trapezoid.append(part_2)
        self.connectors.append(connector)
            
    
    def render(self):
        
        self.split()
        self.__trapezoid()
        self.__semi_circle(self.offset_2)
        # self.curve_splitter()
        # self.split_section(1, 15)
        # self.split_section(0, -15)
        
        for section in self.sections:
            fill(self.palette.random_color())
            beginShape()
            for v in section:
                vertex(v.x, v.y)
            endShape(CLOSE)
        
        beginShape(QUAD_STRIP)
        # fill(self.palette.random_color())
        for v in self.connector_2_3:
            fill(self.palette.random_color())
            vertex(v.x, v.y)
        endShape()
        
        for semi_circle in self.semi_circle:
            fill(self.palette.random_color())
            beginShape()
            for v in semi_circle:
                vertex(v.x, v.y)
            endShape(CLOSE)
            
        
        #TRAPEZOID
        for t in self.trapezoid:
            fill(self.palette.random_color())
            beginShape()
            for v in t:
                vertex(v.x, v.y)
            endShape(CLOSE)  
        
        # beginShape()
        # vertex(self.trapezoid[0].x, self.y + self.h + self.offset_2.y)
        # for v in self.trapezoid:
        #     fill(self.palette.random_color())
        #     # vertex(v.x, self.y + self.h)
        #     vertex(v.x, v.y)
        # vertex(self.trapezoid[-1].x, self.y + self.h + self.offset_2.y)
        # endShape(CLOSE)    
        
        for i, connector in enumerate(self.connectors):
            beginShape(QUAD_STRIP)
            fill(self.palette.random_color())
            # noFill()
            for v in connector:
                # fill(self.palette.random_color())
                vertex(v.x, v.y)
            endShape()
        self.render_stitch()            
        
    
    def render_stitch(self):
        for connector in self.connectors:
            beginShape(LINES)
            # stroke(self.palette.random_color())
            strokeWeight(2)
            for i, v in enumerate(connector):
                if i % 2 == 0:
                    # stroke(self.palette.random_color())
                    # strokeWeight(int(random(2, 5)))
                    next = connector[i + 1]
                    u = PVector.sub(next, v)
                    r1 = random(0.1, 0.5)
                    r2 = random(0.1, 0.5)
                    v1 = v.copy().sub(u.copy().mult(r1))
                    v2 = next.copy().add(u.copy().mult(r2))
                    vertex(v1.x, v1.y)
                    vertex(v2.x, v2.y)
            endShape()
    
    
    def split_section(self, section_i, offset):
        pivot = self.sections[section_i][-2]
        self.section_splitter = []
    
        for i, v in enumerate(self.splitter):
            u = PVector.sub(self.sections[section_i][i], pivot).mult(0.6)
            self.section_splitter.append(PVector.add(pivot, u))
            
        part_1 = []
        part_2 = []
        offset_1 = PVector(offset, offset)
        offset_2 = PVector(0, 0)
        connector = []
        
        for v in self.section_splitter:
            part_1.append(v.copy().add(offset_1))
            part_2.append(v.copy().add(offset_2))
            connector.append(v.copy().add(offset_1))
            connector.append(v.copy().add(offset_2))
        self.connectors.append(connector)
            
        part_1.append(self.sections[section_i][-2].copy().add(offset_1))
        part_1.append(self.section_splitter[0].copy().add(offset_1))
        part_2.append(self.sections[section_i][-3].copy().add(offset_2))
        
        for v in reversed(self.sections[section_i][:-2]):
            part_2.append(v)
        
        part_2.append(self.sections[section_i][-1].copy().add(offset_2))
        
        self.sections[section_i] = part_1
        self.sections.insert(section_i + 1, part_2)
    
    
    # def curve_splitter(self):
    #     n = 8
    #     self.curved_splitter = [[PVector() for i in range(n * 2)] for j in range(len(self.splitter))]
    #     offset_3 = self.offset_1.copy().mult(0.5)
    #     offset_4 = self.offset_2.copy().mult(0.5)
    #     for j, v in enumerate(self.splitter):
    #         v1 = v.copy().add(offset_3)
    #         v2 = v.copy().add(offset_4)
    #         start = PVector.sub(v1, v).heading()
    #         mid_1 = PVector.sub(v, v1).heading()
    #         mid_2 = PVector.sub(v, v2).heading()
    #         stop = PVector.sub(v2, v).heading()
    #         stop = stop - TAU if stop > mid_2 else stop
    #         r = 20
    #         # n = 10
    #         for i in range(n):
    #             a1 = map(i, 0, n - 1, start, mid_1)
    #             self.curved_splitter[j][i] = PVector(v1.x + r * cos(a1), v1.y + r * sin(a1))
    #         for i in range(n, n * 2):
    #             a2 = map(i, n, 2 * n - 1, mid_2, stop)
    #             self.curved_splitter[j][i] = PVector(v2.x + r * cos(a2), v2.y + r * sin(a2))
    
    
    # def render_curved_splitter(self):
    #     for j, _ in enumerate(self.curved_splitter):
    #         beginShape(QUAD_STRIP)
    #         fill(self.palette.random_color())
    #         noStroke()
    #         for i, v in enumerate(self.curved_splitter[j]):
    #             if j != len(self.curved_splitter) - 1:
    #                 vertex(self.curved_splitter[j][i].x, self.curved_splitter[j][i].y)
    #                 vertex(self.curved_splitter[j + 1][i].x, self.curved_splitter[j + 1][i].y)
    #         endShape()

        
