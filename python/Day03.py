import Helper

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def star01(test):
    data = Helper.readData(
        day=3,
        star=-1 if test else 1,
        line_converter=lambda line: (line, line[0:(len(line)//2)], line[(len(line)//2):len(line)])
    )
    sum_of_priorities = 0
    for entry in data:
        sum_of_priorities += sum({LETTERS.index(ch)+1 for ch in entry[1] if ch in entry[2]})
    print("sum_of_priorities:", sum_of_priorities)


def star02(test):
    data = Helper.readData(
        day=3,
        star=-2 if test else 2,
        line_converter=lambda x: x,
        list_converter=lambda list: [list[i:i+3] for i in range(0, len(list), 3)]
    )
    sum_of_priorities = 0
    for entry in data:
        sum_of_priorities += sum({LETTERS.index(ch)+1 for ch in entry[0] if (ch in entry[1] and ch in entry[2])})
    print("sum_of_priorities:", sum_of_priorities)


star01(True)
star01(False)
star02(True)
star02(False)
