import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np

# Generate some random data
num_points = 100
data = np.random.random((num_points, 2))

# Create a figure and an axes
fig, ax = plt.subplots()
camera = Camera(fig)

for i in range(num_points):
    # Create a scatter plot with one point at each frame
    points = data[:i+1]
    artist = ax.scatter(points[:, 0], points[:, 1])
    camera.snap()

animation = camera.animate()
animation.save('animation.gif')
