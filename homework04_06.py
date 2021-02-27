# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

print('Для продолжения работы программы нажмите Enter. Если хотите выйти, нажмите Q')
for el in count(int(input('Введите стартовое число '))):
    print(el)
    stop = input().upper()
    if stop == 'Q':
        break

my_list = [123, 'babay', 1.2, None, False]
for el in cycle(my_list):
    print(el)
    print(el)
    stop = input().upper()
    if stop == 'Q':
        break
