class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname

        if(gender != "male" and gender != "female"):
            print("Значение не передано.")
            self.gender = "male"
        else:
            self.gender = gender

    def __str__(self):
        if(self.gender == "male"):
            return(f"Гражданин: {self.surname} {self.name}")
        elif(self.gender == "female"):
            return(f"Гражданка: {self.surname} {self.name}")
        else:
            return ("Error")

p1 = Person('Maddison', 'Cynthia', 'female')
print(p1) # печатает "Гражданка Cynthia Maddison"
p2 = Person('Zoe', 'Amber', 'female')
print(p2) # печатает "Гражданка Amber Zoe"
p3 = Person('Oscar', 'Smith', True)# печатает "Значение не передано."
print(p3) # печатает "Гражданин Smith Oscar"
p4 = Person('Tony', 'Stark', 'faugy')# печатает "Значение не передано."
print(p4) # печатает "Гражданин Stark Tony"
p5 = Person('Mary', 'Sew', 7)# печатает "Значение не передано."
print(p5) # печатает "Гражданин Sew Mary"
p6 = Person('Zoe', 'Amber', 'Female')# печатает "Значение не передано."
print(p6) # печатает "Гражданин Amber Zoe"