import math
import turtle
screen_name = turtle.Screen()

def compute_figure(sides, radius):
    """
    Compute the side length and angle of a regular polygon given the number of sides and the radius of the circumscribed circle.
    """
    side_length = 2 * radius * math.sin(math.pi / sides)
    angle = (sides - 2) * 180 / sides
    return (sides, side_length, angle)

def draw_figure(figure_data, pos=(0, 0), color='black'):
    """
    Draw a regular polygon based on the computed figure data, position, and color.
    Arguments:
        - figure_data: A tuple containing the number of sides, side length, and angle of the polygon.
        - pos: A tuple representing the (x, y) position to start drawing the polygon.
        - color: A string representing the color of the polygon.
    """
    t = turtle.Turtle()
    t.color(color)
    t.up()
    t.setpos(pos[0], pos[1])
    t.down()

    for i in range(figure_data[0]):
        t.forward(figure_data[1])
        t.left(180 - figure_data[2])

def compute_height(figure_data):
    """
    Compute the height of the regular polygon based on the number of sides and side length.
    """
    if figure_data[0] % 2 == 0:
        return figure_data[1] / math.tan(math.pi / figure_data[0])
    else:
        return figure_data[1] / (2 * math.tan(math.pi / (2 * figure_data[0])))

def compute_center(figure_data):
    """
    Compute the center position of the regular polygon based on the number of sides and side length.
    """
    return (-figure_data[1] / 2, - compute_height(figure_data) / 2)

data = compute_figure(sides=10, radius=100)
draw_figure(figure_data=data, pos=compute_center(data), color='red')

screen_name.exitonclick()