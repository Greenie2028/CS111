from math import pi
class Shape:
    '''

    '''
    def __init__(self,name="Unknown"):
        self.name = name

    def get_area(self):
        raise NotImplementedError(f"get_area not implemented in {type(self)}")
    
    def __str__(self):
        return f"{self.name}: {self.get_area()}"
    
    def show(self):
        print(self)

class Triangle(Shape):
    def __init__(self,base,height):
        self.height = height
        self.base = base
        super().__init__("Triangle")
    def get_area(self):
        return .5*self.base*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__("Circle")
    def get_area(self):
        return round(pi*self.radius**2,2)


for item in [Circle(5), Triangle(4,2), Triangle(1,9)]:
    item.show()