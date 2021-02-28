# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.


if __name__ == "__main__":
    subjects = {}

    try:
        with open("test_6.txt", encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            data = line.replace('(', ' ').split()
            subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
    except IOError as err:
        print(err)
    except ValueError:
        print('Ошибка! Проверьте еще раз')

    print(subjects)
