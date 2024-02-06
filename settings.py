from datetime import time,datetime

playermoney = 10000
current_time = datetime.now()
unharvested_fields = []
ready_to_harvest = []
harvested_fields = []
animals = []
tools = []
game_menu = ["1.Fields", "2.Animals", ".3.Shop", "4.Quit"]
field_menu = ["1.Harvest","2.Check unharvested fields","3.Buy fields","4.Go Back"]
fields_to_buy = {
    "Wheat Field": {
        "Cost": 1000,
        "Value": 500,
        "Time_to_harvest": 15
    },
    "Corn Field": {
        "Cost": 1500,
        "Value": 750,
        "Time_to_harvest": 30
    },
    "Barley Field": {
        "Cost": 2000,
        "Value": 1000,
        "Time_to_harvest": 60
    }
}

def mainmenu():
    print("Your father has left you his farm to take over but you have nothing on it and no harvested crops to keep you going.")
    print("You have been given £10,000 in your will to get the farm up and running again.")
    print("Main Menu:")
    for option in game_menu:
        print(option)

    # Get user input after displaying menu options
    option_selected = int(input("What do you want to do: "))
    if option_selected == 1:
        fieldmenu()
    return option_selected

def fieldmenu():
    print("Menu:")
    for option in field_menu:
        print(option)
    try:
        option_selected = int(input("What do you want to do: "))
        if option_selected == 1:
            # Example: Calculate harvest time for the first field
            first_field = list(fields_to_buy.keys())[0]
            harvest_time = current_time + timedelta(minutes=fields_to_buy[first_field]["Time_to_harvest"])
            if harvest_time <= current_time:
                harvested_fields.append(first_field)
            else:
                print("Field is not ready for harvest yet.")
            return fieldmenu()
        elif option_selected == 2:
            print(f"Unharvested fields:" unharvested_fields)
            return fieldmenu()
        elif option_selected == 3:
            print("Available fields to buy:")
            for field_name in fields_to_buy.keys():
                print(field_name)
            chosen_field = input("Which field do you want to buy: ")
            if chosen_field in fields_to_buy.keys():
                unharvested_fields.append(chosen_field)
                print(f"You have bought {chosen_field}.")
            else:
                print("Invalid field name.")
            return fieldmenu()
        elif option_selected == 4:
            return mainmenu()
        else:
            print("Invalid selection. Please select again.")
            return fieldmenu()
    except ValueError:
        print("Invalid selection. Please select again.")
        return fieldmenu()
