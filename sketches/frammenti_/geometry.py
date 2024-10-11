

def square(x, y, w, h):
    vertices = []
    vertices.append(PVector(x, y))
    vertices.append(PVector(x + w, y))
    vertices.append(PVector(x + w, y + h))
    vertices.append(PVector(x, y + h))
    
    return vertices


def circle(center, r, n_vertices):
    vertices = []
    for i in range(n_vertices):
        a = map(i, 0, n_vertices, 0, TWO_PI)
        vertices.append(PVector(center.x + r * cos(a), center.y + r * sin(a)))
    
    return vertices


def triangle(center, r, rotation):
    vertices = []
    start = random(0, TWO_PI) if rotation else -HALF_PI
    end = start + TWO_PI
    for i in range(3):
        a = map(i, 0, 3, start, end)
        vertices.append(PVector(center.x + r * cos(a), center.y + r * sin(a)))
        
    return vertices


def pentagon(center, r, rotation):
    return polygon(center, r, rotation, 5)


def hexagon(center, r, rotation):
    return polygon(center, r, rotation, 6)

def heptagon(center, r, rotation):
    return polygon(center, r, rotation, 7)

def octagon(center, r, rotation):
    return polygon(center, r, rotation, 8)

def decagon(center, r, rotation):
    return polygon(center, r, rotation, 10)



def polygon(center, r, rotation, n):
    vertices = []
    start = random(0, TWO_PI) if rotation else -HALF_PI
    end = start + TWO_PI
    for i in range(n):
        a = map(i, 0, n, start, end)
        vertices.append(PVector(center.x + r * cos(a), center.y + r * sin(a)))
        
    return vertices
    
