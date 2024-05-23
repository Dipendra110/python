# class Person:
#     def __init__(self, name, place):
#         self.name = name
#         self.place = place
#
#     def info(self):
#         return (self.name, self.place)
#
#
# class Employee(Person):
#     pass
#
#
# a = Employee("abc", "npj")
# print(a.info())
#
#
# class Dog:
#     def eat(self):
#         print('Dog is eating')
#
#
# class Animal(Dog):
#     def display(self):
#         print("Display")
#
#
# a = Animal()
# a.display()
# a.eat()


class He:
    def hear(self):
        print("He can hear")

    def see(self):
        print("He can see")


class She:
    def feel(self):
        print("She can feel")

    def taste(self):
        print("She can taste")

    def hear(self):
        print("She can hear")


class Person(He, She):
    pass


a = Person()
a.hear()
a.taste()
