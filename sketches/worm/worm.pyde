

def setup():
    size(800, 800)
    background(255)
    noLoop()
    init()
    
def draw():
    render()
    
def init():
    pass  
    
def render():
    vertices = []
    n = 1000
    nz_scale = 100
    resolution = 0.005 # 0.005-0.03
    for i in range(n):
        x = map(i, 0, n - 1, 300, 600)
        y = height / 2
        nz = map(noise(x * resolution, y * resolution), 0, 1, -nz_scale, nz_scale)
        vertices.append(PVector(x, y + nz))
        
    beginShape()
    for v in vertices:
        vertex(v.x, v.y)
    endShape()
        
    
