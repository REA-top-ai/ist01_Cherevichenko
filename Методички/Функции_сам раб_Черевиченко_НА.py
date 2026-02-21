# 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9

    return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32

    return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


# 2
def get_force(train_mass, train_acceleration):
    return train_acceleration * train_mass

train_force = get_force(75000, 100000)
print(f'Поезд GE поставляет {train_force} ньютонов силы')



def get_energy(bomb_mass, c = 3 * 10**8):
    return bomb_mass * c**2

bomb_energy = get_energy(1)
print(f'1 кг бомбы составляет {bomb_energy} Джоулей')


def get_work(train_mass, train_acceleration, train_distance):
    return get_force(train_mass, train_acceleration) * train_distance

train_mass = 22680 
train_acceleration = 10 
train_distance = 100 

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f'Поезд выполняет {train_work} Джоулей за {train_distance} метров.')




def done(user_name, ARM):
    if user_name == 'Дмитрий' and ARM == 1:
        return True
    if user_name == 'Ангелина' and ARM == 2:
        return True
    if user_name == 'Василий' and ARM == 3:
        return True
    if user_name == 'Екатерина' and ARM == 4:
        return True

    return False

user_name = input('Введите своё имя\n')
ARM = int(input('Введите свой APM'))

text_for_users = 'Добро пожаловать'
Dmitiy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'

if done(user_name, ARM):
    print(text_for_users)

elif user_name == 'Дмитрий':
    print(Dmitiy_check)

else:
    print('Логин или пароль не верный, попробуйте еще раз')    



def is_A(grade):
    return grade >= 4

def is_B(grade):
    return grade >= 3

def is_C(grade):
    return grade >= 2

def is_D(grade):
    return grade >= 1

def is_F(grade):
    return grade >= 0

grade = int(input('Введите средний балл студента\n'))
if is_A(grade):
    print('A')
elif is_B(grade):
    print('B')
elif is_C(grade):
    print('C')
elif is_D(grade):
    print('D')
elif is_F(grade):
    print('F')
