import Helper
import numpy as np
import itertools as it
import re


def data(test) -> np.ndarray:
    return Helper.readData(
        day=8,
        test=test,
        line_converter=lambda line: [int(x) for x in re.findall(r"\d", line)],
        list_converter=lambda list: np.array(list),
    )


def star01(test):
    d = data(test)
    # number of rows in numpy array d

    north = np.full(d.shape, True)
    south = np.full(d.shape, True)
    for row in range(1, d.shape[0]):
        for col in range(d.shape[1]):
            north[row, col] = d[row, col] > max(d[:row, col])
            south[-row - 1, col] = d[-row - 1, col] > max(d[-row:, col])

    west = np.full(d.shape, True)
    east = np.full(d.shape, True)
    for col in range(1, d.shape[1]):
        for row in range(d.shape[0]):
            west[row, col] = d[row, col] > max(d[row, :col])
            east[row, -col - 1] = d[row, -col - 1] > max(d[row, -col:])

    # merge the boolean arrays into one
    merged = north | south | west | east
    s = np.sum(merged)
    print("seen:", s)


def star02(test):
    d = data(test)
    rows, cols = np.shape(d)

    def score(row: int, col: int) -> int:
        row = int(row)
        col = int(col)

        # create four lists north, south, west and east until value > d[row, col].
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        score = 1

        for down, right in dirs:
            r = row + down
            c = col + right
            dir_score = 0
            while r >= 0 and r < rows and c >= 0 and c < cols:
                dir_score += 1
                if d[r, c] >= d[row, col]:
                    break
                r += down
                c += right
            score *= dir_score

        return score

    # apply score to each element in d
    scores = np.fromfunction(np.vectorize(score), d.shape)
    print("max scenic score:", np.max(scores))


star01(True)
star01(False)
star02(True)
star02(False)
