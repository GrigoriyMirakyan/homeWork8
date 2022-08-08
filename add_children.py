def surname_create(surname):
    with open('2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{surname};')


def name_create(name):
    with open('2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{name};')


def patronymic_create(patronymic):
    with open('2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{patronymic};')


def bd_create(bd):
    with open('2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{bd};')


def progress_create(progress):
    with open('2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{progress}')


def last_id_children(database, db):
    id = [i[-8] for i in database[db['children']]][-1]
    return id


def id_plus(new_id):
    with open('2.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{new_id};')


def id_par_plus(id_par):
    with open('2.txt', 'a', encoding='utf-8') as file:
        file.write(f'{id_par};')


def num_of_class_create(num_of_class):
    with open('2.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{num_of_class};')