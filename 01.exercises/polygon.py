import math
import turtle
from dataclasses import dataclass

@dataclass
class Polygon:
    """
    A class to store properties of a regular polygon,
    including the number of sides, side length, and interior angle.
    """
    sides: int
    side_length: float
    angle: float

    def draw(self,
             pos,
             initial_angle=0,
             color='black'
            ) -> None:
        """
        Draw a regular polygon.
        
        Draw a regular polygon based on the computed figure data, that includes the number of sides,
        side length, and angle.
        The polygon is drawn starting at the specified position and using the specified color.
        
        Parameters:
        -------
        data: Polygon
            A Polygon object containing the number of sides, side length, and angle of the polygon.
            This object can be obtained from the compute_polygon_properties function.
        pos: tuple
            A tuple representing the (x, y) position to start drawing the polygon. Default is (0, 0).
        initial_angle: float
            The initial angle (in degrees) to start drawing the polygon. Default is 0.
        color: str
            A string representing the color of the polygon. Default is 'black'.

        Returns
        -------
        None

        """
        t = turtle.Turtle()
        t.hideturtle() # Hide the turtle cursor
        t.color(color)
        t.up()
        t.setpos(pos[0], pos[1])
        t.down()
        t.left(initial_angle)

        for _ in range(self.sides):
            t.forward(self.side_length)
            t.left(180 - self.angle)

    def compute_center(self
                      ) -> tuple:
        """
        Compute the center position of the regular polygon based on the number of sides and side length.

        This function can be used to calculate the position of the center of the regular polygon,
        allowing to draw the polygon in the center of the canvas.

        Parameters:
        -------
        data: Polygon
            A Polygon object containing the number of sides, side length, and angle of the polygon.
            This object can be obtained from the compute_polygon_properties function.

        Returns
        -------
        tuple
            A tuple (float, float) representing the (x, y) position of the center of the regular polygon.
        """
        return (-self.side_length / 2, - self.compute_height() / 2)
    
    def compute_height(self
                      ) -> float:
        """
        Compute the height of the regular polygon based on the number of sides and side length.

        The height is calculated differently for even and odd number of sides:
        - For even number of sides, the height is given by the formula:
            height = side_length / tan(pi / number_of_sides)
        - For odd number of sides, the height can be approximated by the formula:
            height = side_length / (2 * tan(pi / (2 * number_of_sides)))

        Parameters:
        -------
        data: Polygon
            A Polygon object containing the number of sides, side length, and angle of the polygon.
            This object can be obtained from the compute_polygon_properties function.

        Returns
        -------
        float
            The height of the regular polygon.
        """
        if self.sides % 2 == 0:
            return self.side_length / math.tan(math.pi / self.sides)
        else:
            return self.side_length / (2 * math.tan(math.pi / (2 * self.sides)))
        
    @property
    def perimeter(self) -> float:
        """Calculate the perimeter of the polygon."""
        return self.sides * self.side_length

def compute_polygon_properties(sides,
                               radius
                               ) -> Polygon:
    """
    Compute the side length and angle of a regular polygon
    given the number of sides and the radius of the circumscribed circle.

    Parameters:
    -------
    sides  : int
        The number of sides of the regular polygon.
    radius : float
        The radius of the circumscribed circle.

    Returns
    -------
    Polygon
        A Polygon object containing the number of sides, side length, and interior angle of the regular polygon.

    Raises
    ------
    TypeError
        If the number of sides is not an integer.
    ValueError
        If the number of sides is less than 3.
    ValueError
        If the radius is not a positive number.
    """
    if not isinstance(sides, int):
        raise TypeError("The number of sides must be an integer.")
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    if radius <= 0:
        raise ValueError("The radius must be a positive number.")
    
    side_length = 2 * radius * math.sin(math.pi / sides)
    angle = (sides - 2) * 180 / sides
    
    return Polygon(sides=sides, side_length=side_length, angle=angle)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Regular Polygon")

    my_polygon = compute_polygon_properties(sides=4,
                                            radius=100)

    my_polygon.draw(pos=my_polygon.compute_center(),
                    color='blue')
    
    print(f"lunghezza lato: {my_polygon.side_length}")
    print(f"perimetro: {my_polygon.perimeter}")

    screen.exitonclick()