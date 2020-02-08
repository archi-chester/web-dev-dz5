"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import json


#   пополнить счет
def add_money_to_account(acc, add_money):
    acc += add_money
    print("-----------------------\n")
    set_account(acc)
    return acc


#   получить значение счета из файла
def get_account():
    account = 0
    if os.path.exists("account.txt"):
        #   менеджер контекста
        with open('account.txt', 'r') as f:
            account = int(f.read())
    else:
        with open('account.txt', 'w') as f:
            f.write(str(account))
    return int(account)


#   получить значение счета из файла
def get_purchases():
    purchases = dict()
    if os.path.exists("purchases.json"):
        #   менеджер контекста
        with open('purchases.json', 'r') as f:
            purchases = json.load(f)
    else:
        with open('purchases.json', 'w') as f:
            json.dump(purchases, f)
    return purchases


#   пополнить счет
def set_account(account):
    with open('account.txt', 'w') as f:
        f.write(str(account))
    pass


#   пополнить счет
def set_purchases(purchases):
    with open('purchases.json', 'w') as f:
        json.dump(purchases, f)
    pass


#   покупка
def purchase(purchases, account):
    money_amount = int(input("Сколько хотите потратить? "))
    if money_amount > account:
        print("Недостаточно средств - пополните счет\n")
    else:
        purchase_name = input("Что хотите купить? ")
        purchases[purchase_name] = money_amount
        print(f"Вы купили {purchase_name} за {money_amount}\n")
        set_purchases(purchases)
    print("-----------------------\n")
    pass


#   история покупок
def show_history(purchases):
    print("\nВаши покупки\n-----------------------")
    for key in purchases.keys():
        print(f"{key} - {purchases[key]}")
    print("-----------------------\n")
    pass


def menu():
    #   переменные
    #   счет
    set_account(100)
    account = get_account()
    #   покупки словариком
    purchases = get_purchases()

    #   меню
    while True:
        print(f'На счету {account}\n--------------------')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account = add_money_to_account(account, int(input("Сколько кредит добавить на счет? ")))
            pass
        elif choice == '2':
            purchase(purchases, account)
            pass
        elif choice == '3':
            show_history(purchases)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
