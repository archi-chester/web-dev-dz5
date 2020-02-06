"""
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]
# 2 - количество случайных элементов
result = random.sample(numbers, 2)
print(result) # [5, 1]
После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'
Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь
В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""
import random


def main():

    #   бит для вечной игры
    is_infinity = "Да"

    #   получили список чисел
    all_numbers_list = list(range(0, 5))
    selected_numbers_list = random.sample(all_numbers_list, 5)

    #   кортеж имен
    names = (
        #   0
        'Тараса Шевченко',
        #   1
        'Ганса-Христиана Андерсена',
        #   2
        'Ильи Репина',
        #   3
        'Фредди Меркьюри',
        #   4
        'Альфреда Хичкока',
        #   5
        'Майка Тайсона',
        #   6
        'Александра Невского',
        #   7
        'Сальвадора Дали',
        #   8
        'Билла Гейтса',
        #   9
        'Бориса Ельцина'
    )

    #   кортеж дат
    dates = (
        #   0
        '25.02.1814',
        #   1
        '02.04.1805',
        #   2
        '05.08.1844',
        #   3
        '05.09.1946',
        #   4
        '13.08.1899',
        #   5
        '30.06.1966',
        #   6
        '13.05.1221',
        #   7
        '11.05.1904',
        #   8
        '28.10.1955',
        #   9
        '01.02.1931'
    )

    #   кортеж дат
    days = (
        #   0
        'первое',
        #   1
        'второе',
        #   2
        'третье',
        #   3
        'четвертое',
        #   4
        'пятое',
        #   5
        'шестое',
        #   6
        'седьмое',
        #   7
        'восьмое',
        #   8
        'девятое',
        #   9
        'десятое',
        #   10
        'одинадцатое',
        #   11
        'двенадцатое'
        #   12
        'тринадцатое',
        #   13
        'четырнадцатое',
        #   14
        'пятнадцатое',
        #   15
        'шестнадцатое',
        #   16
        'семнадцатое',
        #   17
        'восемнадцатое',
        #   18
        'девятнадцатое'
    )

    #   кортеж дат
    months = (
        #   0
        'января',
        #   1
        'февраля',
        #   2
        'марта',
        #   3
        'апреля',
        #   4
        'мая',
        #   5
        'июня',
        #   6
        'июля',
        #   7
        'августа',
        #   8
        'сентября',
        #   9
        'октября',
        #   10
        'ноября',
        #   11
        'декабря'
    )
    #   зацикливаем
    while is_infinity == "Да":
        rating_true = 0
        #   перебираем выбранный список
        for index in selected_numbers_list:
            #   спрашиваем дату
            current_date = input(f"Назовите дату рождения {names[index]}: ")
            #   сверяем
            if dates[index] == current_date:
                print('Вы правы')
            else:
                day, month, year = dates[index].split(".")
                day_string = ""
                if int(day) == 31:
                    day_string = "тридцать первое"
                elif int(day) == 30:
                    day_string = "тридцатое"
                elif (int(day) < 30) and (int(day) > 20):
                    day_string = f"двадцать {days[(int(day) % 20) - 1]}"
                elif int(day) == 20:
                    day_string = "двадцатое"
                elif (int(day) < 30) and (int(day) > 20):
                    day_string = f"{days[int(day) - 1]}"
                print(f'Вы ошиблись, правильная дата: {int(day)} {months[int(month) - 1]} {year}')

        print(f"Правильных {rating_true}")
        print(f"Неправильных {5 - rating_true}")

        is_infinity = input("Еще раз (Да/любое другое значение)? ")