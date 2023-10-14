class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary 
        self.gender = gender 
        self.passport = passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')

persons = [ 
    ('Allison Hill', 334053, 'M', '1635644202'), 
    ('Megan Mcclain', 191161, 'F', '2101101595'), 
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'), 
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'), 
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'), 
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126') 
]

worker1 = Worker(persons[0][0], persons[0][1], persons[0][2], persons[0][3])
worker2 = Worker(persons[1][0], persons[1][1], persons[1][2], persons[1][3])
worker3 = Worker(persons[2][0], persons[2][1], persons[2][2], persons[2][3])
worker4 = Worker(persons[3][0], persons[3][1], persons[3][2], persons[3][3])
worker5 = Worker(persons[4][0], persons[4][1], persons[4][2], persons[4][3])
worker6 = Worker(persons[5][0], persons[5][1], persons[5][2], persons[5][3])
worker7 = Worker(persons[6][0], persons[6][1], persons[6][2], persons[6][3])
worker8 = Worker(persons[7][0], persons[7][1], persons[7][2], persons[7][3])
worker9 = Worker(persons[8][0], persons[8][1], persons[8][2], persons[8][3])
worker10 = Worker(persons[9][0], persons[9][1], persons[9][2], persons[9][3])

worker_objects = [ 
    worker1,
    worker2,
    worker3,
    worker4,
    worker5,
    worker6,
    worker7,
    worker8,
    worker9,
    worker10
]

for i in range(0, 10):
    worker_objects[i].get_info()