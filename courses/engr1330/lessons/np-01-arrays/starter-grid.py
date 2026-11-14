import numpy as np

grid = np.arange(10, 210, 10).reshape(4, 5)
print(grid.shape)
print(grid[0, 0])        # TODO: row 2, column 3 (counting from 0)
print(grid[0])           # TODO: the whole column with index 1
print(grid[0:2, 0:2])    # TODO: the bottom-right 2x2 block
print(grid)              # TODO: only values above 50
