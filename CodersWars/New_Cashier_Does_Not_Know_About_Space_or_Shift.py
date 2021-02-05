# Some new cashiers started to work at your restaurant.
#
# They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
#
# All the orders they create look something like this:
#
# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
#
# The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
#
# Their preference is to get the orders as a nice clean string with spaces and capitals like so:
#
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
#
# The kitchen staff expect the items to be in the same order as they appear in the menu.
#
# The menu items are fairly simple, there is no overlap in the names of the items:
#
# 1. Burger
# 2. Fries
# 3. Chicken
# 4. Pizza
# 5. Sandwich
# 6. Onionrings
# 7. Milkshake
# 8. Coke

def get_order(order):
    menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    result = []
    for word in menu:
        for i in range(order.count(word.lower())):
            result.extend([word])

    print(result)
    return ' '.join(result)



order = 'milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza'
print(get_order(order))

def get_orders(order):
    menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    aray = [ i for i in order]
    result = []
    word = ''
    while aray:
        if len(aray) != 0:
            word += aray[0]
            aray.pop(0)
            if word.title() in menu:
                result.append(word.title())
                word = ''
    return ' '.join(result)

print(get_orders(order))
