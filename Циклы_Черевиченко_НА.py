board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble'] 
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket'] 
for game in board_games: 
    print(game) 

for game in sport_games: 
    print(game) 


promise = 'I will not chew gum in class'
for _ in range(5):
    print(promise)


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"] 
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"] 

for student in students_period_A:
    students_period_B.append(student)
    print(student)


dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie'] 
dog_breed_I_want = 'dalmatian' 

for dog in dog_breeds_available_for_adoption:
    if dog == dog_breed_I_want:
        print('У них есть собака, которую я хочу!')
        break



sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]] 
scoops_sold = 0

for market in sales_data:
    scoops_sold += sum(market)

print(scoops_sold)


single_digits = list(range(10))

squares = list()
for num in single_digits:
    print(num)
    squares += [num**2]

cubes = [num**3 for num in single_digits]
print(squares)
print(cubes)

