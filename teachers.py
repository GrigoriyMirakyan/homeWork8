def print_teacher_from_children(surname, name, database, db):
    num_of_class = [i[6] for i in database[db['children']] if surname and name in i][0]
    print(f'number of class {num_of_class}')
    teacher = [i for i in database[db['teachers']] if num_of_class == i[1]]
    print(*[' '.join(i[2:5]) + '\n' for i in teacher])


def print_all_teachers(database, db):
    teachers = [i for i in database[db['teachers']]]
    print(*[' '.join(i[2:5]) + '\n' for i in teachers])


def last_id_teachers(database, db):
    id = [i[-5] for i in database[db['teachers']]][-1]
    return id