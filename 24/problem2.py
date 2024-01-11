from sys import stdin
from itertools import islice
import numpy as np

# Based on https://redd.it/18q40he

def get_rhs_lhs(x1, y1, dx1, dy1, x2, y2, dx2, dy2):
    return [dy2 - dy1, dx1 - dx2, y1 - y2, x2 - x1], x2 * dy2 - y2 * dx2 - x1 * dy1 + y1 * dx1

points_velocities = []

for line in islice((l.strip() for l in stdin), 5):
    point, velocity = line.split(" @ ")
    point = tuple(int(x) for x in point.split(", "))
    velocity = tuple(int(x) for x in velocity.split(", "))
    points_velocities.append((point, velocity))

mat_x_y = []
rhs_x_y = []

for (p1, v1), (p2, v2) in zip(points_velocities, points_velocities[1:]):
    lhs, rhs = get_rhs_lhs(p1[0], p1[1], v1[0], v1[1], p2[0], p2[1], v2[0], v2[1])
    mat_x_y.append(lhs)
    rhs_x_y.append(rhs)

mat_x_z = []
rhs_x_z = []
for (p1, v1), (p2, v2) in zip(points_velocities, points_velocities[1:]):
    lhs, rhs = get_rhs_lhs(p1[0], p1[2], v1[0], v1[2], p2[0], p2[2], v2[0], v2[2])
    mat_x_z.append(lhs)
    rhs_x_z.append(rhs)

mat_x_y = np.array(mat_x_y)
rhs_x_y = np.array(rhs_x_y)
mat_x_z = np.array(mat_x_z)
rhs_x_z = np.array(rhs_x_z)

(X, Y, _, _) = np.linalg.solve(mat_x_y, rhs_x_y)
(_, Z, _, _) = np.linalg.solve(mat_x_z, rhs_x_z)

print(round(X) + round(Y) + round(Z))
