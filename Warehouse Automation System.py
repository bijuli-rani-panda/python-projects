class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity):
        self.inventory[name] = quantity

    def remove_product(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] -= quantity

    def show_inventory(self):
        for item, qty in self.inventory.items():
            print(item, ":", qty)

w = Warehouse()

w.add_product("Laptop", 10)
w.add_product("Mouse", 50)

w.remove_product("Mouse", 5)

w.show_inventory()