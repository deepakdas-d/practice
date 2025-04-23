#Inheritance

class Animal:
    def sound(self):
        print("make Sound")
class Dog(Animal):
    def basic(self):
        super().sound()
    def sound(self):
        print("Dog barks.")

d=Dog()
d.basic()
d.sound()
      