import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """



jack = Point()
# print(type(jack))

jack.x = 150
jack.y = 25

# print(jack.x, jack.y)

# x = jack.y
# print(x)


# import math

# print('(%g, %g)' % (jack.x, jack.y))
# distance = math.sqrt(jack.x**2 + jack.y**2)
# print(distance)


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
 
# print_point(jack)


def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))

# jonathan = Point()
# jonathan.x = 4
# jonathan.y = 5


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    distance = math.sqrt(x_diff**2 + y_diff**2)
    return distance


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner1, corner2, corner3, corner4.
    """

angela = Rectangle()
angela.width = 50
angela.height = 25
angela.corner1 = jack
angela.corner2 = Point()
angela.corner2.x = angela.corner1.x + angela.width
angela.corner2.y = angela.corner1.y
angela.corner3 = Point()
angela.corner3.x = angela.corner2.x
angela.corner3.y = angela.corner2.y - angela.height
angela.corner4 = Point()
angela.corner4.x = angela.corner3.x - angela.width
angela.corner4.y = angela.corner3.y

def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# sarah = find_center(angela)
# print_point(sarah)



def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)

# print_rectangle(angela)
# grow_rectangle(angela, 50, 100)
# print('after growing')
# print_rectangle(angela)


print('Exercise #2')
class Circle:
    """
    Representa a circle.

    attributes: center, radius.
    """
allison = Circle()
allison.center = Point()
allison.center.x = 150
allison.center.y = 100

allison.radius = 75


def point_in_circle(Circle, Point):
    return Circle.center.x - Circle.radius <= Point.x <= Circle.center.x + Circle.radius and Circle.center. y - Circle.radius <= Point.y <= Circle.center.y + Circle.radius


print('Is the point in the circle? ',point_in_circle(allison, jack))


def rect_in_circle(Rectangle, Circle):
    if point_in_circle(Circle, Rectangle.corner1):
        if point_in_circle(Circle, Rectangle.corner2):
            if point_in_circle(Circle, Rectangle.corner3):
                if point_in_circle(Circle, Rectangle.corner4):
                    return True
    else:
        return False

print('Is the rectanle within the circle? ',rect_in_circle(angela, allison))

def rect_circle_overlap(Rectangle, Circle):
    return point_in_circle(Circle, Rectangle.corner1) or point_in_circle(Circle, Rectangle.corner2) or point_in_circle(Circle, Rectangle.corner3) or point_in_circle(Circle, Rectangle.corner4)

print('Rectangle and circle overlap? ', rect_circle_overlap(angela, allison))

# def main():
#     my_point = Point()
#     print(Point.__doc__)
#     my_point.x = 3
#     my_point.y = 4
#     print('My point', end=' ')
#     print_point(my_point)

#     print('Is my_point an instance of Point?', isinstance(my_point, Point))
#     print('Is my_point an instance of Rectangle?',
#           isinstance(my_point, Rectangle))
#     print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
#     print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

#     box = Rectangle()
#     box.width = 100.0
#     box.height = 200.0
#     box.corner = Point()
#     box.corner.x = 0.0
#     box.corner.y = 0.0

#     print('Does box have an attribute x?', hasattr(box, 'x'))

#     print('Does box have an attribute corner?', hasattr(box, 'corner'))

#     print('Rectangle has these:', dir(box))

#     center = find_center(box)
#     print('center', end=' ')
#     print_point(center)

#     print(box.width)
#     print(box.height)
#     print('grow')
#     grow_rectangle(box, 50, 100)
#     print(box.width)
#     print(box.height)


# if __name__ == '__main__':
#     main()
