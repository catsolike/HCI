class Quadrilateral:
    def __init__(self, width, height=None):
        if(not height):
            height = width
            
        self.width = width
        self.height = height

    def __str__(self):
        if(self.width == self.height):
            return(f"Квадрат размером {self.width}*{self.height}")
        else:
            return(f"Прямоугольник размером {self.width}*{self.height}")

    def __bool__(self):
        return (self.width == self.height)

q1 = Quadrilateral(10)
print(q1) # печатает "Квадрат размером 10*10"
print(bool(q1)) # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2) # печатает "Прямоугольник размером 3*5"
print(q2 == True) # печатает "False"