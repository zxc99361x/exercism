
def create_inventory(items):
    d={}
    for i in items:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

def add_items(inventory, items):
    for i in items:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory


def decrement_items(inventory, items):
    for i in items:
        if i in inventory:
            inventory[i]-=1
            if inventory[i]<=0:
                inventory[i]=0
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    d=[]
    for i,c in inventory.items():
        if c >0:
            d.append((i,c))
    return d

