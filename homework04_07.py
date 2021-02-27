# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). # Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.


from math import factorial
from itertools import count


def fact_gen():
    for el in count(1):
        yield factorial(el)


generator = fact_gen()
x = 0
for i in generator:
    if x == 10:
        break
    else:
        print(i)
        x += 1
