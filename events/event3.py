def find_most_common(signal, pos):
    low_count = 0
    high_count = 0
    for line in signal:
        if line[pos] == "0":
            low_count += 1
        else:
            high_count += 1
    return 1 if high_count > low_count else 0


def get_element_with_most_common(signal, pos, least_common=False):
    low_count = 0
    low_elements = []
    high_count = 0
    high_elements = []
    for line in signal:
        if line[pos] == "0":
            low_count += 1
            low_elements.append(line)
        else:
            high_count += 1
            high_elements.append(line)
    if least_common:
        return high_elements if high_count < low_count else low_elements

    return high_elements if high_count >= low_count else low_elements


def solve1():
    with open("input/input3.txt", "r") as fh:
        signal = fh.read().splitlines()
    gamma = "0b"
    epsilon = "0b"
    for i in range(len(signal[0])):
        mcb = find_most_common(signal, i)
        gamma += str(mcb)
        epsilon += str(int(not mcb))

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def solve2():
    with open("input/input3.txt", "r") as fh:
        signal = fh.read().splitlines()

    # finding oxygen
    elements = signal
    ox_rat = "0b"
    c02_rat = "0b"
    for i in range(len(signal[0])):
        elements = get_element_with_most_common(elements, i)
        if len(elements) == 1:
            ox_rat += elements[0]
            break

    # finding C02
    elements = signal
    for i in range(len(signal[0])):
        elements = get_element_with_most_common(elements, i, least_common=True)
        if len(elements) == 1:
            c02_rat += elements[0]
            break
    return int(ox_rat, 2) * int(c02_rat, 2)
