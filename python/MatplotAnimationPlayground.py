# create a starting tuple
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import base64


changes = [x for x in [(random.choice([-1, 0, 1]), random.choice([-1, 0, 1])) for _ in range(100)] if x != (0, 0)]
for i in range(len(changes)-1, 0, -1):
    if (changes[i-1][0] == -changes[i][0] and changes[i-1][1] == -changes[i][1]):
        del changes[i]

results = [x := (0, 0), *[x := (x[0]+change[0], x[1]+change[1]) for change in changes]]

fig, ax = plt.subplots()
lines = ax.plot([], [], color="red", alpha=0.5)
line = lines[0]


def update(num):
    x = [x[0] for x in results[0:num]]
    y = [x[1] for x in results[0:num]]

    line.set_data(x, y)
    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(min(y)-1, max(y)+1)


step_size = 1
frames = [*range(1, len(results), step_size)] + [len(results)]

anim = FuncAnimation(fig, update, frames=frames, interval=100, repeat=False)

plt.show()

anim.save("./Animations/Walk.gif")

print(results)
