class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'Стоимость {self.brand} {self.model} составляет {self.price}'

lenovo = Laptop('lenovo','z-570-dx', '25_000')
print(lenovo.laptop_name)