'''
Создать информационную систему позволяющую работать с сотрудниками
некой компании \ студентами вуза \ учениками школы
'''
import teachers
import children
import greate_database
import list_of_class
import parents
import add_parent
import add_teacher
import add_children

db = {'parents': 1, 'children': 2, 'teachers': 3}
greate_database.reading_file_to_dict(1)
greate_database.reading_file_to_dict(2)
greate_database.reading_file_to_dict(3)
database = greate_database.database

choice = int(input('что вы хотите сделать?\nПоказать список учеников -> введите 1\nПоказать список родителей -> введите 2'
                   '\nПоказать список учитилей -> введите 3\nПоказать список класса -> введите 4\nПоказать учеников родителя -> введите 5'
                   '\nУзнать в каком классе учится ученик -> введите 6\nУзнать успеваемость ученика -> введите 7\nДобавить родителя -> введите 8'
                   '\nДобавить учителя -> введите 9\n'))
if choice == 1:
    children.print_all_childrens(database, db)
elif choice == 2:
    parents.print_all_parents(database, db)
elif choice == 3:
    teachers.print_all_teachers(database, db)
elif choice == 4:
    num_of_class = (input('Введите класс: '))
    list_of_class.print_list_of_class(num_of_class, database, db)
elif choice == 5:
    surname, name, patronymic = input('Введите фамилию: '), input('Введите имя: '), input('Введите отчество: ')
    children.print_children(surname, name, patronymic, database, db)
elif choice == 6:
    surname, name, patronymic = input('Введите фамилию: '), input('Введите имя: '), input('Введите отчество: ')
    children.class_children(surname, name, patronymic, database, db)
elif choice == 7:
    surname, name, patronymic = input('Введите фамилию: '), input('Введите имя: '), input('Введите отчество: ')
    children.progress_children(surname, name, patronymic, database, db)
elif choice == 8:
    new_id = (int(parents.last_id_parents(database, db)) + 1)
    add_parent.id_plus(new_id)
    surname, name, patronymic, bd = input('Введите фамилию: '), input('Введите имя: '), input('Введите отчество: '), input('Введите дату рождения в формате dd.mm.yyyy: ')
    add_parent.surname_create(surname)
    add_parent.name_create(name)
    add_parent.patronymic_create(patronymic)
    add_parent.bd_create(bd)
elif choice == 9:
    new_id = (int(teachers.last_id_teachers(database, db)) + 1)
    add_teacher.id_plus(new_id)
    add_teacher.num_of_class_create(input('Введите класс: '))
    add_teacher.surname_create(input('Введите фамилию: '))
    add_teacher.name_create(input('Введите имя: '))
    add_teacher.patronymic_create(input('Введите отчество: '))
elif choice == 0:
    new_id = (int(add_children.last_id_children(database, db)) + 1)
    add_children.id_plus(new_id)
    add_children.id_par_plus(input('Введите ID родителя: '))
    add_children.surname_create(input('Введите фамилию: '))
    add_children.name_create(input('Введите имя: '))
    add_children.patronymic_create(input('Введите отчество: '))
    add_children.bd_create(input('Введите дату рождения в формате dd.mm.yyyy: '))
    add_children.num_of_class_create(input('Введите класс: '))
    add_children.progress_create(input('Введите успеваемость ученика: '))
else:
    print('Введено неверное значение!!!')


    #Здравствуйте Денис, уже по ходу написания понял, что вместо ID было бы очень неплохо использовать СНИЛС и было бы попроще
    #да и весь этот список вопросов было бы хорошо разбить на блоки и как то сгруппировать... вот такой вот "автокодревью"))
