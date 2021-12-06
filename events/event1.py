
def solve1():
    with open("input/input1.txt", "r") as fh:
        txt = fh.read()
        measures = txt.splitlines()

    prev_dep = int(measures[0])
    num_inc = 0

    for m in measures[1:]:
        m = int(m)
        if prev_dep < m:
            num_inc += 1
        prev_dep = m

    return num_inc

def solve2():
    with open("input/input1.txt", "r") as fh:
        txt = fh.read()
        measures = txt.splitlines()

    windows = []
    d_1 = int(measures[1])
    d_2 = int(measures[0])
    # Create windows
    for m in measures[2:]:
        m = int(m)
        sum = m + d_1 + d_2
        windows.append(sum)
        d_2 = d_1
        d_1 = m
    prev_dep = int(windows[0])
    num_inc = 0
    for m in windows[1:]:
        m = int(m)
        if prev_dep < m:
            num_inc += 1
        prev_dep = m

    return num_inc




