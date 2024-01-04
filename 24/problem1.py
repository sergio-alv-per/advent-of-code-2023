from sys import stdin
import numpy as np

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    

def rot_90(v):
    return Vector(-v.y, v.x)

def rot_minus_90(v):
    return Vector(v.y, -v.x)

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def intersection_is_within_bounds(p1, p2, v1, v2):
    A = np.array([[v1.x, -v2.x], [v1.y, -v2.y]])
    B = np.array([p2.x - p1.x, p2.y - p1.y])
    intercept = np.linalg.solve(A, B)
    point = p1 + v1 * intercept[0]
    
    if 200000000000000 <= point.x <= 400000000000000 and 200000000000000 <= point.y <= 400000000000000:
        return True
    else:
        return False

test_area_lb = 200000000000000
test_area_ub = 400000000000000
points = []
velocities = []

for line in (l.strip() for l in stdin):
    point, velocity = line.split(" @ ")
    point = Vector(*(int(x) for x in point.split(", ")[:-1]))
    velocity = Vector(*(int(x) for x in velocity[:-1].split(", ")[:-1]))
    points.append(point)
    velocities.append(velocity)


path_intersections = 0
for i, (p1, v1) in enumerate(zip(points, velocities)):
    for p2, v2 in zip(points[i+1:], velocities[i+1:]):
        v1_rot = rot_90(v1)
        p1p2 = Vector(p2.x - p1.x, p2.y - p1.y)

        if dot(v1_rot, p1p2) > 0:
            v1_rot = rot_minus_90(v1)
        
        p1p2_rot = rot_90(p1p2)
        if dot(p1p2_rot, v1_rot) < 0:
            p1p2_rot = rot_minus_90(v1)
        
        if dot(v1_rot, v2) > 0 and dot(p1p2_rot, v2) > 0:
            if intersection_is_within_bounds(p1, p2, v1, v2):
                path_intersections += 1

print(path_intersections)