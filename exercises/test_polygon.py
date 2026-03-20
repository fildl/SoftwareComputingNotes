import math
from polygon import Polygon
from polygon import compute_polygon_properties
from polygon import compute_height

def is_close(a, b):
    return math.isclose(a, b, abs_tol=1e-6)

print("Testing compute_polygon_properties function.")

# side lenght of regular polygon inscribed within a circle shoule be 2*r*sin(180°/n)

# test triangle
pol = compute_polygon_properties(sides=3, radius=1)
assert pol.sides == 3
assert is_close(pol.side_length, math.sqrt(3))
assert is_close(pol.angle, 60.0)

pol = compute_polygon_properties(sides=3, radius=2)
assert pol.sides == 3
assert is_close(pol.side_length, 2*math.sqrt(3))
assert is_close(pol.angle, 60.0)

# test square
pol = compute_polygon_properties(sides=4, radius=1)
assert pol.sides == 4
assert is_close(pol.side_length, math.sqrt(2))
assert is_close(pol.angle, 90.0)

pol = compute_polygon_properties(sides=4, radius=2)
assert pol.sides == 4
assert is_close(pol.side_length, 2*math.sqrt(2))
assert is_close(pol.angle, 90.0)

# test hexagon
pol = compute_polygon_properties(sides=6, radius=1)
assert pol.sides == 6
assert is_close(pol.side_length, 1.0)
assert is_close(pol.angle, 120.0)

pol = compute_polygon_properties(sides=6, radius=10)
assert pol.sides == 6
assert is_close(pol.side_length, 10.0)
assert is_close(pol.angle, 120.0)

print("compute_polygon_properties function tests passed.")
print()

print("Testing compute_height function.")

# test triangle
pol = Polygon(sides=3, side_length=1, angle=60)
height = compute_height(pol)
assert is_close(height, math.sqrt(3)/2)

pol = Polygon(sides=3, side_length=2, angle=60)
height = compute_height(pol)
assert is_close(height, math.sqrt(3))

# test square
pol = Polygon(sides=4, side_length=1, angle=90)
height = compute_height(pol)
assert is_close(height, 1)

pol = Polygon(sides=4, side_length=2, angle=90)
height = compute_height(pol)
assert is_close(height, 2)

print("compute_height function tests passed.")
print()

print("All tests passed.")