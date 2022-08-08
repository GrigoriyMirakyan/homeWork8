def print_children(surname, name, patronymic, database, db ):
    id = [i[0] for i in database[db['parents']] if surname and name and patronymic in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:5]) + '\n' for i in deti])


def print_all_childrens(database, db):
    childrens = [i for i in database[db['children']]]
    print(*[' '.join(i[2:5]) + '\n' for i in childrens])


def class_children(surname, name, patronymic, database, db):
    class_of_child = [i[6] for i in database[db['children']] if surname and name and patronymic in i][0]
    print(f'Ученик учится в {class_of_child} классе')


def progress_children(surname, name, patronymic, database, db):
    progress = [i[7] for i in database[db['children']] if surname and name and patronymic in i][0]
    print(f'Успеваемость -> {progress}')