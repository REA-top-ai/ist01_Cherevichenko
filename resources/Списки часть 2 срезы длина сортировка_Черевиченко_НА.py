list1 = list(range(2, 20, 2))
list1_len = len(list1)
print(list1_len)

list1 = list(range(2, 20, 3))
list1_len = len(list1)
print(list1_len)

# Было 9, стало 6. Уменьшилось на 3 или уменьшилась в 1.5 раза



employees = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт'] 
index4 = employees[4]

print(len(employees))
print(employees[6])


shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья'] 
last_element = shopping_list[-1]
element5 = shopping_list[5]

print(last_element, element5)


suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги'] 
beginning = suitcase[0:2] # 2 элемента
beginning = suitcase[:4]

middle = suitcase[2:4]
print(middle)


suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги'] 
start = suitcase[:3]


votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)


addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.'] 
addresses.sort()
print(addresses)


games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon'] 
games_sorted = sorted(games)
print(games_sorted)


inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двуспальная кровать', 'двуспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка', 'королевский кровать', 'двуспальная кровать', 'две односпальные кровати', 'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('две односпальные кровати') # хихи, не запутаете
inventory.sort()

