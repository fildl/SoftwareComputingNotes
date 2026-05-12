import math
from utilities import is_close
from polygon import Polygon
from polygon import compute_height

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