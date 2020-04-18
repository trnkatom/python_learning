class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    # by decorating a method with @property, it makes the method behave like attribute, with 1 difference: I can't set value of property, I need to create a SETTER for the property! (Otherwise I would get an Attribute error: can't set attribute)
    # this way, I don't need to call radius(), instead I can use it like circle.radius; often used for some calculations which result I want to use as attribute
    @property
    def radius(self):
        return self.diameter / 2

    # SETTER for radius property! The method MUST have the SAME NAME as the method defined in property!
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

# creates Circle object with diameter=10 (via default init), calculates radius via method radius (=5)
circle = Circle(10)
print(circle.diameter)
print(circle.radius)

# sets property radius=30 via radius.setter, and updates diameter according to the radius (=double the value)
circle.radius = 30
print(circle.diameter)
print(circle.radius)