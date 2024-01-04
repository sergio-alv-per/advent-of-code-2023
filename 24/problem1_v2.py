from sys import stdin
import numpy as np

test_area_lb = 200000000000000
#test_area_lb = 7
test_area_ub = 400000000000000
#test_area_ub = 27
points = []
velocities = []

for line in (l.strip() for l in stdin):
    point, velocity = line.split(" @ ")
    point = np.array([int(x) for x in point.split(", ")[:-1]])
    velocity = np.array([int(x) for x in velocity.split(", ")[:-1]])
    points.append(point)
    velocities.append(velocity)


path_intersections = 0
for i, (p1, v1) in enumerate(zip(points, velocities)):
    for p2, v2 in zip(points[i+1:], velocities[i+1:]):
        A = np.array([v1, -v2]).transpose()
        B = p2 - p1
        
        try:
            intercept = np.linalg.solve(A, B)
        except np.linalg.LinAlgError:
            continue

        if intercept[0] < 0 or intercept[1] < 0:
            continue

        point = p1 + v1 * intercept[0]

        if test_area_lb <= point[0] <= test_area_ub and test_area_lb <= point[1] <= test_area_ub:
            path_intersections += 1

print(path_intersections)