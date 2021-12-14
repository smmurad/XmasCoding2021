def getIndex(cave, caves):
    return caves.index(cave)

def isCapitalized(str):
    for c in str:
        if c.islower():
            return False
    return True

def isConnected(cave1, cave2):


def bfs(caves, connections, current_cave, current_path):
    remaining_caves = []

    for cave in caves:
        if cave not in current_path and isCapitalized(cave):
            remaining_caves.append()


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




def solve2():
    with open("input/input12.txt", "r") as fh:
        lines = fh.read().splitlines()