class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


rect1 = Rectangle(100, 100)
rect2 = Rectangle(50, 50)
rect3 = Rectangle(25, 25)

print(f"The area of the first rectangle is {rect1.area()}, the perimeter - {rect1.perimeter()}")
print(f"The area of the second rectangle is {rect2.area()}, the perimeter - {rect2.perimeter()}")
print(f"The area of the third rectangle is {rect3.area()}, the perimeter - {rect3.perimeter()}")
print()

nums = Math(10, 5)
print(f"The addition of the values equals to {Math.addition(nums)}")
print(f"The subtraction of the values equals to {Math.subtraction(nums)}")
print(f"The multiplication of the values equals to {Math.multiplication(nums)}")
print(f"The division of the values equals to {Math.division(nums)}")

buttons = [
    Button("Text Box"),
    Button("Check Box"),
    Button("Radio Button"),
    Button("Web Tables"),
    Button("Buttons"),
    Button("Links"),
    Button("Broken Links - Images"),
    Button("Upload and Download"),
    Button("Dynamic Properties")
]

print()
print("Названия кнопок:")
for b in buttons:
    print(f" {b.text}")

for b in buttons:
    print(b.click())
