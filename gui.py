import tkinter as tk
from Field import Field
from Animals import Animals
from main import Game

class FarmGameGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game  # Store the game object as an attribute
        self.title("Farm Life 2024")
        self.create_widgets()
        self.geometry('800x400')

    def create_widgets(self):
        frame1 = tk.Frame(self, borderwidth=1, relief='solid')
        frame2 = tk.Frame(self, borderwidth=1, relief='solid')
        frame1.place(x=20, y=50)
        frame2.place(x=200, y=200)

        # Create main menu buttons
        self.fields_btn = tk.Button(frame1, text="Manage Fields", command=self.game.manage_fields)
        self.fields_btn.pack(pady=10,padx=10)

        self.animals_btn = tk.Button(frame1, text="Manage Animals", command=self.game.manage_animals)
        self.animals_btn.pack(pady=10,padx=10)

        self.banking_btn = tk.Button(frame1, text="Banking", command=self.game.show_funds)
        self.banking_btn.pack(pady=10, padx=10)

        self.inventory_btn = tk.Button(frame1, text="Inventory", command=self.game.inventory_menu)
        self.inventory_btn.pack(pady=10, padx=10)

        self.quit_btn = tk.Button(frame1, text="Quit", command=self.quit)
        self.quit_btn.pack(pady=10, padx=10)

    def manage_fields(self):
        self.game.manage_fields(frame2)

if __name__ == "__main__":
    game = Game()
    gui = FarmGameGUI(game)  # Pass the game object when creating the FarmGameGUI instance
    gui.mainloop()
