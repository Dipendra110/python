class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My cat name is {self.name} and {self.name} is {self.age} years old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My dog name is {self.name} and {self.name} is {self.age} years old.")
    def make_sound(self):
        print("Bark")
cat1=Cat("Charlie",2)
dog1=Dog("Rahul",7)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

dog1.make_sound()
cat1.info()