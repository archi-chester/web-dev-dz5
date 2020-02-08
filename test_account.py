"""
В том же проекте создать модуль test_account.py для тестирования функций консольного файлового менеджера

Пришлось принудительно сделать функцию чистой, хотя весь функционал сводится к вводу выводу - тут нет смысла их тестить
"""
import json

import account as acc
import os


def test_add_money_to_account():
    assert 200 == acc.add_money_to_account(150, 50)
    pass


def test_get_account():
    if os.path.exists("account.txt"):
        with open('account.txt', 'r') as f:
            account_from_file = int(f.read())
            assert acc.get_account() == account_from_file

    else:
        assert (acc.get_account() == 0) and (os.path.exists("account.txt"))


def test_get_purchases():
    if os.path.exists("purchases.json"):
        with open('purchases.json', 'r') as f:
            purchases_from_file = json.load(f)
            assert acc.get_purchases() == purchases_from_file

    else:
        assert (acc.get_purchases() == {}) and (os.path.exists("purchases.json"))


def test_set_account():
    acc.set_account(50)
    assert (acc.get_account() == 50) and (os.path.exists("account.txt"))


def test_set_purchases():
    acc.set_purchases({})
    assert (acc.get_purchases() == {}) and (os.path.exists("purchases.json"))
