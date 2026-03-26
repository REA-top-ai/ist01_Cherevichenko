tort_1 = ['торт', 1]

household_chemicals = [['стиральный порошо', 1], ['средство для мытья посуды', 1]]

Names =['Ben', 'Holly', 'Ann'] 
dogs_names = ['Sharik', 'Gab', 'Beethoven'] 

names_and_dogs_names = zip(Names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)


orders = ['маргаритки', 'васильки']
orders.append('тюльпаны')
orders.append('розы')
print(orders)


orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия'] 
new_orders = orders + ['сирень', 'ирис']


broken_prices = [5, 3, 4, 5, 4] + [4]



list1 = [1, 8] + list(range(2, 8))
list2 = list(range(1, 8))

list1 = list(range(5, 16, 2)) # Скорее всего в задаче опечатка, с шагом 3 мы не получим 15 в конце
list2 = list(range(0, 41, 5))


first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']

age = list()
age.append(42)

all_ages = [32, 41, 29] + age

name_and_age = list(zip(first_names, all_ages))

ids = list(range(4))







