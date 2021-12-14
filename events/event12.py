def getIndex(cave, caves):
    return caves.index(cave)


def isCapitalized(str):
    for c in str:
        if c.islower():
            return False
    return True


def isConnected(cave1, cave2, connections, caves):
    return connections[getIndex(cave1, caves)][getIndex(cave2, caves)]


def increasePaths():
    global num_paths
    num_paths += 1


def bfs(caves, connections, current_cave, current_path, allow_double_visit=False):
    possible_caves = []

    if current_cave == "end":
        increasePaths()
        return

    if allow_double_visit and \
            current_cave in current_path[:-1] and \
            not isCapitalized(current_cave) and\
            current_cave != "start":
        allow_double_visit = False

    for cave in caves:
        if cave == "start":
            continue
        if cave not in current_path or \
                isCapitalized(cave) or \
                allow_double_visit:
            if isConnected(current_cave, cave, connections, caves):
                possible_caves.append(cave)

    for cave in possible_caves:
        current_path.append(cave)
        bfs(caves, connections, cave, current_path, allow_double_visit)
        current_path.pop()


global num_paths


def solve1():
    with open("input/input12.txt", "r") as fh:
        lines = fh.read().splitlines()
    caves = []

    for connection in lines:
        for cave in connection.split("-"):
            if cave not in caves:
                caves.append(cave)
    connections = [[False for i in range(len(caves))] for k in range(len(caves))]
    for connection in lines:
        conn = connection.split("-")
        connections[getIndex(conn[0], caves)][getIndex(conn[1], caves)] = True
        connections[getIndex(conn[1], caves)][getIndex(conn[0], caves)] = True

    global num_paths
    num_paths = 0

    bfs(caves, connections, "start", ["start"])
    return num_paths


def solve2():
    with open("input/input12.txt", "r") as fh:
        lines = fh.read().splitlines()
    caves = []

    for connection in lines:
        for cave in connection.split("-"):
            if cave not in caves:
                caves.append(cave)
    connections = [[False for i in range(len(caves))] for k in range(len(caves))]
    for connection in lines:
        conn = connection.split("-")
        connections[getIndex(conn[0], caves)][getIndex(conn[1], caves)] = True
        connections[getIndex(conn[1], caves)][getIndex(conn[0], caves)] = True

    global num_paths
    num_paths = 0

    bfs(caves, connections, "start", ["start"], True)
    return num_paths