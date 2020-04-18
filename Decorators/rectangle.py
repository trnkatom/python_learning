class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return (self.width * 2) + (self.length * 2)

rectangle = Rectangle(5,10)
print("width: {}\nlength: {}\n-> area: {} (width*length)\n-> perimeter: {} (width*2+length*2)".format(
    rectangle.width,
    rectangle.length,
    rectangle.area,
    rectangle.perimeter))