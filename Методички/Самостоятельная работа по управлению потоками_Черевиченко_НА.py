from random import randint

# 1
name = input('Введите имя человека, который хочет задать вопрос\n')
question = input('Введите вопрос\n')
answer = str()

random_number = randint(1, 10)

if random_number == 1:
    answer = 'Да, безусловно.'
elif random_number == 2:
    answer = 'Это решительно так.'
elif random_number == 3:
    answer = 'Без сомнения.'
elif random_number == 4:
    answer = 'Ответ туманный, попробуйте еще раз.'
elif random_number == 5:
    answer = 'Спросите еще раз позже.'
elif random_number == 6:
    answer = 'Лучше не говорить вам сейчас.'
elif random_number == 7:
    answer = 'Мои источники говорят «нет».'
elif random_number == 8:
    answer = 'Прогноз не очень хороший.'
elif random_number == 9:
    answer = 'Очень сомнительно.'
elif random_number == 10:
    answer = 'Определенно нет.'
else:
    print('Ошибка')

if question == '':
    print('Запустите программу заново и напишите свой вопрос')
elif name == '':
    print(f'Question: {question}')
    print(f'Магический шар отвечает: {answer}')
else:
    print(f'{name} спрашивает: {question}')
    print(f'Магический шар отвечает: {answer}')


# 2
mx = int(input('Введите максимальное значение из описательной статистики'))
average = int(input('Введите среднее значение из описательной статистики'))
mn = int(input('Введите минимальное значение из описательной статистики'))
deviation = int(input('Введите стандартное отклонение значений из описательной статистики'))

if (mx - average > 5 * deviation) or (average - mn > 5 * deviation):
    print('В ваших данных имеются экстремальные значения и требуют предобработки')
elif (mx - average > 3 * deviation) or (average - mn > 3 * deviation):
    print('В ваших данных имеются выбросы и требуют предобработки')
else:
    print('Ваши данные пригодны для анализа')

# 3
age_of_user = int(input('Введите свой возраст\n'))
age_limit = int(input('Введите возрастные ограничения'))

if age_of_user >= age_limit:
    print('Приятного просмотра!')
else:
    print('Извините, ваш возраст не соответствует введенным возрастным ограничениям')

# 4
car_brand = input('Введите марку машины, на которой хотите поехать(Volkswagen Polo / BMW X1)\n')
age_of_driver = int(input('Введите возраст водителя, с которым хотели бы поехать(20 - 34)\n'))
experience_of_driver = int(input('Введите стаж водителя, с которым хотели бы поехать(2 - 15)\n'))
reputation_of_driver = int(input('Введите репутацию водителя, с которым хотели бы поехать(1 - 5)\n'))
traffic_jams = int(input('Введите загруженность дорог в данный момент(1 - 7)\n'))
trip_duration = int(input('Введите длительность поездки(в минутах)\n'))

rate_per_minute = 0
if car_brand == 'Volkswagen Polo':
    if 20 <= age_of_driver <= 27:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 8
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 8.5
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7.5
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 7.4
    elif 27 <= age_of_driver <= 34:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7.2
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 7.2
        elif 10 <= experience_of_driver <= 15:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 6.9
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 6.7
            elif 3 <= reputation_of_driver <= 5:
                if 4 <= traffic_jams <= 7:
                    rate_per_minute = 6.6

elif car_brand == 'BMW X1':
    if 20 <= age_of_driver <= 27:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 12
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 12.5
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.6
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11.3
    elif 27 <= age_of_driver <= 34:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.4
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.7
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11.9
        elif 10 <= experience_of_driver <= 15:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 10.8
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11
            elif 3 <= reputation_of_driver <= 5:
                if 4 <= traffic_jams <= 7:
                    rate_per_minute = 10.9

price = rate_per_minute * trip_duration
if price == 0:
    print('Проверьте введённые вами данные, где-то допущена ошибка')
else:
    print(f'Стоимость вашей поездки составит {price}')


cappuccino_recipe = '''1. Сварите кофе. Можно сварить в 
турке (доведите до кипения 2-3 раза, 
чтобы напиток получился насыщеннее). 
Или заварить во френч-прессе. 
Обязательно процедите, налейте в 
подогретую кружку. 
2. Подогрейте молоко. Старайтесь 
не перегревать его больше, чем 65 
градусов. Оно не должно быть сильно 
горячим. 
3. Взбейте с помощью блендера или 
миксера. Добивайтесь однородной пены, 
без крупных пузырьков. 
4. Влейте взбитую массу в кофе.'''

latte_recipe = '''1. Кофе следует заварить, причем 
любым способом, который вам кажется 
удобнее. 
2. Главное, чтобы кофе был довольно 
крепким. 
3. Молоко нужно разогреть, но не 
кипятить: оптимальной будет 
температура в 50-60 градусов. Читайте 
ещё: вкусный рецепт приготовления 
кофе по турецки. 
4. После этого его нужно тщательно 
взбить с помощью блендера (либо 
миксера).
5. Процедура займет порядка 5 минут, 
пока не образуется воздушная пена. 
6. Следующий шаг – это переливание 
молока в заранее подготовленный 
высокий бокал (лучше всего для этого 
подходит так называемый айриш-бокал). 
7. Пена в итоге все равно останется 
сверху. 
8. Затем нужно влить в молоко кофе. 
9. Делать это нужно очень аккуратно, 
кофе должен литься тоненькой струйкой. 
10. Дело в том, что только таким образом 
может получиться правильный 
трехслойный напиток: молоко, кофе и 
пена сверху. 
11. Завершается приготовление 
классического латте добавлением 
корицы либо шоколада сверху. 
12. Впрочем, можно и вовсе не добавлять 
ничего.'''

Frappuccino_recipe = '''1. Варим и охлаждаем кофе. Для его 
приготовления можно использовать 
турку, кофемашину и любой другой 
прибор. 
Внимание! Для данного рецепта кофе 
можно заменить зеленым чаем. Объем 
тот же – 150 мл. 
2. Все компоненты помещаем в 
стационарный блендер. Ингредиенты 
взбиваем до тех пор, пока лед не 
превратиться в мелкую крошку. 
3. Взбиваем сливки. Их предварительно 
нужно охладить, подержав 1-2 часа в 
холодильнике. При этом продукт нельзя 
замораживать, в противном случае он 
отслоится, и крем не получится. Сливки 
взбиваем миксером. Сначала 
устанавливаем минимальные обороты, 
постепенно увеличивая их количество. 
Продукт взбиваем до того момента, пока 
масса не будет сохранять форму. 
4. Кофе переливаем в бокал. Сверху 
украшаем сливками. Подаем холодным.'''

Espresso_recipe = '''1. В чашку с толстыми стенками 
насыпают растворимый кофе и сахарный 
песок в тех количествах, которые обычно 
используются для одной порции 
2. Далее в чашку добавляют немного 
кипятка и интенсивно взбивают ложкой 
полученную смесь 
3. После некоторого времени масса 
посветлеет и приобретет консистенцию 
сметаны 
4. Во взбитую смесь аккуратно 
доливают оставшуюся воду, медленно 
помешивая до образования густой пены'''

name_of_coffee = input('Введите название кофе\n')

if name_of_coffee == 'Капучино':
    print(cappuccino_recipe)
elif name_of_coffee == 'Латте':
    print(latte_recipe)
elif name_of_coffee == 'Фрапучино':
    print(Frappuccino_recipe)
elif name_of_coffee == 'Эспрессо':
    print(Espresso_recipe)
else:
    print('Введите название кофе корректно')




phrase_11 = 'Коллеги, '
phrase_12 = 'В то же время, '
phrase_13 = 'Однако, '
phrase_14 = 'Тем не менее, '
phrase_15 = 'Следовательно, '
phrase_16 = 'Соответственно, '
phrase_17 = 'Вместе с тем, '
phrase_18 = 'С другой стороны, '

phrase_21 = 'парадигма цифровой экономики '
phrase_22 = 'контекст цифровой трансформации '
phrase_23 = 'диджитализация бизнес-процессов '
phrase_24 = 'прагматичный подход к цифровым платформам '
phrase_25 = 'совокупность сквозных технологий '
phrase_26 = 'программа прорывных иследований '
phrase_27 = 'ускорение блокчейн-транзакций '
phrase_28 = 'экспоненциальный рост Big Data'

phrase_31 = 'открывает новые возможности для '
phrase_32 = 'выдвигает новые требования '
phrase_33 = 'несет в себе риски '
phrase_34 = 'расширяет горизонты '
phrase_35 = 'заставляет искать варианты '
phrase_36 = 'не оставляет шанса для '
phrase_37 = 'повышает вероятность '
phrase_38 = 'обостряет проблему '

phrase_41 = 'дальнейшего углубления '
phrase_42 = 'бюджетного финансирования '
phrase_43 = 'синергетического эффекта '
phrase_44 = 'компрометации конфиденциальных '
phrase_45 = 'универсальной коммодитизации '
phrase_46 = 'несанкционированной кастомизации '
phrase_47 = 'нормативного регулирования '
phrase_48 = 'практического применения'

phrase_51 = 'знаний и компетенций.'
phrase_52 = 'непроверенных гипотез.'
phrase_53 = 'волатильных активов.'
phrase_54 = 'опасных экспериментов.'
phrase_55 = 'государственно-частных партнерств.'
phrase_56 = 'цифровых следов граждан.'
phrase_57 = 'нежелательных последствий.'
phrase_58 = 'внезапных открытий.'


phrase_1 = randint(1, 8)
if phrase_1 == 1:
    str1 = phrase_11
elif phrase_1 == 2:
    str1 = phrase_12
elif phrase_1 == 3:
    str1 = phrase_13
elif phrase_1 == 4:
    str1 = phrase_14
elif phrase_1 == 5:
    str1 = phrase_15
elif phrase_1 == 6:
    str1 = phrase_16
elif phrase_1 == 7:
    str1 = phrase_17
else:
    str1 = phrase_18

phrase_2 = randint(1, 8)
if phrase_2 == 1:
    str2 = phrase_21
elif phrase_2 == 2:
    str2 = phrase_22
elif phrase_2 == 3:
    str2 = phrase_23
elif phrase_2 == 4:
    str2 = phrase_24
elif phrase_2 == 5:
    str2 = phrase_25
elif phrase_2 == 6:
    str2 = phrase_26
elif phrase_2 == 7:
    str2 = phrase_27
else:
    str2 = phrase_28

phrase_3 = randint(1, 8)
if phrase_3 == 1:
    str3 = phrase_31
elif phrase_3 == 2:
    str3 = phrase_32
elif phrase_3 == 3:
    str3 = phrase_33
elif phrase_3 == 4:
    str3 = phrase_34
elif phrase_3 == 5:
    str3 = phrase_35
elif phrase_3 == 6:
    str3 = phrase_36
elif phrase_3 == 7:
    str3 = phrase_37
else:
    str3 = phrase_38

phrase_4 = randint(1, 8)
if phrase_4 == 1:
    str4 = phrase_41
elif phrase_4 == 2:
    str4 = phrase_42
elif phrase_4 == 3:
    str4 = phrase_43
elif phrase_4 == 4:
    str4 = phrase_44
elif phrase_4 == 5:
    str4 = phrase_45
elif phrase_4 == 6:
    str4 = phrase_46
elif phrase_4 == 7:
    str4 = phrase_47
else:
    str4 = phrase_48

phrase_5 = randint(1, 8)
if phrase_5 == 1:
    str5 = phrase_51
elif phrase_5 == 2:
    str5 = phrase_52
elif phrase_5 == 3:
    str5 = phrase_53
elif phrase_5 == 4:
    str5 = phrase_54
elif phrase_5 == 5:
    str5 = phrase_55
elif phrase_5 == 6:
    str5 = phrase_56
elif phrase_5 == 7:
    str5 = phrase_57
else:
    str5 = phrase_58


print(str1 + str2 + str3 + str4 + str5)













