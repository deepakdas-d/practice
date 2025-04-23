#POLYMORPHISM

class dog:
    def sound(self):
        print("Barks...")

class cat:
    def sound(self):
        print("Meow...")

ani=[dog(),cat()]
for i in ani:
    i.sound()
