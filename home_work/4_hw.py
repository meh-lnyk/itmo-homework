class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(100, 100)
rect2 = Rectangle(50, 50)
rect3 = Rectangle(25, 25)

print(f"The area of the first rectangle is {rect1.area()}, the perimeter - {rect1.perimeter()}")
print(f"The area of the second rectangle is {rect2.area()}, the perimeter - {rect2.perimeter()}")
print(f"The area of the third rectangle is {rect3.area()}, the perimeter - {rect3.perimeter()}")
