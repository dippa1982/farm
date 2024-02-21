from datetime import datetime, timedelta, time

class Animals:
    def __init__(self,age,hunger,animal_type):
        self.age = age
        self.hunger = hunger
        self.animal_type = animal_type
        self.last_fed_time = datetime.now()

    def milk(self):
        if self.animal_type == "Cow":
            print("Milking Cow")
        else:
            print("Cant milk this animal type")

    def butcher(self):
        pass

    def age_one_year(self):
        self.age += 1
        print(f"The {self.animal_type} is now {self.age} year(s) old.")
        if self.age >= 10:
            self.die()

    def feed(self):
        if self.hunger <= 30:
            self.hunger = 100
            self.last_fed_time = datetime.now()
            print(f"{self.animal_type} has been fed.")
        else:
            print(f"{self.animal_type} doent need feeding\n Hunger levels are {self.hunger}")

    def reduce_hunger(self):
        current_time = datetime.now()
        time_since_last_fed = current_time - self.last_fed_time
        hunger_reduction_rate = 0.1
        self.hunger -= hunger_reduction_rate * time_since_last_fed.total_seconds()
        self.hunger = max(0, self.hunger)  # Ensure hunger doesn't go below 0
        if self.hunger == 0:
            self.die()

    def die(self):
        if self.hunger == 0:
            print(f"The {self.animal_type} has died of starvation.")
        elif self.age >= 10:
            print(f"The {self.animal_type} has died of old age.")

    def progress_bar(self):
        if self.hunger == 0:
            return "Animal is Dead"
        else:
            current_time = datetime.now()
            time_elapsed = current_time - self.last_fed_time
            progress = min(1.0, time_elapsed.total_seconds() / (30 * 60))  # Assuming hunger decay rate of 30 minutes
            bar_length = 20
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            return f"[{bar}] {progress * 100:.1f}%"
