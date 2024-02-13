import os
import random
from Field import Field
from Animals import Animals
from datetime import datetime
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class Game:
    def __init__(self):
        self.fields = [] #List of field objects
        self.animals = [] #List of animal objects
        self.money = 10000  # Starting money

    def start(self):
        print("Welcom to Farm Life 2024")
        print("Your father has left you his farm to take over but you have nothing on it and no harvested crops to keep you going.")
        print("You have been given £10,000 in your will to get the farm up and running again.")

    def save_game(self,filename):
        game_state = {
            "fields":[field.__dict__ for field in self.fields],
            "money":self.money
        }
        with open(filename,"w") as file:
            json.dump(game_state,file,cls=DateTimeEncoder)
            print("Game saved Successfully")

    def load_game(self, filename):
        try:
            with open(filename, 'r') as file:
                game_state = json.load(file)
                self.fields = []
                for field_data in game_state['fields']:
                    field_data['plant_time'] = datetime.fromisoformat(field_data['plant_time']) if field_data['plant_time'] else None
                    self.fields.append(Field(**field_data))
                self.money = game_state['money']
            print("Game loaded successfully.")
        except FileNotFoundError:
            print("Save file not found. Starting new game.")
        except json.JSONDecodeError:
            print("Error decoding save file. Starting new game.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            menu = ["Fields","Animals","Banking","Game Menu"]
            for idx, option in enumerate(menu, start=1):
                print(f"{idx}. {option}")
            try:
                option_selected = int(input("What do you want to do: "))
                if option_selected == 1:
                    self.manage_fields()
                elif option_selected == 2:
                    self.manage_animals()
                elif option_selected == 3:
                    self.show_funds()
                elif option_selected == 4:
                    self.game_menu()
                else:
                    print("Invalid selection. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def game_menu(self):
        print("\nMain Menu:")
        menu = ["Save Game", "Load Game","Go to Game Menu", "Quit"]
        for idx, option in enumerate(menu, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = int(input("What do you want to do: "))
            if option_selected == 4:
                print("Exiting the game. Goodbye!")
                os.system(quit())
            elif option_selected == 1:
                    self.save_game("save_game.json")
            elif option_selected == 2:
                    self.load_game("save_game.json")
            elif option_selected == 3:
                return
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_funds(self):
        print(f"You have £{self.money} left in your account")

    def manage_animals(self):
        print("\n Animal Management:")
        animal_menu = ["Buy Animal","Feed Animal","Butcher Animal"]
        for idx,option in enumerate(animal_menu, start=1):
            print(f"{idx}.{option}")
        try:
            option_selected = int(input("What do you want to do: "))
            if option_selected == 1:
                pass
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def manage_fields(self):
        print("\nField Management:")
        field_menu = ["Buy Field","Field Progress","Plant Fields","Harvest Field","Back to Main Menu"]
        for idx, option in enumerate(field_menu, start=1):
            print(f"{idx}. {option}")
        try:
            option_selected = int(input("What do you want to do:  "))
            if option_selected == 1:
                self.buy_field()
            elif option_selected == 2:
                self.show_fields()
            elif option_selected == 3:
                self.plant_crops()
            elif option_selected == 4:
                self.harvest_field()
            elif option_selected == 5:
                return  # Go back to main menu
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
            crop_types = ["Wheat", "Corn"]
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
                new_field = Field(name="Wheat Field",growtime=200,value=100,crop_type="Wheat")
            elif crop_type == "Corn":
                new_field = Field(name="Corn Field", growtime=100, value=100,crop_type="Corn")
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
                chosen_field.random_event()
                print("Field ready to harvest")
                harvested_value = chosen_field.harvest()
                print(f"You harvested {field.crop_type} from {field.name}.")
                print(f"You added {field.value} to your Capital")
                self.money += field.value
                print(f"you now have £{self.money}")
            else:
                print("Crops are not ready to harvest yet.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = Game()
    game.start()
    game.main_menu()