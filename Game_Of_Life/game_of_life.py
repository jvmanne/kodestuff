def next_generation(cells):
    row = len(cells)
    col = len(cells[0])
    next_cells = [[0 for x in range(col)] for y in range(row)]
    for x in range(row):
        for y in range(col):
            living_neighbours = -cells[x][y]
            for a in range(max(x - 1, 0), min(x + 2, row)):
                for b in range(max(y - 1, 0), min(y + 2, col)):
                    living_neighbours += cells[a][b]
            if living_neighbours == 3 or (living_neighbours == 2 and cells[x][y]):
                next_cells[x][y] = 1
    return next_cells

def print_cells(cells):
    for row in cells:
        for cell in row:
            print(cell, end=" ")
        print()
    print()

cells = [[0,0,0],[1,1,1],[0,0,0]]
print_cells(cells)
for x in range(4):
    cells = next_generation(cells)
    print_cells(cells)