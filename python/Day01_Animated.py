import Helper
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def star01(test):
    data = Helper.readData(
        day=1,
        star=-1 if test else 1,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: [sum(group) for group in Helper.empty_line_seperated_groups(lines)]
    )
    star01.maximum = 0

    fig = plt.figure()
    bar_ax = fig.add_subplot(3, 1, (1, 2))
    hist_ax = fig.add_subplot(3, 1, 3)

    def update(num):
        bar_ax.clear()
        x = range(0, num)
        y = data[0:num]
        bar_ax.bar(x=x, height=y, color="blue")

        star01.maximum = max(y)
        maximum_index = y.index(star01.maximum)
        bar_ax.bar(x=[maximum_index], height=[star01.maximum], color="red", alpha=1.0)

        hist_ax.clear()
        hist_ax.hist(y, bins=20)

    step_size = 1 if test else 3
    frames = [*range(1, len(data), step_size)] + [len(data)]

    anim = FuncAnimation(fig, update, frames=frames, interval=500 if test else 10, repeat=False)

    anim.save(f"./Animations/Day01_Star01{'test' if test else ''}.gif")

    print('maximum:', star01.maximum)


def star02(test):
    data = Helper.readData(
        day=1,
        star=-2 if test else 2,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: sorted([sum(group) for group in Helper.empty_line_seperated_groups(lines)], reverse=True)
    )
    star02.sumTopThree = 0

    fig = plt.figure()
    bar_ax = fig.add_subplot(3, 1, (1, 2))
    hist_ax = fig.add_subplot(3, 1, 3)

    def update(num):
        bar_ax.clear()
        x = range(0, num)
        y = data[0:num]
        bar_ax.bar(x=x, height=y, color="blue")

        maximum_heights = y[0:3]
        star02.sumTopThree = sum(maximum_heights)
        maximum_indices = [0, 1, 2]
        bar_ax.bar(x=maximum_indices, height=maximum_heights, color="red", alpha=1.0)

        hist_ax.clear()
        hist_ax.hist(y, bins=20)

    step_size = 3
    frames = [*range(1, len(data), step_size)] + [len(data)]

    anim = FuncAnimation(fig, update, frames=frames, interval=500 if test else 10, repeat=False)

    anim.save(f"./Animations/Day01_Star02{'test' if test else ''}.gif")

    print('sumTopThree:', star02.sumTopThree)


star01(True)
star01(False)
star02(True)
star02(False)
