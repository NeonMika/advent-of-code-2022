import re
import Helper


def str2ranges(str):
    l0, l1, r0, r1 = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", str)[0]
    return ((int(l0), int(l1)), (int(r0), int(r1)))


def fully_overlap(range_pair):
    left = range_pair[0]
    right = range_pair[1]
    return (left[0] >= right[0] and left[1] <= right[1]) or (right[0] >= left[0] and right[1] <= left[1])


def partly_overlap(range_pair):
    left = range_pair[0]
    right = range_pair[1]

    return len(set(range(left[0], left[1]+1)).intersection(set(range(right[0], right[1]+1)))) > 0


def star01(test):
    data = Helper.readData(
        day=4,
        star=-1 if test else 1,
        line_converter=str2ranges
    )
    c = sum(fully_overlap(x) for x in data)
    print("fully overlap:", c)


def star02(test):
    data = Helper.readData(
        day=4,
        star=-2 if test else 2,
        line_converter=str2ranges
    )
    c = sum(partly_overlap(x) for x in data)
    print("partly overlap:", c)


star01(True)
star01(False)
star02(True)
star02(False)
