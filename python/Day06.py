import Helper


def chunked(list, segment_length):
    return [list[i:i+segment_length] for i in range(0, len(list)-segment_length)]


def all_diff(list):
    return len(list) == len(set(list))


def star01(test):
    data = Helper.readData(
        day=6,
        star=-1 if test else 1,
        line_converter=lambda line: line,
        list_converter=lambda list: chunked(list[0], 4))

    first_all_diff = next(x for x in data if all_diff(x))
    index_of_first_all_diff = data.index(first_all_diff)
    print("index of first all diff:", index_of_first_all_diff)
    print("  +4:", index_of_first_all_diff + 4)


def star02(test):
    data = Helper.readData(
        day=6,
        star=-1 if test else 1,
        line_converter=lambda line: line,
        list_converter=lambda list: chunked(list[0], 14)
    )

    first_all_diff = next(x for x in data if all_diff(x))
    index_of_first_all_diff = data.index(first_all_diff)
    print("index of first all diff:", index_of_first_all_diff)
    print("  +14:", index_of_first_all_diff + 14)


star01(True)
star01(False)
star02(True)
star02(False)
