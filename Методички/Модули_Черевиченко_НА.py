from matplotlib import pyplot as plt
from string import ascii_letters
from datetime import datetime
import random

current_time = datetime.now() 
print(current_time)


random_list = [random.randint(1, 100) for _ in range(101)]

random_number = random.choice(random_list)
print(random_list)
print(random_number)


number_a = list(range(1, 13))
number_b = random.sample(range(1000), 12)

plt.plot(number_a, number_b)
plt.show()




employees = [
    {
        'ФИО': 'Иванов Иван Иванович',
        'Должность': 'Менеджер',
        'Дата найма': '22.10.2013',
        'Оклад': 250000
    },
    {
        'ФИО': 'Сорокина Екатерина Матвеевна',
        'Должность': 'Аналитик',
        'Дата найма': '12.03.2020',
        'Оклад': 75000
    },
    {
        'ФИО': 'Струков Иван Сергеевич',
        'Должность': 'Старший программист',
        'Дата найма': '23.04.2012',
        'Оклад': 150000
    },
    {
        'ФИО': 'Корнеева Анна Игоревна',
        'Должность': 'Ведущий программист',
        'Дата найма': '22.02.2015',
        'Оклад': 120000
    },
    {
        'ФИО': 'Старчиков Сергей Анатольевич',
        'Должность': 'Младший программист',
        'Дата найма': '12.11.2021',
        'Оклад': 50000
    },
    {
        'ФИО': 'Бутенко Артем Андреевич',
        'Должность': 'Архитектор',
        'Дата найма': '12.02.2010',
        'Оклад': 200000
    },
    {
        'ФИО': 'Савченко Алина Сергеевна',
        'Должность': 'Старший аналитик',
        'Дата найма': '13.04.2016',
        'Оклад': 100000
    }
]



def programmer_bonus(employees):
    bonus_dict = {}
    
    for employee in employees:
        if 'программист' in employee['Должность'].lower():
            bonus = employee['Оклад'] * 0.03
            bonus_dict[employee['ФИО']] = bonus
    
    return bonus_dict


def holiday_bonus(employees):
    bonus_dict = {}

    for employee in employees:
        name_parts = employee['ФИО'].split()
        patronymic = name_parts[2] 
        if patronymic.endswith(('на', 'вна')):
            bonus_dict[employee['ФИО']] = 2000
        else:
            bonus_dict[employee['ФИО']] = 4000
    return bonus_dict


def salary_indexation(employees):
    indexed_salaries = {}
    current_date = datetime.now()
    
    for employee in employees:
        hire_date = datetime.strptime(employee['Дата найма'], '%d.%m.%Y')
        years_worked = (current_date - hire_date).days / 365.25
        
        if years_worked > 10:
            new_salary = employee['Оклад'] * 1.07  
        else:
            new_salary = employee['Оклад'] * 1.05  
        
        indexed_salaries[employee['ФИО']] = new_salary
    return indexed_salaries


def vacation_schedule(employees):
    eligible_employees = []
    current_date = datetime.now()
    
    for employee in employees:
        hire_date = datetime.strptime(employee['Дата найма'], '%d.%m.%Y')
        days_worked = (current_date - hire_date).days 
        
        if days_worked > 6 * 30:
            eligible_employees.append(employee['ФИО'])
    
    return eligible_employees




admin_number = random.randint(1, 9)

num_participants = random.randint(5, 30)
participants = [random.randint(1, 100) for _ in range(num_participants)]

cnt = 0
for number in participants:
    digit_sum = sum(int(digit) for digit in str(number))
    
    if digit_sum % admin_number == 0:
        cnt += 1
        print(f"Выигрышный номер: {number}")
        if cnt == 5:
            break

print(f'Загаднное число - {admin_number}')






n = int(input('Введите количество бросков монеты: '))
for _ in range(n):
    print(random.choice(['Орел', 'Решка']))



n = int(input('Введите количество бросков кубика: '))
for _ in range(n):
    print(random.randint(1, 6))



length = int(input('Введите длину пароля: '))
characters = ascii_letters
password = [random.choice(characters) for _ in range(length)]
print(''.join(password))



