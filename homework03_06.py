# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(a):
    word = a.split(' ')
    total = []
    for i in word:
        string_element = str(i)
        first_letter = str(i)[:1].upper()
        all_words = first_letter + string_element[1:]
        total.append(all_words)
    return total

words = input('Введите строку из слов, разделенных пробелами: ').split()
for i in words:
    output = int_func(i)
    if output:
        print(int_func(i), ' ')
