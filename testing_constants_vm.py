from menu.menu_item import MenuItem, ItemList

zero_balance = "$0.00"
quarter = "$0.25"
fifty_cent = "$0.50"
dollar = "$1.00"
five = "$5.00"
twenty = "$20.00"
all_currency = "$26.25"

drink = "B3"
chips = "A1"

test_menu = {'A1': {'name': 'lays', 'price': '3.75', 'stock': 0},
             'B3': {'name': 'pepsi', 'price': '1.75', 'stock': 10},
             'C4': {'name': 'payday', 'price': '.99', 'stock': 10}, }

lays = MenuItem() \
    .__setitem__('code', 'A1') \
    .__setitem__('name', 'lays') \
    .__setitem__('price', '3.75') \
    .__setitem__('stock', 0)

pepsi = MenuItem() \
    .__setitem__('code', 'B3') \
    .__setitem__('name', 'pepsi') \
    .__setitem__('price', '1.75') \
    .__setitem__('stock', 10)

payday = MenuItem() \
    .__setitem__('code', 'C4') \
    .__setitem__('name', 'payday') \
    .__setitem__('price', '0.99') \
    .__setitem__('stock', 10)


items = ItemList(lays, pepsi, payday)
