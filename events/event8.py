def solve1():
    with open("input/input8.txt", "r") as fh:
        txt = fh.read()
    txt = txt.replace("|", "\n").splitlines()
    for i in range(len(txt)):
        txt[i] = txt[i].rstrip("| ").lstrip(" ").split(" ")
        txt[i] = list(map(len, txt[i]))
    counter = 0
    for i in range(0, len(txt), 2):
        for displ in txt[i+1]:
            if displ == 6 or displ == 5:
                continue
            if displ in txt[i]:
                counter += 1
    return counter


# Real displays
r0 = "abcefg"
r1 = "cf"
r2 = "acdeg"
r3 = "acdfg"
r4 = "bcdf"
r5 = "abdfg"
r6 = "abdefg"
r7 = "acf"
r8 = "abcdefg"
r9 = "abcdfg"


def solve2():
    with open("input/input8.txt", "r") as fh:
        txt = fh.read()
    count = 0
    txt = txt.replace("|", "\n").splitlines()
    for i in range(len(txt)):
        txt[i] = txt[i].rstrip("| ").lstrip(" ").split(" ")
    for i in range(0, len(txt), 2):
        line = txt[i]
        mystery = txt[i+1]
        numbers = [""]*10
        unknown_number = ""

        for sign in line:
            #finding "easy"
            if len(sign) == 2:
                numbers[1] = sign
            if len(sign) == 4:
                numbers[4] = sign
            if len(sign) == 3:
                numbers[7] = sign
            if len(sign) == 7:
                numbers[8] = sign
        # finding a
        a = numbers[7].replace(numbers[1], "")

        for sign in line:
            # finding c by 6-8 in 1
            if len(sign) == 6:
                un = numbers[8]
                for char in sign:
                    un = un.replace(char, "")
                if un in numbers[7]:
                    c = un
                    f = numbers[1].replace(c, "")
        #finding d6 and d5
        for sign in line:
            if len(sign) == 6 and len(sign.replace(c, "")) == 6:
                numbers[6] = sign
            if len(sign) == 5 and len(sign.replace(c, "")) == 5:
                numbers[5] = sign
        #finding e 6-5
        e = numbers[6]
        for i in numbers[5]:
            e = e.replace(i, "")
        #finding d9 and d0 and d2 and d3
        for sign in line:
            if len(sign) == 6 and len(sign.replace(e, "")) == 6:
                numbers[9] = sign
            elif len(sign) == 6 and not sameDisp(sign, numbers[6]):
                numbers[0] = sign
            elif len(sign) == 5 and not sameDisp(sign, numbers[5]):
                if len(sign.replace(e, "")) == 5:
                    numbers[3] = sign
                else:
                    numbers[2] = sign
        for num in mystery:
            for i in range(len(numbers)):
                dnum = numbers[i]
                if sameDisp(num, dnum):
                    unknown_number += str(i)
        count += int(unknown_number)
    return count

def sameDisp(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i not in str2:
            return False
    return True