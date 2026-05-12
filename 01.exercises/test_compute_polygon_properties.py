import math
from utilities import is_close
from polygon import Polygon
from polygon import compute_polygon_properties

print("Testing compute_polygon_properties function.")

# side lenght of regular polygon inscribed within a circle shoule be 2*r*sin(180°/n)

# test triangle
## radius 1

def test_triangle_sides():
    '''
    Test that the number of sides of the triangle is 3.
    '''
    pol = compute_polygon_properties(sides=3, radius=1)
    assert pol.sides == 3

def test_triangle_side_length():
    '''
    Test that the side lenght of the triangle is sqrt(3).
    '''
    pol = compute_polygon_properties(sides=3, radius=1)
    assert is_close(pol.side_length, math.sqrt(3))

def test_triangle_angle():
    '''
    Test that the angle of the triangle is 60 degrees.
    '''
    pol = compute_polygon_properties(sides=3, radius=1)
    assert is_close(pol.angle, 60.0)

## radius 2

def test_triangle_sides_radius_2():
    '''
    Test that the number of sides of the triangle is 3 when the radius is 2.
    '''
    pol = compute_polygon_properties(sides=3, radius=2)
    assert pol.sides == 3

def test_triangle_side_length_radius_2():
    '''
    Test that the side lenght of the triangle is sqrt(3) when the radius is 2.
    '''
    pol = compute_polygon_properties(sides=3, radius=2)
    assert is_close(pol.side_length, 2*math.sqrt(3))

def test_triangle_angle_radius_2():
    '''
    Test that the angle of the triangle is 60 degrees when the radius is 2.
    '''
    pol = compute_polygon_properties(sides=3, radius=1)
    assert is_close(pol.angle, 60.0)

# test square
## radius 1

def test_square_sides():
    '''
    Test that the number of sides of the square is 4.
    '''
    pol = compute_polygon_properties(sides=4, radius=1)
    assert pol.sides == 4

def test_square_side_length():
    '''
    Test that the side lenght of the square is sqrt(2).
    '''
    pol = compute_polygon_properties(sides=4, radius=1)
    assert is_close(pol.side_length, math.sqrt(2))

def test_square_angle():
    '''
    Test that the angle of the square is 90 degrees.
    '''
    pol = compute_polygon_properties(sides=4, radius=1)
    assert is_close(pol.angle, 90.0)

## radius 2

def test_square_sides_radius_2():
    '''
    Test that the number of sides of the square is 4 when the radius is 2.
    '''
    pol = compute_polygon_properties(sides=4, radius=2)
    assert pol.sides == 4

def test_square_side_length_radius_2():
    '''
    Test that the side lenght of the square is sqrt(2) when the radius is 2.
    '''
    pol = compute_polygon_properties(sides=4, radius=2)
    assert is_close(pol.side_length, 2*math.sqrt(2))

def test_square_angle_radius_2():
    '''
    Test that the angle of the square is 90 degrees when the radius is 2.
    '''
    pol = compute_polygon_properties(sides=4, radius=2)
    assert is_close(pol.angle, 90.0)

# test hexagon
## radius 1

def test_hexagon_sides():
    '''
    Test that the number of sides of the hexagon is 6.
    '''
    pol = compute_polygon_properties(sides=6, radius=1)
    assert pol.sides == 6

def test_hexagon_side_length():
    '''
    Test that the side lenght of the hexagon is 1.
    '''
    pol = compute_polygon_properties(sides=6, radius=1)
    assert is_close(pol.side_length, 1.0)

def test_hexagon_angle():
    '''
    Test that the angle of the hexagon is 120 degrees.
    '''
    pol = compute_polygon_properties(sides=6, radius=1)
    assert is_close(pol.angle, 120.0)

## radius 10

def test_hexagon_sides_radius_5():
    '''
    Test that the number of sides of the hexagon is 6 when the radius is 5.
    '''
    pol = compute_polygon_properties(sides=6, radius=5)
    assert pol.sides == 6

def test_hexagon_side_lengt_radius_5():
    '''
    Test that the side lenght of the hexagon is 5 when the radius is 5.
    '''
    pol = compute_polygon_properties(sides=6, radius=5)
    assert is_close(pol.side_length, 5.0)

def test_hexagon_angle_():
    '''
    Test that the angle of the hexagon is 120 degrees.
    '''
    pol = compute_polygon_properties(sides=6, radius=1)
    assert is_close(pol.angle, 120.0)

#assert is_close(pol.angle, 120.0)

print("compute_polygon_properties function tests passed.")