def solve1():
    with open("input/input2.txt", "r") as fh:
        cmds = fh.read().splitlines()

    d_x = 0
    d_y = 0
    for cmd in cmds:
        direction, val = cmd.split()
        val = int(val)
        if direction == "forward":
            d_x += val
        if direction == "down":
            d_y += val
        if direction == "up":
            d_y -= val

    return d_x * d_y

def solve2():
    with open("input/input2.txt", "r") as fh:
        cmds = fh.read().splitlines()

    d_x = 0
    d_y = 0
    aim = 0

    for cmd in cmds:
        dir, val = cmd.split()
        val = int(val)
        if dir == "forward":
            d_x += val
            d_y += val*aim
        if dir == "down":
            aim += val
        if dir == "up":
            aim -= val

    return d_x * d_y