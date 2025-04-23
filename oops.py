#Object Oriented Programming.

class car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def info(self):
        print(f"Name:{self.name}")
my=car('Ford','Mustang',1975)
my.info()

        