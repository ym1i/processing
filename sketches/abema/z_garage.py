 
    # ameba.py

    def mixed_grid_alt(self, n_cols, n_rows):
        pegs = []
        margin = 300
        grid_width = (width - margin) / (n_cols + 1)
        grid_height = (height - margin) / (n_rows + 1)
        r = grid_width * random(0.15, 0.3)
        n_scale = grid_width / 1
        resolution = 0.8
        
        big_peg = randint(0, 3)
        big_peg = 0
        if big_peg == 0:
            i = 2.5
            j = 1.5
            n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
            pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r * 3)) # BIG PEG
            
            i = n_rows
            for j in range(1, n_cols + 1):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            j = n_rows
            for i in reversed(range(1, n_rows)):
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))
            i = 1
            for j in reversed(range(1, n_rows)):
                if j == 1:
                    continue
                n = map(noise(i * resolution, j * resolution), 0, 1, -n_scale, n_scale)
                pegs.append(Peg((grid_width * i) + (margin / 2) + n, (grid_height * j) + (margin / 2) + n, r))

        return pegs
