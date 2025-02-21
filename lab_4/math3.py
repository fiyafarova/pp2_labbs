import math

def regular_polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

num_sides = 4
side_length = 25

area = regular_polygon_area(num_sides, side_length)
print("The area of the polygon is:", int(area))
