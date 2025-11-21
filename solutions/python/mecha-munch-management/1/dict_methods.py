def add_item(current_cart, items_to_add):
    for i in items_to_add:
        if i in current_cart:
            current_cart[i]+=1
        else:
            current_cart[i]=1
    return current_cart


def read_notes(notes):
    d = {}
    for i in notes:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d


def update_recipes(ideas, recipe_updates):
    for n,i in recipe_updates:
        ideas[n]=i
    return ideas


def sort_entries(cart):
    d=sorted(cart.items())
    return d


def send_to_store(cart, aisle_mapping):
    d={}
    for item in sorted(cart.keys(),reverse=True):
        q=cart[item]
        info=aisle_mapping[item]
        d[item]=[q]+info
    return d


def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart.keys():
        q=fulfillment_cart[item][0]
        store_inventory[item][0]-=q
        if store_inventory[item][0]<=0:
            store_inventory[item][0]="Out of Stock"
    return store_inventory
            
