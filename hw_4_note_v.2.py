print ('Записная приветствует Вас')
todos = {}

def strike(text):
    result = ''
    for c in text:
        result += '\u0336'+c
    return result

def strike_todo():
    while True:
        number = int(input ('какой номер задачи отмечаем:\n '))
        text = todos[number] 
        todos[number] = strike(text)
        y = input('желаете продолжить? (y/n) ')
        if y in ('y', 'Y'):
            continue
        else:
            break
    return print_todos(todos)

def strike_all ():
    while True:
        for key in todos:
            text = todos[key] 
            todos[key] = strike(text)
        else:
            break
    return print_todos(todos)

def valid_number (number):
    return number.isdigit() and 0<int(number)<= len(todos)

def add_todo():
    while True:
        todo = input('Введите задачу:')
        i = len(todos) + 1
        todos[i] = todo
        y = input('желаете продолжить? (y/n) ')
        if y in ('y', 'Y'):
            continue
        else:
            break
    return print_todos(todos)

def del_todo ():
    while len(todos):
        print_todos (todos)
        number = int(input ('введите номер задачи:'))
        todos.pop(number)
        y = input('желаете продолжить? (y/n) ')
        if y in ('y', 'Y'):
            continue
        else:
            break
    return print_todos(todos)

def print_todos(dict_1):
    for key, value in dict_1.items(): 
        print (key,  value)
    return 

def update_todo():
    while True:
        print_todos (todos)
        number = input ('введите номер задачи:')
        if not valid_number (number):
            print (' нет такого номера, пробуйте еще:\n')
            continue
        else:
            text = input ('введите новую задачу:\n')
            todos[int(number)] = text    
            y = input('желаете продолжить? (y/n) ')
            if y in ('y', 'Y'):
                continue
            return 

def filter_todos(text):
    return filter(lambda x: text in x ['text'], todos)
        
        
        



menu = '''
1. посмотреть задачи
2. добавить задачу
3. удалить задачу
4. обновить задачу
5. отметить задачу
6. отметить все задачи
7. удалить все выделенные задачи
8. удалить все
9. поиск задач по слову
0. выйти
''' 


while True:
    choice = input(menu)
    if choice == '1':
        print_todos(todos)
    elif choice == '2':
        add_todo()
    elif choice == '3':
        del_todo()
    elif choice == '4':
        update_todo()
    elif choice == '5':
        strike_todo()
    elif choice == '6':
        strike_all()        
    elif choice == '7':
        break
    elif choice == '8':
        todos.clear()
        continue
    elif choice == '9':
        text = input ('что ищем? \n:')
        a = filter (filter_todos,todos)
        print (list (a))
    elif choice == '0':
        print ("Goodbye!")
        break
    else:
        print (' нет такого номера, пробуйте еще!\n')
        continue

    