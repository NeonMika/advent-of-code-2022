import Helper


def star01(test):
    data = Helper.readData(
        day=1,
        star=-1 if test else 1,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: [sum(group) for group in Helper.empty_line_seperated_groups(lines)]
    )
    maximum = max(data)
    print('maximum:', maximum)


def star02(test):
    data = Helper.readData(
        day=1,
        star=-2 if test else 2,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: sorted([sum(group) for group in Helper.empty_line_seperated_groups(lines)], reverse=True)
    )
    sumTopThree = sum(data[0:3])
    print('sumTopThree:', sumTopThree)


star01(True)
star01(False)
star02(True)
star02(False)
