def print_list_of_class(num_of_class, database, db):
    list_of_class = [i for i in database[db['children']] if num_of_class == i[6]]
    print(*[' '.join(i[2:4]) + '\n' for i in list_of_class])