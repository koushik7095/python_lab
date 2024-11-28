class superhero:
    def __init__(self,name,power):
        self.name=name
        self.power=power

    def display_power(self):
        print(f"{self.name}'s power is {self.power}.")

class thor(superhero):
    def __init__(self,name,power,suit_type):
        super().__init__(name,power)
        self.suit_type=suit_type

    def display_suit(self):
        print(f"{self.name} wears a {self.suit_type} suit.")

thor=thor("thor","god of thunder","lighting")
thor.display_power()
thor.display_suit()
