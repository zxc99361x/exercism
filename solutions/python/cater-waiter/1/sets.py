from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    a=set(drink_ingredients)
    b=(a&ALCOHOLS)
    if b:
        return drink_name+" Cocktail"
    else:
        return drink_name + " Mocktail"
        
def categorize_dish(dish_name, dish_ingredients):
    categories = {
        'VEGAN': VEGAN,
        'VEGETARIAN': VEGETARIAN,
        'PALEO': PALEO,
        'KETO': KETO,
        'OMNIVORE': OMNIVORE
    }
    for name, category_set in categories.items():
        if dish_ingredients <= category_set:
            return f"{dish_name}: {name}"


def tag_special_ingredients(dish):
    a=set(dish[1])
    a=(a&SPECIAL_INGREDIENTS)
    return (dish[0],a)

def compile_ingredients(dishes):
    a=set()
    for i in dishes:
        a=a.union(i)
    return a


def separate_appetizers(dishes, appetizers):
    a=set(dishes)
    b=set(appetizers)
    a=a-b
    return list(a)

def singleton_ingredients(dishes, intersection):
    a=set()
    for i in dishes:
        a=a | i
    return a-intersection
    
