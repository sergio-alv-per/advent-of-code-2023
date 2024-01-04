from sys import stdin
import matplotlib.pyplot as plt
from math import dist


points = []
velocities = []

for line in (l.strip() for l in stdin):
    point, velocity = line.split(" @ ")
    point = tuple(int(x) for x in point.split(", ")[:-1])
    velocity = tuple(int(x) for x in velocity[:-1].split(", ")[:-1])
    points.append(point)
    velocities.append(velocity)


# normalize points and velocities
#max_norm = max(dist(p, (0, 0)) for p in points)
#points = [(p[0] / max_norm, p[1] / max_norm) for p in points]
#velocities = [(v[0] / dist(v, (0, 0)), v[1] / dist(v, (0, 0))) for v in velocities]

# small dots
plt.scatter(*zip(*points), s=1)
# arrows
plt.quiver(*zip(*points), *zip(*velocities))
plt.savefig("vis.png", dpi=1000)