pi = 3.14159
class polygon:
    def __init__(self, name):
        self.name = name
    #base class
    def prop(self):
        return f"This is a {self.name}."

class Circle(polygon):
    def __init__(self, radius):
        super().__init__("Circle")  
        self.radius = radius
    
    def area(self):
        return pi  * self.radius * self.radius

class Rectangle(polygon):
    def __init__(self, width, height):
        super().__init__("Rectangle")  
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def main():
    a = float(input("Enter radius : "))
    b = float(input("Enter Length : "))
    c = float(input("Enter Length : "))
    
    circle = Circle(a)
    rectangle = Rectangle(b,c)
    
    print(circle.prop())
    print(f"The area of the circle is: {circle.area()}")
    
    print(rectangle.prop())
    print(f"The area of the rectangle is: {rectangle.area()}")

if __name__ == '__main__':
    main()
