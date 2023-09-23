def get_todos():
    with open("todos.txt", "r") as fileLocal:
        todos1 = fileLocal.readlines()
    return todos1


def write_todos(todos_local):
    with open("todos.txt", 'w') as fileLocal:
        fileLocal.writelines(todos_local)

