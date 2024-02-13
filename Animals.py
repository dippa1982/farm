from datetime import datetime, timedelta

class Animals:
    def __init__(self,age,animal_type):
        self.age = age
        self.hunger = 100
        self.animal_type = None

    def milk(self):
        if self.animal_type == "Cow":
            print("Milking Cow")
        else:
            print("Cant milk this animal type")

    def feed(self):
        if self.hunger <= 30:
            print(f"Feeding {self.animal_type} hunger levels are now {self.hunger}")

    def butcher(self):
        pass