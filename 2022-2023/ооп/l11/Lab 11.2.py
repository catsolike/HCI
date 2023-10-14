class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.__balance: float
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        if not isinstance(value,(int, float)):
            raise TypeError('Value is not a number')
        self.__balance += value
        
    
    def payment(self, value) -> bool:
        if not isinstance(value, (int, float)): 
            raise TypeError("Value is not integer or float")

        if self.balance < value:
            print("Недостаточно средств на балансе. Пополните счет")
            return False
        
        self.balance -= value
        return True 

user_1 = User('Username_1', 10)
product_1 = Product('product_1', 7)
product_2 = Product('product_2', 700)
# a.payment('100')
print(user_1)
print(user_1.balance)
print(user_1.deposit(100))
print(user_1.payment(product_1.price))
print(user_1.payment(product_2.price))
print(user_1)

