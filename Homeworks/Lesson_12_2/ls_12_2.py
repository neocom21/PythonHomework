class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}" # lemon, price: 5

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}" # Ivan Ivanov



class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        #User: Ivan Ivanov
        #Items:
        #lemon: 4 pcs.
        #apple: 20 pcs.

        tx= f"User: {self.user}\nItems: \n"
        for item, cnt in self.products.items():
            tx += f"{item.name}: {cnt} pcs.\n"

        return tx

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total



lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )

print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov


cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)

print(cart)

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
