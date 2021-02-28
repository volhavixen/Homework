# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
with open('test_5.txt', 'w+', encoding='utf-8') as file:
    file.write(' '.join([str(randint(1, 200)) for i in range(100)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))
