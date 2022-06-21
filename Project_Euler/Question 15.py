def lattice_paths(grid_size):
    grid = []
    for i in range(grid_size+1):
        grid.append([0] * (grid_size + 1))
    for i in range(grid_size):
        grid[grid_size][i] = 1
        grid[i][grid_size] = 1
    
    for i in range(grid_size-1, -1, -1):
        for ii in range(grid_size-1, -1, -1):
            grid[i][ii] = grid[i][ii+1] + grid[i+1][ii]
    return grid[0][0]

print(lattice_paths(40))