import Helper


def day01_star01(test):
    data = Helper.readData(
        day=1,
        star=-1 if test else 1,
        line_converter=lambda x: int(x) if x != '' else '',
        list_converter=lambda x: [sum(group) for group in Helper.empty_line_seperated_groups(x)]
    )
    maximum = max(data)
    print('maximum:', maximum)


def day01_star02(test):
    data = Helper.readData(
        day=1,
        star=-2 if test else 2,
        line_converter=lambda x: int(x) if x != '' else '',
        list_converter=lambda x: sorted([sum(group) for group in Helper.empty_line_seperated_groups(x)], reverse=True)
    )
    sumTopThree = sum(data[0:3])
    print('sumTopThree:', sumTopThree)


day01_star01(True)
day01_star01(False)
day01_star02(True)
day01_star02(False)
