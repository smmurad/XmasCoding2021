def getFishesAfterDays(days, fish_state):
    fish_state = list(map(int, fish_state))
    cycle = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for d in fish_state:
        cycle[d] += 1
    for day in range(days):
        new_fishes = cycle[0]
        for i in range(len(cycle)-1):
            cycle[i] = cycle[i+1]
        cycle[8] = new_fishes
        cycle[6] += new_fishes

    fishes = 0
    for key, val in cycle.items():
        fishes += val

    return fishes


def solve1():
    with open("input/input6.txt", "r") as fh:
        fish_state = fh.read().split(",")
    return getFishesAfterDays(80, fish_state)


def solve2():
    with open("input/input6.txt", "r") as fh:
        fish_state = fh.read().split(",")
    return getFishesAfterDays(256, fish_state)




