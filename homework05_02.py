# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("my_file_2.txt") as file_obj:
    content = file_obj.read()
    print(f'Содержимое файла: \n {content}')

with open("my_file_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")


