import itertools


def readData(day: int,
             star: int,
             text_converter=lambda x: x,
             line_converter=str.split,
             list_converter=lambda x: x):
    with open(f'data/{day:02}_{starToNr(star)}.txt') as f:
        return list_converter([line_converter(x) for x in str.split(text_converter(f.read()), sep='\n')])


def starToNr(star: int):
    if (star == -1):
        return 'test01'
    elif (star == -2):
        return 'test02'
    else:
        return f'{star:02}'


def empty_line_seperated_groups(data):
    return [list(group)
            for key, group
            in itertools.groupby(data, lambda x: not x)
            if not key]
