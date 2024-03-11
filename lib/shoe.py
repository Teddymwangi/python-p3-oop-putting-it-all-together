class Shoe:
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
        self.is_worn = False

    def wear(self):
        if not self.is_worn:
            print(f"You put on the {self.color} {self.brand} shoes.")
            self.is_worn = True
        else:
            print("You're already wearing these shoes.")

    def take_off(self):
        if self.is_worn:
            print(f"You took off the {self.color} {self.brand} shoes.")
            self.is_worn = False
        else:
            print("You're not wearing these shoes.")