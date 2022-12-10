import itertools
from typing import Callable


def readData(day: int,
             test: bool | None = None,
             star: int = 1,
             text_converter: Callable = lambda x: x,
             line_converter: Callable = str.split,
             list_converter: Callable = lambda x: x):
    try:
        with open(f'data/{day:02}_{starToNr(test, star)}.txt') as f:
            return list_converter([line_converter(x) for x in str.split(text_converter(f.read()), sep='\n')])
    except FileNotFoundError:
        return list_converter([])


def starToNr(test: bool | None, star: int):
    if (test):  # True
        return f'test{abs(star):02}'
    else:  # None or False
        if (star < 0):
            return f'test{abs(star):02}'
        else:
            return f'{star:02}'


def empty_line_seperated_groups(data):
    return [list(group)
            for key, group
            in itertools.groupby(data, lambda x: not x)
            if not key]
