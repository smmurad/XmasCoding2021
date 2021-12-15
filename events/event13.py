def get_borders(coords):
    max_x = 0
    max_y = 0
    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]

    return max_x + 1, max_y + 1


def build_grid(coords, max_x, max_y):
    grid = [[False for x in range(max_x)] for y in range(max_y)]
    for coord in coords:
        grid[coord[1]][coord[0]] = True
    return grid


def split_and_int(el):
    ls = el.split(",")
    return list(map(int, ls))


def fold(grid, fold_pos, fold_axis, max_x, max_y):
    if fold_axis == "y":
        new_grid = grid[:int(fold_pos)]
        for y in range(1, max_y - fold_pos):
            for x in range(max_x):
                new_grid[fold_pos-y][x] = new_grid[fold_pos-y][x] or grid[fold_pos+y][x]

        return new_grid

    if fold_axis == "x":
        new_grid = [[False for x in range(fold_pos)] for y in range(max_y)]
        for y in range(max_y):
            for x in range(fold_pos):
                new_grid[y][x] = grid[y][x]

        for y in range(max_y):
            for x in range(1, max_x - fold_pos):
                new_grid[y][fold_pos-x] = new_grid[y][fold_pos-x] or grid[y][fold_pos+x]

        return new_grid

    print("No valid fold axis given:", fold_axis)
    return []


def solve1():
    with open("input/input13.txt", "r") as fh:
        lines = fh.read().split("\n\n")
    coords = lines[0].splitlines()
    coords = list(map(split_and_int, coords))
    folds = lines[1].splitlines()
    folds = list(map(lambda x: x.split()[2], folds))
    folds = list(map(lambda x: x.split("="), folds))
    max_x, max_y = get_borders(coords)
    grid = build_grid(coords, max_x, max_y)
    for f in folds:
        max_x = len(grid[0])
        max_y = len(grid)
        grid = fold(grid, int(f[1]), f[0], int(max_x), int(max_y))

        count = 0
        for line in grid:
            for e in line:
                if e:
                    count += 1
        return count


def solve2():
    with open("input/input13.txt", "r") as fh:
        lines = fh.read().split("\n\n")
    coords = lines[0].splitlines()
    coords = list(map(split_and_int, coords))
    folds = lines[1].splitlines()
    folds = list(map(lambda x: x.split()[2], folds))
    folds = list(map(lambda x: x.split("="), folds))
    max_x, max_y = get_borders(coords)
    grid = build_grid(coords, max_x, max_y)
    for f in folds:
        max_x = len(grid[0])
        max_y = len(grid)
        grid = fold(grid, int(f[1]), f[0], int(max_x), int(max_y))

    for line in grid:
        for e in line:
            if e:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    return ""
