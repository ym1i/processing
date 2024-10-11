
    
def vox(x, y, z, w, h, d):
    beginShape(QUADS) 
    # FACE
    vertex(x,  y,  z + d)
    vertex(x + w,  y,  z + d)
    vertex(x + w,  y + h,  z + d)
    vertex(x, y + h,  z + d)  
    # RIGHT
    vertex(x + w,  y + h,  z + d)
    vertex(x + w,  y + h,  z)
    vertex(x + w,  y,  z)
    vertex(x + w, y,  z + d)
    # BACK
    vertex(x + w,  y + h,  z)
    vertex(x,  y + h,  z)
    vertex(x,  y ,  z)
    vertex(x + w, y,  z)
    # LEFT
    vertex(x,  y + h,  z)
    vertex(x,  y + h,  z + d)
    vertex(x,  y,  z + d)
    vertex(x, y,  z)
    # BOTTOM
    vertex(x,  y + h,  z)
    vertex(x + w,  y + h,  z)
    vertex(x + w,  y + h,  z + d)
    vertex(x, y + h,  z + d)
    # TOP
    vertex(x,  y,  z)
    vertex(x + w,  y,  z)
    vertex(x + w,  y,  z + d)
    vertex(x, y,  z + d)
    endShape()
