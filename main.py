"""
Консольный файловый менеджер:

1. Создать новый проект ""Консольный файловый менеджер"

2. В проекте реализовать следующий функционал:

После запуска программы пользователь видит меню, состоящее из следующих пунктов:

- создать папку;

- удалить (файл/папку);

- копировать (файл/папку);

- просмотр содержимого рабочей директории;

- посмотреть только папки;

- посмотреть только файлы;

- просмотр информации об операционной системе;

- создатель программы;

- играть в викторину;

- мой банковский счет;

- смена рабочей директории (*необязательный пункт);

- выход.

Так же можно добавить любой дополнительный функционал по желанию.
"""
import account
import victory
import os
import platform
from shutil import copyfile


#   меню
while True:
    print('#' * 10, "\nКонсольный файловый менеджер\n", "#" * 10)
    print('1.   создать папку')
    print('2.   удалить (файл/папку)')
    print('3.   копировать (файл/папку)')
    print('4.   просмотр содержимого рабочей директории')
    print('5.   посмотреть только папки')
    print('6.   посмотреть только файлы')
    print('7.   просмотр информации об операционной системе')
    print('8.   создатель программы')
    print('9.   играть в викторину')
    print('10.  мой банковский счет')
    print('11.  сохранить содержимое рабочей директории в файл')
    print('0. выход')

    choice = input(f'{"#" * 10}\nВыберите пункт меню: ')
    #   создать папку
    if choice == '1':
        new_dir = input("Введите имя директории: ")
        if os.path.exists(new_dir):
            print(f"Папка {new_dir} уже существует")
        else:
            os.mkdir(new_dir)
            print(f"Создана папка {new_dir}")
        pass

    #   удалить (файл/папку)
    elif choice == '2':
        new_dir = input("Введите имя директории: ")
        if not os.path.exists(new_dir):
            print(f"Папка {new_dir} не существует")
        else:
            os.rmdir(new_dir)
            print(f"Удалена папка {new_dir}")
        pass

    #   копировать (файл/папку)
    elif choice == '3':

        item_for_copy = input('Выберите файл для копирования: ')
        if not os.path.exists(item_for_copy):
            print(f"Папка {item_for_copy} не существует")
        else:
            copyfile(item_for_copy, item_for_copy + "_copy")
            print(f"Создание {item_for_copy + '_copy'} успешно завершено")
        pass

    #   просмотр содержимого рабочей директории
    elif choice == '4':
        print(f"Содержимое {os.getcwd()}:")
        for item in os.listdir("."):
            print(item)
        pass

    #   посмотреть только папки
    elif choice == '5':
        print(f"Содержимое {os.getcwd()}　(только папки):")
        for item in os.listdir("."):
            if os.path.isdir(item):
                print(item)
        pass

    #   посмотреть только файлы
    elif choice == '6':
        print(f"Содержимое {os.getcwd()}　(только папки):")
        for item in os.listdir("."):
            if os.path.isfile(item):
                print(item)
        pass

    #   просмотр информации об операционной системе
    elif choice == '7':
        print(f'OS: {platform.system()}')
        pass

    #   создатель программы
    elif choice == '8':
        print("\nArchibald v. Chester aka B@dB10ck\n")
        pass

    #   играть в викторину
    elif choice == '9':
        victory.main()
        pass

    #   мой банковский счет
    elif choice == '10':
        account.menu()
        pass

    #   сохранить содержимое рабочей директории в файл
    elif choice == '11':
        files_str = "files: " + ", ".join(list(filter(lambda cur_file: os.path.isfile(cur_file), os.listdir("."))))
        dirs_str = "dirs: " + ", ".join(list(filter(lambda cur_dir: os.path.isdir(cur_dir), os.listdir("."))))

        print(files_str, dirs_str)

        with open('current_dir.txt', 'w', encoding='utf-8') as f:
            f.writelines([files_str, '\n', dirs_str])
        pass

    #   мой банковский счет
    elif choice == '0':
        break
    else:
        print('Неверный пункт меню')