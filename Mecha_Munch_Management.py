'''a = {x: 2 **x  for x in range(10)}
print(a)
'''
def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item not in current_cart:
            current_cart.setdefault(item, 1)
        else:
            current_cart[item] += 1
    print(current_cart)
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    new_cart = {item: 1 for item in notes}

    return new_cart



def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for recipe,update in recipe_updates:
        #if recipe in ideas:
         #   ideas[recipe].update(update)
        if recipe in ideas:
            ideas[recipe] = update
        else:
            ideas[recipe] = update
    print(get.keys())
    return ideas

'''update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                    'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
                    'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
[('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})])

{'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
 'Raspberry Pie': {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2},
 'Pasta Primavera': {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1},
 'Blueberry Crumble': {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3}}
'''


def send_to_store(cart, aisle_mapping):
    """Combines users order to aisle and refrigeration information.

    Takes a user's shopping cart and aisle and refrigeration information
    and returns a dictionary with the information ready to send to the store.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    #Create dictionary to hold cart and aisle information
    fulfillment = {}

    #Loop through cart items
    for clave in cart:
        #Get the items quantity and aisle information
        valor1 = [cart.get(clave,[])]#Convert the result into a list so the two dictionaries values can be combined
        valor2 = aisle_mapping.get(clave,[])

        #Add items and aisle information to fulfillment dictionary
        fulfillment[clave] = valor1 + valor2
    diccionario_invertido ={}
    #for clave in reversed(sorted(fulfillment.keys())):
    #    diccionario_invertido[clave] = fulfillment[clave]
    
    

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for product,quantity in fulfillment_cart.items():
        store_inventory[product][0] -= quantity[0]
    for product,quantity in store_inventory.items():
        if quantity[0] == 0:
            quantity[0] = 'Out of Stock'

    
    print(store_inventory)



update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
{'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]})
