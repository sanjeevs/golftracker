'''
Immutable value object representing the positon of a point.
'''

class ScreenCoord:
    ''' Represent a point on the screen.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"ScreenCoord({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other,  ScreenCoord):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

class CartCoord:
    ''' Represent a point with origin at left bottom of screen.'''
    def __init__(self, screen_coord, height):
        self.x = screen_coord.x
        self.y = height - y

    def __repr__(self):
        return f"CartCoord({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other,  CartCoord):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

class ScreenPath:
    ''' A immutable sequence of points in screen coordinates. '''
    def __init__(self, coordinates=None):
        if coordinates is None:
            coordinates = []
        self.coordinates = tuple(coordinates)

    def __repr__(self):
        return f"ScreenPath({', '.join(map(str, self.coordinates))})"

    def __eq__(self, other):
        if isinstance(other, Path):
            return self.coordinates == other.coordinates
        return False

    def __hash__(self):
        return hash(self.coorindates)

    def x_values(self, n):
        return [coordinate.x for coordinate in self.coordinates[:n]]

    def y_values(self, n):
        return [coordinate.y for coordinate in self.coordinates[:n]]


def CartPath(Path):
    def __init__(self, path, height):
        cart_coordinates = [CartCoord(coord, height) for coord in path.coordinates]
        super().__init__(coordinates=cart_coordinates)