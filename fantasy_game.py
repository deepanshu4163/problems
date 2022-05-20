"""
You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detail-
ing how many of that item the player has. For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take any possible
“inventory” and display it.

Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems) , where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot .

The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item.
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
    
# displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)      #The setdefault() method is a nice shortcut to ensure that a key exists. If key doesn't exist then it adds key to dictionary and set value 0
        inventory[i] = inventory[i] + 1 
    """
    ALTERNATIVE METHOD WITHOUT USING   setdefault()

        for i in addedItems:
        if i in inventory.keys():
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1

    """
    
    return inventory        

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)