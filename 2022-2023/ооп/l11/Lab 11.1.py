class Registration:
    def __init__(self, login):
        self.__login : str
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if login.count('@') != 1:
            return ValueError("Логин должен содержать один символ '@'")
        if '.' not in login and login.find('@') > login.find('.'):
            return ValueError("Логин должен содержать минимум один символ '.' после символа '@'")

        self.__login = login
    