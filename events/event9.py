def solve1():
    with open("input/input9.txt", "r") as fh:
        txt = fh.read().splitlines()
    grid = []
    for line in txt:
        grid.append([int(i) for i in line])
    size_x = len(grid[0])
    size_y = len(grid)
    count = 0
    for y in range(size_y):
        for x in range(size_x):
            if x == 0 or grid[y][x] < grid[y][x-1]:
                if x == size_x - 1 or grid[y][x] < grid[y][x + 1]:
                    if y == 0 or grid[y][x] < grid[y - 1][x]:
                        if y == size_y - 1 or grid[y][x] < grid[y + 1][x]:
                            count += grid[y][x]+1
    return count


def solve2():
    with open("input/input9.txt", "r") as fh:
        txt = fh.read().splitlines()
    grid = []
    for line in txt:
        grid.append([int(i) for i in line])
    size_x = len(grid[0])
    size_y = len(grid)
    danger_grid = [[0 for i in range(size_x)] for i in range(size_y)]
    bottoms = []
    count = 0
    for y in range(size_y):
        for x in range(size_x):
            if grid[y][x] == 9:
                danger_grid[y][x] = -1
                continue
            if x == 0 or grid[y][x] < grid[y][x-1]:
                if x == size_x - 1 or grid[y][x] < grid[y][x + 1]:
                    if y == 0 or grid[y][x] < grid[y - 1][x]:
                        if y == size_y - 1 or grid[y][x] < grid[y + 1][x]:
                            count += grid[y][x]+1
                            danger_grid[y][x] = 1
                            bottoms.append((y, x))
    it = 1
    for y in range(size_y):
        for x in range(size_x):
            if danger_grid[y][x] == 1:
                danger_grid[y][x] = it
                it += 1

    noChange = False
    while not noChange:
        noChange = True
        # for line in danger_grid:
        #     print(line)
        for y in range(size_y):
            for x in range(size_x):
                print((y, x))
                if danger_grid[y][x] != 0:
                    continue
                if x > 0:
                    if danger_grid[y][x-1] > 0:
                        noChange = False
                        danger_grid[y][x] = danger_grid[y][x-1]
                if y > 0:
                    if danger_grid[y-1][x] > 0:
                        noChange = False
                        danger_grid[y][x] = danger_grid[y-1][x]
                if x < size_x-1:
                    if danger_grid[y][x + 1] > 0:
                        noChange = False
                        danger_grid[y][x] = danger_grid[y][x +1]
                if y < size_y-1:
                    if danger_grid[y + 1][x] > 0:
                        noChange = False
                        danger_grid[y][x] = danger_grid[y + 1][x]

    max_val = max(list(map(max, danger_grid)))
    nums = {}
    for i in range(1, max_val+1):
        nums[i] = 0

    for y in range(size_y):
        for x in range(size_x):
            val = danger_grid[y][x]
            if val > 0:
                nums[val] += 1
    # print(nums)
    for line in danger_grid:
        print(line)
