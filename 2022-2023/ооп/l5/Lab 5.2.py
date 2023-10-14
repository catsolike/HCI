class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if(isinstance(i, int)):
                self.values.append(i)

    def __str__(self):
        if (not self.values):
            return("Пустой вектор")
        else:
            # return(f"Вектор ({sorted(self.values)})")  # возвращает список с квадратными скобками
            return 'Вектор ' + ', '.join([str(i) for i in sorted(self.values)])  # возвращает значения из списка в строковом типе; разделитель - запятая

v1 = Vector(1, 32, 12, 'abc')
print(v1) # печатает "Вектор(1, 12, 32)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"