def get_surrounding_fish(index):
    fish = []
    for yd in range(-1, 2):
        for xd in range(-1, 2):
            if yd == xd and yd == 0:
                continue
            new_fish = (index[0]+yd, index[1]+xd)
            if new_fish[0] < 0 or new_fish[0] > 9:
                continue
            if new_fish[1] < 0 or new_fish[1] > 9:
                continue
            fish.append(new_fish)
    return fish


def increase_and_propogate(index, grid):
    grid[index[0]][index[1]] += 1
    if grid[index[0]][index[1]] == 10:
        surrounding_fish = get_surrounding_fish(index)
        for fish in surrounding_fish:
            increase_and_propogate(fish, grid)


def solve1():
    with open("input/input11.txt", "r") as fh:
        txt = fh.read().splitlines()
    count = 0
    grid = [[0 for i in range(10)] for k in range(10)]
    for y in range(10):
        for x in range(10):
            grid[y][x] = int(txt[y][x])
    for steps in range(100):
        for y in range(10):
            for x in range(10):
                increase_and_propogate((y, x), grid)
        for y in range(10):
            for x in range(10):
                if grid[y][x] >= 10:
                    grid[y][x] = 0
                    count += 1
    return count


def solve2():
    with open("input/input11.txt", "r") as fh:
        txt = fh.read().splitlines()
    grid = [[0 for i in range(10)] for k in range(10)]
    for y in range(10):
        for x in range(10):
            grid[y][x] = int(txt[y][x])
    steps = 0
    while True:
        count = 0
        for y in range(10):
            for x in range(10):
                increase_and_propogate((y, x), grid)
        for y in range(10):
            for x in range(10):
                if grid[y][x] >= 10:
                    grid[y][x] = 0
                    count += 1
        if count == 100:
            return steps+1
        steps += 1
