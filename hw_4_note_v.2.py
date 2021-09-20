print ('Записная приветствует Вас')
import json
todos = {}

def strike(text):
    result = ''
    for c in text:
        result += '\u0336'+c
    return result

def strike_todo():
    while True:
        number = input ('какой номер задачи отмечаем:\n ')
        text = todos[number] 
        todos[number] = strike(text)
        y = input('желаете продолжить? (y/n) ')
        if y in ('y', 'Y'):
            continue
        else:
            break
    return print_todos()

def strike_all ():
    while True:
        for key in todos:
            text = todos[key] 
            todos[key] = strike(text)
        else:
            break
    return print_todos()

def valid_number (number):
    return number.isdigit() and 0<int(number)<= len(todos)

def add_todo():
    while True:
        todo = input('Введите задачу:')
        i = str(len(todos) + 1)
        todos[i] = todo
        y = input('желаете продолжить? (y/n) ')
        if y in ('y', 'Y'):
            continue
        else:
            break
    return print_todos()

def del_todo ():
    while len(todos):
        print_todos ()
        number = input ('введите номер задачи:')
        todos.pop(number)        
        y = input('желаете продолжить? (y/n) ')
        if y in ('y', 'Y'):
            continue
        else:
            break
    return print_todos()

def print_todos():
    global todos
    for key, value in todos.items(): 
        print (key,  value)
    return 

def update_todo():
    while True:
        print_todos ()
        number = input ('введите номер задачи:')
        if number not in todos.keys():
            print (' нет такого номера, пробуйте еще:\n')
            continue
        else:
            text = input ('введите новую задачу:\n')
            todos[number] = text    
            y = input('желаете продолжить? (y/n) ')
            if y in ('y', 'Y'):
                continue
            return 

def filter_todos(text):
    d = {key: value for key, value in todos.items() if text in value['text']}
    return list(d)

def open_todos():
    add_file = input('введите имя файла своей todo, или n:')
    if add_file in ('N','n','No','no','NO', False, ''):
        global todos
        with open ('my_todo.json', 'r') as todos_json:
            todos = json.load(todos_json)
    else:
        with open (f'{add_file}', 'r') as todos_json:
            todos = json.load(todos_json)
    return print_todos

def save_todos():
    save_file = input('в какой файл сохраняем')
    if save_file in ('N','n','No','no','NO', False, ''):
        with open('my_todo.json', 'w') as todos_json:
            json.dump(todos,todos_json)
            return print ('Saved in my_todos.json' )
    else:
        with open(f'{save_file}', 'w') as todos_json:
            json.dump(todos,todos_json)
            return print (f'Saved in {save_file}' )
    

def all_del_todos():
    y = input('точно удаляем? (y/n) ')
    if y in ('y', 'Y'):
        todos.clear()
      
    
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

open_todos()
while True:
    choice = input(menu)
    if choice == '1':
        print_todos()
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
        all_del_todos()
    elif choice == '9':
        text = input ('что ищем? \n:')
        filter_todos(text)     
    elif choice == '0':
        save_todos()
        print ("Goodbye!")
        break
    else:
        print (' нет такого номера, пробуйте еще!\n')
        continue

    