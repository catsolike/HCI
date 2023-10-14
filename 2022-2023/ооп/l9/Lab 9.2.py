class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Банк работает только c числами")

    def withdraw(self, value):
        Customer.check_type(value)
        if value > self.balance:
            raise ValueError("Сумма списания превышает баланс")

        self.balance -= value
    
    def deposit(self, value):
        Customer.check_type(value)
        self.balance += value


bob = Customer('Bob Odenkirk')
bob.deposit(200)
print(bob.balance) # 200
bob.withdraw(150)
print(bob.balance) # 50
# bob.deposit('hello') # TypeError: Банк работает только с числами
# bob.withdraw(300) # ValueError: Сумма списания превышает баланс