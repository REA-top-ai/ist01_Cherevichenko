
# 1
print((6 * 6) - 1 == 8 + 1) # False (35 != 9)
print(13 - 7 != (3 * 2) + 1) # True (6 != 7)
print(3 * (2 - 1) == 4 - 1) # True (3 == 3)

# 2
print((6 * 6) - 1 >= 8 + 1) # True (35 >= 9)
print(13 - 7 <= (3 * 2) + 1) # True (6 <= 7)
print(3 * (2 - 1) > 4 - 1) # False (3 == 3)

# 3
'''bool_variable = true

print(bool_variable) # NameError. Из-за того, что python чувствителен к регистру(True != true)
'''
bool_variable = 'true'

print(type(bool_variable)) # Тип - str(string)


bool_variable = True

print(type(bool_variable)) # Тип - bool


# 4
user_name = input('Введите своё имя\n')

text_for_users = 'Добро пожаловать'
Dmitiy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'

if user_name == 'Дмитрий':
    print(Dmitiy_check)
if user_name != 'Дмитрий':
    print(text_for_users)


enter_number = 0

if enter_number < 3:
    print(f'Попробуйте еще раз. У вас осталось {3 - enter_number} попыток')
if enter_number >= 3:
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки')



# 5
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0) # False
statement_two = (4 * 2 <= 8) and (7 - 1 == 6) # True



user_name = input('Введите своё имя\n')
ARM = int(input('Введите свой APM'))

text_for_users = 'Добро пожаловать'
Dmitiy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'

done = False
if user_name == 'Дмитрий' and ARM == 1:
    print(text_for_users)
    done = True
if user_name == 'Ангелина' and ARM == 2:
    print(text_for_users)
    done = True
if user_name == 'Василий' and ARM == 3:
    print(text_for_users)
    done = True
if user_name == 'Екатерина' and ARM == 4:
    print(text_for_users)
    done = True

if user_name != 'Дмитрий' and not(done):
    print('Логин или пароль не верный, попробуйте еще раз')
if not(done) and user_name == 'Дмитрий':
    print(Dmitiy_check)


print((2 - 1 > 3) or (-5 * 2 == -10)) # True
print((9 + 5 <= 15) or (7 != 4 + 3)) # True



user_name = input('Введите своё имя\n')
ARM = int(input('Введите свой APM'))

text_for_users = 'Добро пожаловать'
Dmitiy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'

done = False
if user_name == 'Дмитрий' and ARM == 1:
    print(text_for_users)
    done = True
if user_name == 'Ангелина' and ARM == 2:
    print(text_for_users)
    done = True
if user_name == 'Василий' and ARM == 3:
    print(text_for_users)
    done = True
if user_name == 'Екатерина' and ARM == 4:
    print(text_for_users)
    done = True

if not(done):
    if user_name == 'Дмитрий':
        print(Dmitiy_check)
    else:
        print('Логин или пароль не верный, попробуйте еще раз')    


grade = int(input('Введите средний балл студента\n'))

if grade >= 4.0:
    print('A')
elif grade >= 3.0:
    print('B')
elif grade >= 2.0:
    print('C')
elif grade >= 1.0:
    print('D')
elif grade >= 0:
    print('F')
