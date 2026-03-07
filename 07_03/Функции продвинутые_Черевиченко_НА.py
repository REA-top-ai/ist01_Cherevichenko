from json import dumps

tables = { 
    1: ['Jiho', False], 
    2: [], 
    3: [], 
    4: [], 
    5: [], 
    6: [], 
    7: [], 
} 

def assign_table(table_number, name, vip_status = False):
    tables[table_number].append(name)
    tables[table_number].append(vip_status)

assign_table(6, 'Yoni', False)
assign_table(4, 'Карл')

print(tables)


def print_order(*order_items):
    print(order_items)

print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')

tables = { 
1: { 
    'name': 'Jiho', 
    'vip_status': False, 
    'order': 'Orange Juice, Apple Juice' 
    }, 
    2: {}, 
    3: {}, 
    4: {}, 
    5: {}, 
    6: {}, 
    7: {}, 
}

def assign_table(table_number, name, vip_status = False):
    keys = ['name', 'vip_status']
    tables[table_number] = {key: value for key, value in zip(keys, [name,  vip_status])}
        

def assign_and_print_order(table_number, *order_items):
    tables[table_number] |= {'order': order_items}
    
    for dish in order_items:
        print(dish)

assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Стейк', 'Морской окунь', 'Бутылка вина')


tables = { 
    1: { 
        'name': 'Chioma', 
        'vip_status': False, 
        'order': { 
            'drinks': 'Orange Juice, Apple Juice', 
            'food_items': 'Pancakes' 
        } 
        }, 
        2: {}, 
        3: {}, 
        4: {}, 
        5: {}, 
        6: {}, 
        7: {}, 
} 

def assign_food_items(table_number, **order_items):
    order = dict()
    if order_items.get('food') is not None:
        order['food'] = order_items['food']
    if order_items.get('drinks') is not None:
        order['drinks'] = order_items['drinks']

    assign_and_print_order(table_number, order)

assign_food_items(3, food='Pancakes, Poached Egg', drinks='Water')
print(dumps(tables, indent=4, ensure_ascii=False))



def calculate_price_per_person(total, tip, split): 
    total_tip = total * (tip/100) 
    split_price = (total + total_tip) / split 
    print(split_price) 
               
table_7_total = [534.5, 20, 5]

calculate_price_per_person(*table_7_total)

