def get_e_score(bracket):
    if bracket == ")":
        return 3
    if bracket == "]":
        return 57
    if bracket == "}":
        return 1197
    if bracket == ">":
        return 25137
    print("Invalid char given")
    return 0


def matching_end_bracket(start_bracket):
    if start_bracket == "(":
        return ")"
    if start_bracket == "[":
        return "]"
    if start_bracket == "{":
        return "}"
    if start_bracket == "<":
        return ">"


# returns false if error
def find_end_or_continue(line, b_to_match, pos):
    error = False
    if pos == len(line):
        return -1, False
    cur_b = line[pos]
    while cur_b in start_bracks:
        pos, error = find_end_or_continue(line, line[pos], pos+1)
        if error or pos == -1 or pos == len(line):
            return pos, error
        cur_b = line[pos]
    if line[pos] == matching_end_bracket(b_to_match):
        return pos + 1, False
    else:
        return pos, True


start_bracks = "([{<"
end_bracks = ")]}>"


def solve1():
    with open("input/input10.txt", "r") as fh:
        lines = fh.read().splitlines()
    it = 0
    error_score = 0
    for line in lines:
        pos, error = find_end_or_continue(line, line[0], 0)
        if error:
            error_score += get_e_score(line[pos])
        it += 1
    return error_score


def add_char(char, it):
    global to_add
    to_add[it].append(char)


def find_end_and_fix(line, b_to_match, pos, it):
    if pos == len(line):
        add_char(matching_end_bracket(b_to_match), it)
        return pos

    cur_b = line[pos]
    while cur_b in start_bracks:
        pos = find_end_and_fix(line, cur_b, pos+1, it)
        if pos == len(line):
            add_char(matching_end_bracket(b_to_match), it)
            return pos
        cur_b = line[pos]
    if line[pos] == matching_end_bracket(b_to_match):
        return pos + 1
    return pos


def get_cost(bracket):
    if bracket == ")":
        return 1
    if bracket == "]":
        return 2
    if bracket == "}":
        return 3
    if bracket == ">":
        return 4
    print("invalid char:", bracket)
    return 0


def get_full_cost(strs):
    tot_score = 0
    for c in strs:
        tot_score *= 5
        tot_score += get_cost(c)
    return tot_score


to_add = []


def solve2():
    with open("input/input10.txt", "r") as fh:
        lines = fh.read().splitlines()
    it = 0
    error_score = 0
    lines_to_remove = []
    for line in lines:
        pos, error = find_end_or_continue(line, line[0], 1)
        if error:
            error_score += get_e_score(line[pos])
            lines_to_remove.append(it)
        it += 1
    for i in reversed(lines_to_remove):
        lines.pop(i)
    it = 0
    global to_add
    to_add = [[] for i in range(len(lines))]
    for line in lines:
        pos = 0
        while pos != len(line):
            pos = find_end_and_fix(line, line[pos], pos+1, it)
        it += 1
    costs = []
    for strs in to_add:
        costs.append(get_full_cost(strs))
    costs.sort()
    return costs[int(len(costs)/2)]


