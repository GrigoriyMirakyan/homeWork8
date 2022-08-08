def id_plus(new_id):
    with open('1.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{new_id};')


def surname_create(surname):
    with open('1.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{surname};')


def name_create(name):
    with open('1.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{name};')


def patronymic_create(patronymic):
    with open('1.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{patronymic};')


def bd_create(bd):
    with open('1.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{bd}')