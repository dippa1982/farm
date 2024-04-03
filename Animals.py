from datetime import datetime, timedelta
import random

class Animals:
    """Class to represent farm animals."""
    HUNGER_THRESHOLD = 30
    OLD_AGE_THRESHOLD = 10
    HUNGER_DECAY_RATE = 0.1

    def __init__(self, age: int, hunger: int, species: str):
        self.age = age
        self.hunger = hunger
        self.species = species
        self.last_fed_time = datetime.now()

    def milk(self) -> int:
        """Simulate milking the animal and return the amount of milk produced."""
        if self.species == "Cow":
            current_time = datetime.now()
            milk_time = current_time - timedelta(hours=1)
            if milk_time >= self.last_fed_time:
                milk_amount = random.randint(50, 100)
                print(f"Milking Cow. Produced {milk_amount}kg of milk.")
                self.last_fed_time = current_time
                return milk_amount
            else:
                print("Cow not ready for milking")
                return 0
        else:
            print("No cows to milk")
            return 0

    def age_one_year(self) -> None:
        """Simulate the animal aging by one year."""
        current_time = datetime.now()
        one_hour_ago = current_time - timedelta(hours=1)
        if one_hour_ago >= self.last_fed_time:
            self.age += 1
            self.last_fed_time = current_time
            if self.age >= self.OLD_AGE_THRESHOLD:
                self.die()

    def butcher(self) -> int:
        """Simulate butchering the animal and return the amount of meat produced."""
        if self.species == "Cow":
            meat_amount = 50
            print(f"Butchering {meat_amount}kg of beef from the cow.")
            self.add_to_inventory("beef", meat_amount)
            return meat_amount
        elif self.species == "Pig":
            meat_amount = 30
            print(f"Butchering {meat_amount}kg of pork from the pig.")
            self.add_to_inventory("pork", meat_amount)
            return meat_amount
        else:
            print("Cannot butcher this animal type.")
            return 0

    def feed(self) -> None:
        """Feed the animal, resetting its hunger level."""
        if self.hunger <= self.HUNGER_THRESHOLD:
            self.hunger = 100
            self.last_fed_time = datetime.now()
            print(f"{self.species} has been fed.")
        else:
            print(f"{self.species} doesn't need feeding")

    def reduce_hunger(self) -> None:
        """Reduce the animal's hunger level over time."""
        current_time = datetime.now()
        time_since_last_fed = current_time - self.last_fed_time
        self.hunger -= self.HUNGER_DECAY_RATE * time_since_last_fed.total_seconds()
        self.hunger = max(0, self.hunger)  # Ensure hunger doesn't go below 0
        if self.hunger == 0:
            self.die()

    def die(self) -> None:
        """Handle the death of the animal."""
        if self.hunger == 0:
            print(f"The {self.species} has died of starvation.")
        elif self.age >= self.OLD_AGE_THRESHOLD:
            print(f"The {self.species} has died of old age.")

    def progress_bar(self) -> str:
        """Generate a progress bar representing the animal's hunger level."""
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
