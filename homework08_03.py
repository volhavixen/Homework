# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список: ')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ENN:
        print(ENN,'-', 'это не число! Попробуйте еще раз.')
print(my_list)