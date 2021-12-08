

def isVertical(line):
    start = line[0].split(",")
    end = line[1].split(",")
    return start[0] == end[0] and start[1] != end[1]


def isHorizontal(line):
    start = line[0].split(",")
    end = line[1].split(",")
    return start[0] != end[0] and start[1] == end[1]


def isDiagonal(line):
    start = line[0].split(",")
    end = line[1].split(",")
    return start[0] != end[0] and start[1] != end[1]


def solve1():
    with open("input/input5.txt", "r") as fh:
        txt = fh.read().splitlines()
    lines = []
    it = 0
    for i in txt:
        lines.append(txt[it].split(" -> "))
        it += 1
    start_xs = [int(lines[i][0].split(",")[0]) for i in range(len(lines))]
    start_ys = [int(lines[i][0].split(",")[1]) for i in range(len(lines))]
    end_xs = [int(lines[i][1].split(",")[0]) for i in range(len(lines))]
    end_ys = [int(lines[i][1].split(",")[1]) for i in range(len(lines))]
    min_x = min(start_xs + end_xs)
    max_x = max(start_xs + end_xs)
    min_y = min(start_ys + end_ys)
    max_y = max(start_ys + end_ys)
    grid = [[0 for i in range(min_x, max_x+100)] for j in range(min_y, max_y+100)] # the size was wrong for some reason??
    count = 0
    for line in lines:
        if isDiagonal(line):
            continue
            y_start = int(line[0].split(",")[1])
            y_end = int(line[1].split(",")[1])
            x_start = int(line[0].split(",")[0])
            x_end = int(line[1].split(",")[0])
            diff = abs(y_start-y_end)
            y_dir = 1 if y_start < y_end else -1
            x_dir = 1 if x_start < x_end else -1
            for x in range(diff+1):
                grid[y_start+(x*y_dir)][x_start+(x*x_dir)] += 1
                if grid[y_start+(x*y_dir)][x_start+(x*x_dir)] == 2:
                    count += 1

        if isHorizontal(line):
            y = int(line[0].split(",")[1])
            min_x = min(int(line[0].split(",")[0]), int(line[1].split(",")[0]))
            max_x = max(int(line[0].split(",")[0]), int(line[1].split(",")[0]))
            for i in range(min_x, max_x+1):
                grid[y][i] += 1
                if grid[y][i] == 2:
                    count += 1
        if isVertical(line):
            x = int(line[0].split(",")[0])
            min_y = min(int(line[0].split(",")[1]), int(line[1].split(",")[1]))
            max_y = max(int(line[0].split(",")[1]), int(line[1].split(",")[1]))
            for i in range(min_y, max_y+1):
                grid[i][x] += 1
                if grid[i][x] == 2:
                    count += 1

    return count



def solve2():
    with open("input/input5.txt", "r") as fh:
        txt = fh.read().splitlines()
    lines = []
    it = 0
    for i in txt:
        lines.append(txt[it].split(" -> "))
        it += 1
    start_xs = [int(lines[i][0].split(",")[0]) for i in range(len(lines))]
    start_ys = [int(lines[i][0].split(",")[1]) for i in range(len(lines))]
    end_xs = [int(lines[i][1].split(",")[0]) for i in range(len(lines))]
    end_ys = [int(lines[i][1].split(",")[1]) for i in range(len(lines))]
    min_x = min(start_xs + end_xs)
    max_x = max(start_xs + end_xs)
    min_y = min(start_ys + end_ys)
    max_y = max(start_ys + end_ys)
    grid = [[0 for i in range(min_x, max_x + 100)] for j in
            range(min_y, max_y + 100)]  # the size was wrong for some reason??
    count = 0
    for line in lines:
        if isDiagonal(line):
            y_start = int(line[0].split(",")[1])
            y_end = int(line[1].split(",")[1])
            x_start = int(line[0].split(",")[0])
            x_end = int(line[1].split(",")[0])
            diff = abs(y_start - y_end)
            y_dir = 1 if y_start < y_end else -1
            x_dir = 1 if x_start < x_end else -1
            for x in range(diff + 1):
                grid[y_start + (x * y_dir)][x_start + (x * x_dir)] += 1
                if grid[y_start + (x * y_dir)][x_start + (x * x_dir)] == 2:
                    count += 1

        if isHorizontal(line):
            y = int(line[0].split(",")[1])
            min_x = min(int(line[0].split(",")[0]), int(line[1].split(",")[0]))
            max_x = max(int(line[0].split(",")[0]), int(line[1].split(",")[0]))
            for i in range(min_x, max_x + 1):
                grid[y][i] += 1
                if grid[y][i] == 2:
                    count += 1
        if isVertical(line):
            x = int(line[0].split(",")[0])
            min_y = min(int(line[0].split(",")[1]), int(line[1].split(",")[1]))
            max_y = max(int(line[0].split(",")[1]), int(line[1].split(",")[1]))
            for i in range(min_y, max_y + 1):
                grid[i][x] += 1
                if grid[i][x] == 2:
                    count += 1

    return count