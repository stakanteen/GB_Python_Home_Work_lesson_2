# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

crazy_list = [int(10), float(10.10), str('abc'), b'hello']
for item in crazy_list:
    print(item, ' - ', type(item))