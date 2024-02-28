import os
import random
import time
from datetime import datetime
import json
from Field import Field
from Animals import Animals

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def clear_screen():
    time.sleep(2)
    os.system("cls")

class Game:
    def __init__(self):
        self.fields = []
        self.animals = []
        self.money = 10000
        self.inventory = {'beef': 0, 'pork': 0, 'milk': 0}
        self.silo = {'Wheat': 0, 'Barley': 0, 'Corn': 0, 'Canola': 0, 'Potato': 0, 'Grapes': 0}

    def validate_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                option = int(user_input)
                if option in valid_options:
                    return option
            print("Invalid input. Please enter a valid option.")

    def start(self):
        print("Welcome to Farm Life 2024")
        print("Your father has left you his farm to take over but you have nothing on it and no harvested crops to keep you going.")
        print("You have been given £10,000 in your will to get the farm up and running again.")

    def save_game(self, filename):
        game_state = {
            "fields": [field.__dict__ for field in self.fields],
            "animals": [animal.__dict__ for animal in self.animals],
            "money": self.money
        }
        with open(filename, "w") as file:
            json.dump(game_state, file, cls=DateTimeEncoder)
            print("Game saved successfully.")

    def load_game(self, filename):
        try:
            with open(filename, 'r') as file:
                game_state = json.load(file)
                self.fields = [Field(**field_data) for field_data in game_state['fields']]
                self.money = game_state['money']
            print("Game loaded successfully.")
        except FileNotFoundError:
            print("Save file not found. Starting new game.")
        except json.JSONDecodeError:
            print("Error decoding save file. Starting new game.")

    def main_menu(self):
        menu = ["Fields", "Animals", "Banking", "Inventory", "Game Menu"]
        while True:
            print("\nMain Menu:")
            for idx, option in enumerate(menu, start=1):
                print(f"{idx}. {option}")
            try:
                option_selected = self.validate_input("What do you want to do: ", list(range(1, len(menu) + 1)))
                if option_selected == 1:
                    self.manage_fields()
                elif option_selected == 2:
                    self.manage_animals()
                elif option_selected == 3:
                    self.show_funds()
                elif option_selected == 4:
                    self.inventory_menu()
                elif option_selected == 5:
                    self.game_menu()
                else:
                    print("Invalid selection. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def game_menu(self):
        menu = ["Save Game", "Load Game", "Go Back", "Quit"]
        print("\nGame Menu:")
        for idx, option in enumerate(menu, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = self.validate_input("What do you want to do: ", list(range(1, len(menu) + 1)))
            if option_selected == 1:
                self.save_game("save_game.json")
            elif option_selected == 2:
                self.load_game("save_game.json")
            elif option_selected == 3:
                return
            elif option_selected == 4:
                print("Exiting the game. Goodbye!")
                quit()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_funds(self):
        print(f"You have £{self.money} left in your account.")

    def manage_fields(self):
        field_menu = ["Buy Field", "Show Field Progress", "Plant Fields", "Harvest Field", "Back to Main Menu"]
        print("\nField Management:")
        for idx, option in enumerate(field_menu, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = self.validate_input("What do you want to do: ", list(range(1, len(field_menu) + 1)))
            if option_selected == 1:
                self.buy_field()
            elif option_selected == 2:
                self.show_fields()
            elif option_selected == 3:
                self.plant_crops()
            elif option_selected == 4:
                self.harvest_field()
            elif option_selected == 5:
                return
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def buy_field(self):
        print("\nYou're buying a field.")
        field_cost = 2000
        if self.money >= field_cost:
            self.money -= field_cost
            new_field = Field()
            self.fields.append(new_field)
            print("Field purchased successfully!")
            print(f"Funds reduced by {field_cost} and your bank account is now {self.money}")
        else:
            print("Not enough money to buy the field.")

    def show_fields(self):
        if not self.fields:
            print("You don't own any fields yet.")
        else:
            print("\nList of Fields:")
            for i, field in enumerate(self.fields, start=1):
                print(f"Field {i}: {field.name}: {field.crop_type}: {field.growtime}: {field.progress_bar()}")

    def plant_crops(self):
        if not self.fields:
            print("You don't own any fields yet.")
            return
        print("\nFields available for planting:")
        for i, field in enumerate(self.fields, start=1):
            print(f"{i}. {field.name}")
        try:
            field_index = int(input("Choose a field to plant crops in (enter the field number): "))
            if field_index < 1 or field_index > len(self.fields):
                print("Invalid field number.")
                return
            crop_types = ["Wheat", "Corn", "Canola", "Barley", "Potatoes", "Grapes"]
            print("Select the crop type:")
            for idx, option in enumerate(crop_types, start=1):
                print(f"{idx}. {option}")
            crop_type_index = int(input("Enter the number of the crop type: "))
            if crop_type_index < 1 or crop_type_index > len(crop_types):
                print("Invalid crop type number.")
                return
            chosen_field = self.fields[field_index - 1]
            crop_type = crop_types[crop_type_index - 1]
            if crop_type == "Wheat":
                new_field = Field(name="Wheat Field", growtime=100, value=100, crop_type="Wheat")
            elif crop_type == "Corn":
                new_field = Field(name="Corn Field", growtime=100, value=75, crop_type="Corn")
            elif crop_type == "Canola":
                new_field = Field(name="Canola Field", growtime=400, value=400, crop_type="Canola")
            elif crop_type == "Barley":
                new_field = Field(name="Barley Field", growtime=50, value=50, crop_type="Barley")
            elif crop_type == "Potatoes":
                new_field = Field(name="Potato Field", growtime=600, value=1000, crop_type="Potatoes")
            elif crop_type == "Grapes":
                new_field = Field(name="Grapes Field", growtime=200, value=200, crop_type="Corn")
            chosen_field.plant_crops(new_field.crop_type)
            print(f"You planted {crop_type} in {chosen_field.name}.")
            print(f"Growth time for {new_field.name}: {new_field.growtime} seconds")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def harvest_field(self):
        if not self.fields:
            print("You don't own any fields yet.")
            return
        print("\nFields available for harvesting:")
        for i, field in enumerate(self.fields, start=1):
            print(f"{i}. {field.name}")
        try:
            field_index = int(input("Choose a field to harvest crops from (enter the field number): "))
            if field_index < 1 or field_index > len(self.fields):
                print("Invalid field number.")
                return
            chosen_field = self.fields[field_index - 1]
            if chosen_field.is_ready_to_harvest():
                harvested_value = chosen_field.harvest()
                print(f"You harvested {field.crop_type} from {field.name}.")
                self.silo[field.crop_type] += random.randint(500, 1000)
            else:
                print("Crops are not ready to harvest yet.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def manage_animals(self):
        animal_menu = ["Buy Animal", "Feed Animal", "Meat Processing", "Milk Cows", "Show Animals", "Go back"]
        print("\nAnimal Management:")
        for idx, option in enumerate(animal_menu, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = self.validate_input("What do you want to do: ", list(range(1, len(animal_menu) + 1)))
            if option_selected == 1:
                self.buy_animals()
            elif option_selected == 2:
                self.feed_animals()
            elif option_selected == 3:
                self.process_butchering()
            elif option_selected == 4:
                self.milk_cows()
            elif option_selected == 5:
                self.show_animals()
            elif option_selected == 6:
                return
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_animals(self):
        if not self.animals:
            print("You don't own any animals yet.")
        else:
            print("\nList of Animals:")
            for i, animal in enumerate(self.animals, start=1):
                print(f"Animal {i}: {animal.species} || Age: {animal.age} || Hunger: {animal.progress_bar()}")

    def milk_cows(self):
        if not self.animals:
            print("You don't own any animals yet.")
        else:
            for animal in self.animals:
                animal.milk()

    def process_butchering(self):
        if not self.animals:
            print("You don't own any animals yet.")
        else:
            for animal in self.animals:
                animal.butcher()

    def feed_animals(self):
        if not self.animals:
            print("You don't own any animals to feed.")
        else:
            for animal in self.animals:
                animal.feed()

    def buy_animals(self):
        print("\nYou're buying a new animal.")
        animal_type = ["Cow", "Pig"]
        for idx, option in enumerate(animal_type, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = int(input("What do you want to buy: "))
            animal_cost = 200
            if self.money >= animal_cost:
                self.money -= animal_cost
                animal_type = "Cow" if option_selected == 1 else "Pig"
                new_animal = Animals(age=1, hunger=100, species=animal_type)
                self.animals.append(new_animal)
                print(f"{new_animal.species} purchased successfully!")
                print(f"Funds reduced by {animal_cost} and your bank account is now {self.money}")
            else:
                print("Not enough money to buy an animal.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def inventory_menu(self):
        inventory_menu = ['Show inventory', 'Sell Items', 'Go Back']
        print("\nInventory Menu:")
        for idx, option in enumerate(inventory_menu, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = int(input("What do you want to do: "))
            if option_selected == 1:
                self.show_inventory()
            elif option_selected == 2:
                self.sell_items()
            elif option_selected == 3:
                return
        except ValueError:
            print("Invalid input. Please enter a number.")

    def sell_items(self):
        print("\nSell Items:")
        item = input("What do you want to sell (beef, pork, milk, wheat, corn, canola, barley, potato, grapes): ").strip().lower()
        if item not in self.inventory and item not in self.silo:
            print("Invalid item.")
            return
        try:
            quantity = int(input(f"How many kg of {item} do you want to sell: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                return
            if item in ['beef', 'pork', 'milk']:
                self.sell_to_butcher(item, quantity)
            else:
                self.sell_silo(item.capitalize(), quantity)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def sell_to_butcher(self, item, quantity):
        butcher_price = 10
        milk_price = 2
        if item == 'beef' or item == 'pork':
            total_price = butcher_price * quantity
        elif item == 'milk':
            total_price = milk_price * quantity
        if quantity <= self.inventory[item]:
            self.inventory[item] -= quantity
            self.money += total_price
            print(f"{quantity} kg of {item} sold for £{total_price}")
        else:
            print("You don't have enough of that item to sell.")

    def sell_silo(self, item, quantity):
        price = 1
        if quantity <= self.silo[item]:
            self.silo[item] -= quantity
            self.money += quantity * price
            print(f"{quantity} kg of {item} sold for £{quantity * price}")
        else:
            print("You don't have enough of that item to sell.")

if __name__ == "__main__":
    game = Game()
    game.start()
    game.main_menu()
