class User:
    # id = 0
    # first_name = 'firstName'
    # last_name = 'secondName'
    # birthday = '31.12.2000'

    def __init__(self, id, first_name, last_name, birthday):
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name
        self.birthday = birthday
    
    def greet_user(self):
        print('Давно тебя не было в уличных гонках,', self.first_name, self.last_name + '.')

user1 = User(1, 'Stephan', 'Korobeynich', '10.08.1994')
user2 = User(2, 'Matt', 'Serpov', '07.06.1998')
user3 = User(3, 'Maxim', 'Johnson', '14.01.2000')
user4 = User(4, 'Ken', 'Belov', '11.11.1993')

# User.greet_user()
user1.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()