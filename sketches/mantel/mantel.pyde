# Mantel Ani | Manolo
# https://github.com/manoloide/AllSketchs/blob/master/2018/mantelAni/mantelAni.pde
# ---------------------------------------------------------------------------------------------


def setup():
    global colors, bg_color, points, det, des
    size(960, 540)
    
    seed = int(random(999999))
    noiseDetail(1)
    noiseSeed(seed)
    
    colors = [color(216, 29, 3), color(16, 25, 157), color(28, 126, 79), color(246, 165, 2), color(239, 212, 191), color(226, 224, 239), color(5, 4, 0)]
    bg_color = random_color()
    background(bg_color)
    strokeWeight(1)
    
    points = []
    des = random(1000000)
    det = random(0.01, 0.016) * 960    # (9.6, 15.36)
    
    # draw_background()
    # add_points()
    generate()


def draw():
    noLoop()
    

def generate():
    draw_background()
    add_points()
    draw_circles()
            
    noStroke()
    # for i in range(len(points)):
    #     p = points[i]
    #     fill(lerpColor(bg_color, color(0), random(0.05, 0.15)), 80)
    #     r = p.z * 0.5
    #     res = max(8, int(PI * r))
    #     da = TWO_PI / res
    #     beginShape()
    #     for j in range(res):
    #         ang = da * j
    #         sa = (ang + PI * 1.75) % TWO_PI
    #         sa = abs(sa - PI)
    #         if sa < HALF_PI:
    #             sa = HALF_PI
    #         rr = r * (1.2 - pow(abs(sin(sa)), 1.5) * 0.2)
    #         x = p.x + cos(ang) * rr
    #         y = p.y + sin(ang) * rr
    #         vertex(x, y)

    #     endShape(CLOSE)
    #     arc2(p.x, p.y, p.z, p.z * 1.5, 0, TAU, 0, 20, 20)


def draw_background():
    for i in range(1000):
        stroke(random_color(), 250)
        fill(random_color(), 240)
        x = width * random(-0.1, 1.1)
        y = height * random(-0.1, 1.1)
        
        beginShape()
        dis = int(width / 9.6)    #100
        for j in range(dis):
            nx = map(x, 0, width, 0, 1) * det    # (0, 15.36)
            ny = map(y, 0, height, 0, 1) * det
            ang = noise(des + nx, des + ny) * TWO_PI
            x += cos(ang)
            y += sin(ang)
            vertex(x, y)
        endShape(CLOSE)


def draw_circles():
    for p in points:
        col = random_color()
        fill(col)
        # ellipse(p.x, p.y, p.z, p.z)
        arc2(p.x, p.y, p.z, p.z*0.0, 0, TAU, 0, 5, 0)
        arc2(p.x, p.y, p.z, p.z*0.5, 0, TAU, 0, 20, 0)
        arc2(p.x+p.z*0.125, p.y-p.z*0.125, p.z*0.0, p.z*0.5, 0, TAU, 255, 20, 0)


def add_points():
    global points
    
    for i in range(1000):
        x = width * random(1)
        y = width * random(1)
        dis = dist(x, y, width/2, height/2)    # distance between (x, y) and center
        dis = dis / (width * 1.41)
        dis = map(dis, 0, 1, 2, 1)
        nx = map(x, 0, width, 0, 1) * det
        ny = map(y, 0, height, 0, 1) * det
        # s = width * random(0.1) * random(0.5, 1) * dis
        s = width * noise(des + nx, des + ny) * dis * random(0.05, 0.2)
        
        if s < 1:
            continue
        
        add = True
        # keep some distance between new point and existing points
        for j in range(len(points)):
            o = points[j]
            if dist(x, y, o.x, o.y) < (s + o.z) * 0.6:
                add = False
                break
        
        if add:
            points.append(PVector(x, y, s))
        

def arc2(x, y, s1, s2, a1, a2, col, shd1, shd2):
    radius1 = s1 * 0.5
    radius2 = s2 * 0.5
    amp = a2 - a1
    mapped_amp = map(amp, 0, TWO_PI, 0, 1)
    cc = max(1, int(max(radius1, radius2) * PI * mapped_amp))
    delta_ang = amp / cc 

    for i in range(cc):
        ang = a1 + delta_ang * i
        beginShape()
        fill(col, shd1)
        vertex(x + cos(ang) * radius1, y + sin(ang) * radius1)
        vertex(x + cos(ang + delta_ang) * radius1, y + sin(ang + delta_ang) * radius1)
        fill(col, shd2)
        vertex(x + cos(ang + delta_ang) * radius2, y + sin(ang + delta_ang) * radius2)
        vertex(x + cos(ang) * radius2, y + sin(ang) * radius2)
        endShape(CLOSE)
    
    
def random_color():
    return colors[int(random(len(colors)))]


def lerp_color(v):
    v = abs(v) % len(colors)
    c1 = colors[v]
    c2 = colors[v + 1]
    return lerpColor(c1, c2, v % 1)
    
