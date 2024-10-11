

def grid_layout(width, height, n_cols, n_rows, margin):
    vertices = []
    grid_width = (width - margin) / (n_cols + 1)
    grid_height = (height - margin) / (n_rows + 1)
    
    for j in range(1, n_rows + 1):                
        for i in range(1, n_cols + 1):
            vertices.append(PVector((grid_width * i) + (margin / 2), (grid_height * j) + (margin / 2)))
            
    return vertices
