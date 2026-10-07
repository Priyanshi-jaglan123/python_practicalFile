# Inventory of different stores

store1 = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

store2 = {
    "Laptop": 5,
    "Keyboard": 10,
    "Monitor": 8
}

store3 = {
    "Mouse": 10,
    "Monitor": 5,
    "Printer": 4
}


# Merging inventories
inventory = {}

for store in (store1, store2, store3):

    for product, quantity in store.items():

        inventory[product] = inventory.get(product, 0) + quantity


# Display final inventory
print("Combined Inventory:")

for product, quantity in inventory.items():
    print(product, ":", quantity)