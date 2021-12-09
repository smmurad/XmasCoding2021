import math

def getCost(lst, pos, cost_table, advanced_cost=False):
    tot_cost = 0
    for crab in lst:
        if advanced_cost:
            diff = abs(crab-pos)
            tot_cost += cost_table[diff]
        else:
            tot_cost += abs(crab-pos)
    return tot_cost


def get_min_cost(txt, advanced_cost=False, binary=False):
    left_crab = txt[0]
    right_crab = txt[-1]
    furthest_crab = max(txt)
    cost_table = []
    cost_table.append(0)
    for i in range(1, furthest_crab+1):
        cost_table.append(i + cost_table[i-1])

    crab_cost = []
    if not binary:
        for i in range(right_crab):
            crab_cost.append(getCost(txt, i, cost_table, advanced_cost=advanced_cost))
        return min(crab_cost)

    pos = int((right_crab + left_crab) / 2)
    cost = getCost(txt, pos, cost_table)
    cost1 = getCost(txt, pos + 1, cost_table)

    if cost > cost1:
        goUp = True
        goDown = False
    else:
        goUp = False
        goDown = True

    while True:
        if goUp:
            pos = math.ceil((left_crab + right_crab) / 2)
        if goDown:
            pos = math.floor((right_crab + left_crab) / 2)

        cost = getCost(txt, pos, cost_table, advanced_cost=advanced_cost)
        costR = getCost(txt, pos + 1, cost_table, advanced_cost=advanced_cost)
        costL = getCost(txt, pos - 1, cost_table, advanced_cost=advanced_cost)
        if cost < costR and cost < costL:
            return cost
        elif cost > costL:
            right_crab = pos
            goUp = False
            goDown = True
        else:
            left_crab = pos
            goUp = True
            goDown = False


def solve1():
    with open("input/input7.txt", "r") as fh:
        txt = fh.read().split(",")
    txt = list(map(int, txt))
    txt.sort()
    return get_min_cost(txt, binary=True)


def solve2():
    with open("input/input7.txt", "r") as fh:
        txt = fh.read().split(",")
    txt = list(map(int, txt))
    txt.sort()
    return get_min_cost(txt, binary=False, advanced_cost=True)