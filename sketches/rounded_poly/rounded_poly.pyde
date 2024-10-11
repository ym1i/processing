

def setup():
    size(800, 800)


def draw():
  background(220)
  strokeWeight(3)

  drawShape(width / 2, width / 2, width / 4)
  noLoop()


def drawShape(X, Y, R):
    vertices = []
    
    for i in range(10):
        a = map(i, 0, 9, 0, TAU)
        rad = random(0.5, 1) * R
        x = X + rad * cos(a)
        y = Y + rad * sin(a)
        
        vertices.append(PVector(x, y))
        
    rounded_poly(vertices, 9999)


def rounded_poly(points, radiusAll):
   
    radius = radiusAll
    n_points = len(points)
    p1 = points[n_points - 1]

    for i in range(n_points):
        p2 = points[i % n_points]
        p3 = points[(i + 1) % n_points]
    
        A = PVector(p1.x, p1.y)
        B = PVector(p2.x, p2.y)
        C = PVector(p3.x, p3.y)

        BA = A.sub(B)
        BC = C.sub(B)
    
        BAnorm = BA.copy().normalize() 
        BCnorm = BC.copy().normalize()
    
        sinA = -BAnorm.dot(BCnorm.copy().rotate(PI / 2))
        sinA90 = BAnorm.dot(BCnorm)
        angle = asin(sinA)

        radDirection = 1 
        drawDirection = False
        if sinA90 < 0: 
            if angle < 0:
                angle += PI
            else:
                angle += PI
                radDirection = -1
                drawDirection = True
        else: 
            if angle > 0:
                radDirection = -1
                drawDirection = true
            # angle > 0 ? ((radDirection = -1), (drawDirection = true)) : 0
        

        # accelDir = BAnorm.rotate(PI/2).copy().add(BCnorm)
        # radDirection = Math.sign(accelDir.dot(BCnorm.rotate(PI / 2)))
        # drawDirection = radDirection === -1

        # p2.radius ? (radius = p2.radius) : (radius = radiusAll)
        
    
        halfAngle = angle / 2
        lenOut = abs((cos(halfAngle) * radius) / sin(halfAngle))

        # Special part A
        if (lenOut > min(BA.mag() / 2, BC.mag() / 2)):
            lenOut = min(BA.mag() / 2, BC.mag() / 2)
            cRadius = abs((lenOut * sin(halfAngle)) / cos(halfAngle))
        else: 
            cRadius = radius
        

        x = B.x + BC.normalize().x * lenOut - BC.normalize().y * cRadius * radDirection
        y = B.y + BC.normalize().y * lenOut + BC.normalize().x * cRadius * radDirection

        arc(x, y, cRadius, BA.heading() + (PI / 2) * radDirection, BC.heading() - (PI / 2) * radDirection, drawDirection)

        p1 = p2
        p2 = p3
  
  
