# addInventory.py
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # if the dictionary is not empty iterate values in the list to compare against the dictionary
    # when a list item is equal to a key increment the value in the dictionary by the count in the list 
    for i in range(len(addedItems)):
        if(addedItems[i] in list(inventory.keys())):
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1 
        else:
            inventory.setdefault(addedItems[i], 1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)