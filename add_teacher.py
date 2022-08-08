def id_plus(new_id):
    with open('3.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{new_id};')


def surname_create(surname):
    with open('3.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{surname};')


def name_create(name):
    with open('3.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{name};')


def patronymic_create(patronymic):
    with open('3.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{patronymic}')


def num_of_class_create(num_of_class):
    with open('3.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{num_of_class};')
