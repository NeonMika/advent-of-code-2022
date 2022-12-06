# create a starting tuple
import random
import matplotlib.pyplot as plt
from celluloid import Camera


changes = [x for x in [(random.choice([-1, 0, 1]), random.choice([-1, 0, 1])) for _ in range(100)] if x != (0, 0)]
for i in range(len(changes)-1, 0, -1):
    if (changes[i-1][0] == -changes[i][0] and changes[i-1][1] == -changes[i][1]):
        del changes[i]

results = [x := (0, 0), *[x := (x[0]+change[0], x[1]+change[1]) for change in changes]]

fig, ax = plt.subplots()
camera = Camera(fig)

artists = []

for i in range(1, len(results)):
    x = [d[0] for d in results[0:i]]
    y = [d[1] for d in results[0:i]]

    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(min(y)-1, max(y)+1)

    ax.plot(x, y, color="red", alpha=0.5)
    camera.snap()

animation = camera.animate()

plt.show()

animation.save("./Animations/Walk.gif")
