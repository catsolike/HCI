class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Access:
    __access_list = ["admin", "developer"]

    @staticmethod
    def __check_access(role):
        return role in Access.__access_list

    @staticmethod
    def get_access(usr):
        if not isinstance(usr, User):
            return print("AccessTypeError")

        if Access.__check_access(usr.role):
            return print(f"User {usr.name}: success")
        else: 
            return print("Access Denied")




user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"
zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied
Access.get_access(5) # печатает AccessTypeError