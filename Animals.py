from datetime import datetime, timedelta

class Animals:
    def __init__(self,age,animal_type):
        self.age = age
        self.hunger = 100
        self.animal_type = animal_type
        self.last_fed_time = datetime.now()

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

    def age_one_year(self):
        self.age += 1
        print(f"The {self.animal_type} is now {self.age} year(s) old.")

    def feed(self):
        self.hunger = 100
        self.last_fed_time = datetime.now()
        print(f"{self.animal_type} has been fed.")

    def reduce_hunger(self):
        current_time = datetime.now()
        time_since_last_fed = current_time - self.last_fed_time
        print(time_since_last_fed)
        # Reduce hunger gradually based on elapsed time (adjust rate as needed)
        hunger_reduction_rate = 0.1 # Adjust as needed
        self.hunger -= hunger_reduction_rate * time_since_last_fed.total_seconds()
        # Ensure hunger level does not go below 0
        self.hunger = max(0, self.hunger)
        if self.hunger == 0:
            self.die()

    def die(self):
        print(f"The {self.animal_type} has died of starvation.")

    def progress_bar(self):
        if self.hunger == 100:
            return "Animal has just been fed"
        else:
            current_time = datetime.now()
            time_since_last_fed = current_time - self.last_fed_time
            max_hunger_time = timedelta(hours=4)
            progress = min(1.0, time_since_last_fed.total_seconds() / max_hunger_time.total_seconds())
            bar_length = 20
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            return f"[{bar}] {progress * 100:.1f}%"