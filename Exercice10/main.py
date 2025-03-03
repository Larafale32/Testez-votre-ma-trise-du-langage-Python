## Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"La personne s'appelle {self.name} et a {self.age} ans"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        return f" {super().display_details()}. Il touche un salaire de {self.salary} euros par mois"

employee1 = Employee("Arnaud", 24, 4000)

print(employee1.display_details())
