class House():
    """"описание дома"""
    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 70

    def build(self):
        """строить дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен.")

    def age_house(self,year):
        """возраст дома"""
        self.age += year






class ProspectHouse(House):
    """дома на проспекте"""
    def __init__(self,prospect,number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = ProspectHouse("Ленина",5)
print(PrHouse.prospect)

