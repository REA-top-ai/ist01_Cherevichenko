favour_word = 'stepik'
print(favour_word)


first_name = 'Виталий'
last_name = 'Красилов'

new_account = last_name[:5]
temp_password = last_name[3:7]


def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

first_name = input('Введите своё имя\n')
last_name = input('Введите свою фамилию\n')

new_account = account_generator(first_name, last_name)

print(new_account)


def password_generator(first_name, last_name):
    return first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]


first_name = input('Введите своё имя\n')
last_name = input('Введите свою фамилию\n')

temp_password = password_generator(first_name, last_name)

print(temp_password)



company_motto = 'Мечты сбываются'
second_to_last = company_motto[-2]
final_word = company_motto[-4:]


first_name = 'Аоб'
last_name = 'Дейли'

fixed_first_name = 'Р' + first_name[1:]



password_rob_deily = "theycallme\"crazy\"91"

print(password_rob_deily)


poem_title = "spring storm" 
poem_author = "William Carlos Williams" 

poem_title_fixed = poem_title.title()

print(poem_title, poem_title_fixed)




