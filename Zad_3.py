

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property:\nArea: {self.area} m2\nRooms: {self.rooms}\nPrice: {self.price} zł\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}\nHouse details:\nPlot size: {self.plot} m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}\nFlat details:\nFloor: {self.floor}"


house1 = House(area = 150, rooms = 5, price = 250000, address = "Katowice, 12-567, Słoczena 12", plot = 500)
flat1 = Flat(area = 80, rooms = 3, price = 120000, address = "Mariacka, 12-567, 50", floor = 2)


print(house1, "\n")
print("-" * 50)
print(flat1, "\n")

