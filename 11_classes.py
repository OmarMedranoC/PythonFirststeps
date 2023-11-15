#### Classes#######

from ast import Pass


class MyEmptyPerson:
    pass
print(MyEmptyPerson())
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Omar", "Medrano")
print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self):
        self.name = "Omar"
        self.surname = "Medrano"

my_person = Person()
print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} esta caminando")    

my_person = Person("Omar", "Medrano")
print(my_person.full_name)
my_person.walk()
