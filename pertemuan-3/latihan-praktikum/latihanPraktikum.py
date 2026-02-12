class Character:
    def __init__(self, name, hp, speciality):
        self.name = name
        self.hp = hp
        self.speciality = speciality
        self.money = 1000
    
    def show_char(self):
        print(f"Your Character\nName: {self.name}\nSpeciality: {self.speciality}\n=========================")

    def change_name(self, newName):
        self.name = newName
        print(f"Name changed to {newName}\n=========================")

    def check_money(self):
        print(f"Your balance: {self.money}\n=========================")

char1 = Character("Barley", 3000, "Thrower")
char1.show_char()
char1.check_money()
char1.change_name("Dynamike")