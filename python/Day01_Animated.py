import Helper
import matplotlib.pyplot as plt
from celluloid import Camera


class Animated:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 10))
        self.camera = Camera(self.fig)
        self.bar_ax = self.fig.add_subplot(6, 1, (1, 2))
        self.bar_sorted_ax = self.fig.add_subplot(6, 1, (3, 4))
        self.hist_ax = self.fig.add_subplot(6, 1, 5)
        self.box_ax = self.fig.add_subplot(6, 1, 6)

        self.x = []
        self.y = []
        self.highlights = []
        self.highlight_comments = []

    def add(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def add_highlight(self, y, comment):
        self.highlights.append(y)
        self.highlight_comments.append(comment)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_highlights(self, highlights, highlight_comments):
        self.highlights = highlights
        self.highlight_comments = highlight_comments

    def render(self):
        y_sorted = sorted(self.y, reverse=True)

        self.bar_ax.bar(x=self.x, height=self.y, color="blue")
        self.bar_ax.bar(x=[self.x[self.y.index(highlight)] for highlight in self.highlights], height=self.highlights, color="red", alpha=1.0)

        self.bar_sorted_ax.bar(x=self.x, height=y_sorted, color="blue")
        self.bar_sorted_ax.bar(x=[y_sorted.index(highlight) for highlight in self.highlights], height=self.highlights, color="red", alpha=1.0)

        self.hist_ax.hist(self.y, bins=20, color="green")

        self.box_ax.boxplot(
            self.y,
            patch_artist=True,
            vert=False,
            # boxprops=dict(facecolor='#1b9e77', color='#1b9e77'),
            # capprops=dict(color='#1b9e77'),
            # whiskerprops=dict(color='#1b9e77'),
            # flierprops=dict(color='#1b9e77', markeredgecolor='#1b9e77'),
            # medianprops=dict(color='#e41a1c')
        )
        self.box_ax.scatter(self.highlights, [1 for _ in self.highlights], marker='s', color='red')

        for i, highlight in enumerate(self.highlights):
            original_highlight_idx = self.y.index(highlight)
            sorted_highlight_idx = y_sorted.index(highlight)
            self.bar_ax.text(self.x[original_highlight_idx], highlight, self.highlight_comments[i])
            self.bar_sorted_ax.text(sorted_highlight_idx, highlight, self.highlight_comments[i])

            self.box_ax.axvline(x=highlight, ymin=0.5, ymax=0.75, color='red')
            self.box_ax.text(highlight, 1.1 + (0.1 * i), self.highlight_comments[i])

        self.camera.snap()

    def animate(self, *args, **kwargs): return self.camera.animate(*args, **kwargs)


def star01(test):
    data = Helper.readData(
        day=1,
        star=-1 if test else 1,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: [sum(group) for group in Helper.empty_line_seperated_groups(lines)]
    )
    animation = Animated()
    maximum = 0

    step_size = 1 if test else 3
    for frame in [*range(1, len(data), step_size)] + [len(data)]:
        x = range(0, frame)
        y = data[0:frame]
        animation.set_x(x)
        animation.set_y(y)

        maximum = max(y)
        animation.set_highlights([maximum], ["Maximum"])
        animation.render()

    animation.animate(interval=500 if test else 10).save(f"./Animations/Day01_Star01{'test' if test else ''}.gif")

    print('maximum:', maximum)


def star02(test):
    data = Helper.readData(
        day=1,
        star=-2 if test else 2,
        line_converter=lambda line: int(line) if line != '' else '',
        list_converter=lambda lines: [sum(group) for group in Helper.empty_line_seperated_groups(lines)]
    )
    animation = Animated()
    sumTopThree = 0

    step_size = 1 if test else 3
    for frame in [*range(3, len(data), step_size)] + [len(data)]:
        x = range(0, frame)
        y = data[0:frame]
        animation.set_x(x)
        animation.set_y(y)

        maximum_heights = sorted(y, reverse=True)[0:3]
        sumTopThree = sum(maximum_heights)
        animation.set_highlights(maximum_heights, ["1st", "2nd", "3rd"])
        animation.render()

    animation.animate(interval=500 if test else 10).save(f"./Animations/Day01_Star02{'test' if test else ''}.gif")

    print('sumTopThree:', sumTopThree)


star01(True)
star01(False)
star02(True)
star02(False)
