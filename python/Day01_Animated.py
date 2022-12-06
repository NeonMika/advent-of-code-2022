import Helper
import matplotlib.pyplot as plt
from celluloid import Camera


def star01(test):
    data = Helper.readData(
        day=1,
        star=-1 if test else 1,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: [sum(group) for group in Helper.empty_line_seperated_groups(lines)]
    )
    star01.maximum = 0

    fig = plt.figure(figsize=(10, 8))
    camera = Camera(fig)
    bar_ax = fig.add_subplot(4, 1, (1, 2))
    hist_ax = fig.add_subplot(4, 1, 3)
    box_ax = fig.add_subplot(4, 1, 4)

    step_size = 1 if test else 3
    for frame in [*range(1, len(data), step_size)] + [len(data)]:
        x = range(0, frame)
        y = data[0:frame]

        star01.maximum = max(y)
        maximum_index = y.index(star01.maximum)

        bar_ax.bar(x=x, height=y, color="blue")
        bar_ax.bar(x=[maximum_index], height=[star01.maximum], color="red", alpha=1.0)

        hist_ax.hist(y, bins=20, color="green")

        box_ax.boxplot(
            y,
            patch_artist=True,
            vert=False,
            # boxprops=dict(facecolor='#1b9e77', color='#1b9e77'),
            # capprops=dict(color='#1b9e77'),
            # whiskerprops=dict(color='#1b9e77'),
            # flierprops=dict(color='#1b9e77', markeredgecolor='#1b9e77'),
            # medianprops=dict(color='#e41a1c')
        )

        camera.snap()

    animation = camera.animate(interval=500 if test else 10)
    animation.save(f"./Animations/Day01_Star01{'test' if test else ''}.gif")

    print('maximum:', star01.maximum)


def star02(test):
    data = Helper.readData(
        day=1,
        star=-2 if test else 2,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: [sum(group) for group in Helper.empty_line_seperated_groups(lines)]
    )
    star02.sumTopThree = 0

    fig = plt.figure(figsize=(10, 8))
    camera = Camera(fig)
    bar_ax = fig.add_subplot(4, 1, (1, 2))
    hist_ax = fig.add_subplot(4, 1, 3)
    box_ax = fig.add_subplot(4, 1, 4)

    step_size = 1 if test else 3
    for frame in [*range(3, len(data), step_size)] + [len(data)]:

        x = range(0, frame)
        y = sorted(data[0:frame], reverse=True)

        maximum_heights = y[0:3]
        star02.sumTopThree = sum(maximum_heights)
        maximum_indices = [0, 1, 2]

        bar_ax.bar(x=x, height=y, color="blue")
        bar_ax.bar(x=maximum_indices, height=maximum_heights, color="red", alpha=1.0)

        hist_ax.hist(y, bins=20, color="green")

        box_ax.boxplot(
            y,
            patch_artist=True,
            vert=False,
            # boxprops=dict(facecolor='#1b9e77', color='#1b9e77'),
            # capprops=dict(color='#1b9e77'),
            # whiskerprops=dict(color='#1b9e77'),
            # flierprops=dict(color='#1b9e77', markeredgecolor='#1b9e77'),
            # medianprops=dict(color='#e41a1c')
        )

        camera.snap()

    animation = camera.animate(interval=500 if test else 10)
    animation.save(f"./Animations/Day01_Star02{'test' if test else ''}.gif")

    print('sumTopThree:', star02.sumTopThree)


star01(True)
star01(False)
star02(True)
star02(False)
