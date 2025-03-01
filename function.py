import os
FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH,'w'):
        pass

def get_todos(filepath = FILEPATH):
    """
    Read the text file and return the list of to-do items
    """
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def send_todos(todos, filepath = FILEPATH):
    """
    Writes the todos list into the todos.txt file
    """
    with open(filepath,'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    """
    This code is only executed if the current file is run and not when it is imported
    """
    print("Hello")
    print(get_todos())

