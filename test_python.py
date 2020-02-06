"""
В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt,
pow, hypot. Чем больше тестов на каждую функцию - тем лучше
"""
from math import pi, sqrt, pow, hypot


#   filter
def test_filter():
    items = [3, 2, 1, 4, 5]
    sorted_items = list(sorted(items))
    assert sorted_items == [1, 2, 3, 4, 5]
    pass


#   map
def test_map():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    assert squared == [1, 4, 9, 16, 25]
    pass


#   sorted
def test_sorted():
    # array = list(['2','1'])
    # assert array.sor
    pass


#   pi
def test_pi():
    assert pi == 3.141592653589793
    pass


#   sqrt
def test_sqrt():
    assert sqrt(4) == 2
    pass


#   pow
def test_pow():
    assert pow(3, 3) == 27
    pass


#   hypot
def test_hypot():
    assert hypot(3, 4) == 5
    pass

