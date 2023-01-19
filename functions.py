FILEPATH = 'todos.txt'  # define value of variable at top of module. Capital letters. Constant


def get_todos(filepath=FILEPATH):  # when u define function, what's inside () is parameter/argument
    """Read a txt file and return
    the list of to-do items.
    """
    with open(filepath, 'r') as file_local:  # by default file opens in read more. ‘r’ not necessary
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the txt file."""
    with open(filepath, 'w') as file_local:  # we don't need  value from it
        file_local.writelines(todos_arg)  # # func does not return anything. func goes somewhere and performs task.
