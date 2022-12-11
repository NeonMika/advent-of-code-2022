import Helper
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import timeit
from celluloid import Camera


class Animated:
    def __init__(self, rope_length=2):
        self.fig = plt.figure(figsize=(20, 10))
        self.camera = Camera(self.fig)
        self.top_ax = self.fig.add_subplot(2, 2, 1)
        self.top_ax.invert_yaxis()
        self.top_heatmap_ax = self.fig.add_subplot(2, 2, 2)
        self.top_heatmap_ax.invert_yaxis()
        self.top_colorbar = None
        self.bottom_ax = self.fig.add_subplot(2, 2, 3)
        self.bottom_ax.invert_yaxis()
        self.bottom_heatmap_ax = self.fig.add_subplot(2, 2, 4)
        self.bottom_heatmap_ax.invert_yaxis()
        self.bottom_colorbar = None

        self.rope_length = rope_length
        self.x = []
        self.y = []

    def add(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def render(self):
        last_rope_x = self.x[-self.rope_length :]
        last_rope_y = self.y[-self.rope_length :]

        head_x = self.x[-self.rope_length :: -self.rope_length]
        head_y = self.y[-self.rope_length :: -self.rope_length]

        # top
        self.top_ax.plot(head_x, head_y, color="black")
        self.top_ax.plot(last_rope_x, last_rope_y, color="blue", linewidth=2)
        self.top_ax.scatter(x=last_rope_x, y=last_rope_y, color="blue")
        self.top_ax.scatter(x=head_x[0:1], y=head_y[0:1], color="red")

        # top heatmap

        min_x = int(min(self.x))
        max_x = int(max(self.x))
        min_y = int(min(self.y))
        max_y = int(max(self.y))

        heatmap = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=int)

        for r, c in zip(head_y, head_x):
            heatmap[r - min_y, c - min_x] = 1

        for r, c in zip(last_rope_y[1:], last_rope_x[1:]):
            heatmap[r - min_y, c - min_x] = 2

        heatmap[last_rope_y[0] - min_y, last_rope_x[0] - min_x] = 3

        # print(heatmap)

        cmap = colors.ListedColormap(["white", "black", "blue", "red"])

        mesh = self.top_heatmap_ax.pcolormesh(
            heatmap,
            cmap=cmap,
            vmin=0,
            vmax=3,  # interpolation="none"
        )

        if self.top_colorbar:
            self.top_colorbar.remove()
        self.top_colorbar = self.fig.colorbar(mesh)
        self.top_colorbar.set_ticks(
            ticks=[0, 1, 2, 3], labels=["empty", "head_trail", "tail", "head"]
        )

        # self.top_heatmap_ax.set_facecolor("white")
        # self.top_heatmap_ax.set_xticks([])
        # self.top_heatmap_ax.set_yticks([])
        self.top_heatmap_ax.axis("off")
        # self.top_heatmap_ax.get_xaxis().set_visible(False)
        # self.top_heatmap_ax.get_yaxis().set_visible(False)

        self.top_heatmap_ax.text(
            last_rope_x[0] - min_x + 0.5,
            last_rope_y[0] - min_y + 0.5,
            f"H",
            ha="center",
            va="center",
        )
        for idx, (x, y) in enumerate(zip(last_rope_x[1:], last_rope_y[1:])):
            self.top_heatmap_ax.text(
                x - min_x + 0.5,
                y - min_y + 0.5,
                f"T{idx+1}",
                ha="center",
                va="center",
            )

        # bottom
        self.bottom_ax.plot(last_rope_x, last_rope_y, color="blue", linewidth=2)
        self.bottom_ax.scatter(x=last_rope_x, y=last_rope_y, color="blue")
        self.bottom_ax.scatter(x=head_x[0:1], y=head_y[0:1], color="red")

        # bottom heatmap

        min_x = int(min(last_rope_x))
        max_x = int(max(last_rope_x))
        min_y = int(min(last_rope_y))
        max_y = int(max(last_rope_y))

        heatmap = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=int)

        for r, c in zip(last_rope_y[1:], last_rope_x[1:]):
            heatmap[r - min_y, c - min_x] = 1

        heatmap[last_rope_y[0] - min_y, last_rope_x[0] - min_x] = 2

        # print(heatmap)

        cmap = colors.ListedColormap(["white", "blue", "red"])

        mesh = self.bottom_heatmap_ax.pcolormesh(
            heatmap,
            cmap=cmap,
            vmin=0,
            vmax=2,
            # interpolation="none"
        )

        if self.bottom_colorbar:
            self.bottom_colorbar.remove()
        self.bottom_colorbar = self.fig.colorbar(mesh)
        self.bottom_colorbar.set_ticks([0, 1, 2], labels=["empty", "tail", "head"])

        # self.heatmap_ax.set_facecolor("white")
        # self.heatmap_ax.set_xticks([])
        # self.heatmap_ax.set_yticks([])
        self.bottom_heatmap_ax.axis("off")
        # self.heatmap_ax.get_xaxis().set_visible(False)
        # self.heatmap_ax.get_yaxis().set_visible(False)

        self.bottom_heatmap_ax.text(
            last_rope_x[0] - min_x + 0.5,
            last_rope_y[0] - min_y + 0.5,
            f"H",
            ha="center",
            va="center",
        )
        for idx, (x, y) in enumerate(zip(last_rope_x[1:], last_rope_y[1:])):
            self.bottom_heatmap_ax.text(
                x - min_x + 0.5,
                y - min_y + 0.5,
                f"T{idx+1}",
                ha="center",
                va="center",
            )

        self.camera.snap()

    def animate(self, *args, **kwargs):
        return self.camera.animate(*args, **kwargs)


def star01(test):
    data = Helper.readData(day=9, test=test)
    animation = Animated()

    rope = np.zeros((2, 2), dtype=int)

    trail = [tuple(rope[1])]

    animation.add(0, 0)
    animation.add(0, 0)
    animation.render()

    opNr = 0

    for i, d in enumerate(data):
        for i in range(int(d[1])):
            opNr += 1
            head_change = np.array((110, 110))
            if d[0] == "R":
                head_change = np.array((1, 0))
            elif d[0] == "L":
                head_change = np.array((-1, 0))
            elif d[0] == "U":
                head_change = np.array((0, -1))
            elif d[0] == "D":
                head_change = np.array((0, 1))
            rope[0] += head_change
            diff = rope[0] - rope[-1]
            max_abs_diff = np.max(np.absolute(diff))
            tail_move = np.sign(diff) if max_abs_diff > 1 else np.array([0, 0])
            rope[-1] += tail_move
            trail.append(tuple(rope[-1]))
            animation.add(rope[0, 0], rope[0, 1])
            animation.add(rope[-1, 0], rope[-1, 1])

            if opNr % (1 if test else 15) == 0:
                # print(100 * (i + 1) / len(data), "%")
                animation.render()

    print("covered cells:", len(set(trail)))

    animation.render()
    animation.animate(interval=500 if test else 10).save(
        f"./Animations/Day09_Star01{'test' if test else ''}.gif"
    )


def star02(test):
    data = Helper.readData(day=9, test=test, star=2)
    animation = Animated(10)

    rope = np.zeros((10, 2), dtype=int)

    trail = [tuple(rope[-1])]

    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)
    animation.add(0, 0)

    opNr = 0

    for i, d in enumerate(data):
        for i in range(int(d[1])):
            opNr += 1
            head_change = np.array((0, 0))
            if d[0] == "R":
                head_change = np.array((1, 0))
            elif d[0] == "L":
                head_change = np.array((-1, 0))
            elif d[0] == "U":
                head_change = np.array((0, -1))
            elif d[0] == "D":
                head_change = np.array((0, 1))

            rope[0] += head_change
            animation.add(rope[0, 0], rope[0, 1])

            for i in range(1, rope.shape[0]):
                diff = rope[i - 1] - rope[i]
                max_abs_diff = np.max(np.absolute(diff))
                move = np.sign(diff) if max_abs_diff > 1 else np.array([0, 0])
                rope[i] += move
                animation.add(rope[i, 0], rope[i, 1])
            trail.append(tuple(rope[-1]))

            if opNr % (1 if test else 15) == 0:
                # print(100 * (i + 1) / len(data), "%")
                animation.render()

    print("covered cells:", len(set(trail)))

    animation.render()
    animation.animate(interval=500 if test else 10).save(
        f"./Animations/Day09_Star02{'test' if test else ''}.gif"
    )


print()
print("|----------------------------------------|")
print("|--- Test 1 -----------------------------|")
print("|----------------------------------------|")
print()
print("test1 seconds:", timeit.timeit(lambda: star01(True), number=1))
print()
print("|----------------------------------------|")
print("|--- Star 1 -----------------------------|")
print("|----------------------------------------|")
print()
print("star2 seconds:", timeit.timeit(lambda: star01(False), number=1))
print()
print("|----------------------------------------|")
print("|--- Test 2 -----------------------------|")
print("|----------------------------------------|")
print()
print("test2 seconds:", timeit.timeit(lambda: star02(True), number=1))
print()
print("|----------------------------------------|")
print("|--- Star 2 -----------------------------|")
print("|----------------------------------------|")
print()
print("star2 seconds:", timeit.timeit(lambda: star02(False), number=1))
