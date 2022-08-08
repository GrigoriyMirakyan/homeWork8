def print_all_parents(database, db):
    parents = [i for i in database[db['parents']]]
    print(*[' '.join(i[1:4]) + '\n' for i in parents])

def last_id_parents(database, db):
    id = [i[-5] for i in database[db['parents']]][-1]
    return id
