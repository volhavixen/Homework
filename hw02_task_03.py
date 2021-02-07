# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
seasonlist = ['winter', 'spring', 'summer', 'autumn']
seasondict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

if month == 1 or month == 2 or month == 12:
        print(seasonlist[0])
        print(seasondict.get(1))

elif month == 3 or month == 4 or month == 5:
    print(seasonlist[1])
    print(seasondict.get(2))

elif month == 6 or month == 7 or month == 8:
    print(seasonlist[2])
    print(seasondict.get(3))

elif month == 9 or month == 10 or month == 11:
    print(seasonlist[3])
    print(seasondict.get(4))
else:
    print('Ошибка! Введите число от 0 до 12: ')