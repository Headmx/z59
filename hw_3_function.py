list_up=' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_low=' абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
list = ()
question = 'y'
text = '''
\n1. увеличить регистр
\n2. уменьшить регистр
\n3. заменить элемент в строке
\n4. сделать первую букву заглавной
\n5. каждое слово с заглавной сделать
\n6. соединить все элементы в строке
\n7. выход
'''
list_add=input('Введите строку:')

def upper(list):
    new_list=''
    i=0
    for i in range(len(list)):
        if list[i] in list_low:
            new_index = list_low.index(list[i])
            new_list=new_list + list_up[new_index]
            i+=1
            continue
        else:
            new_list = new_list + list[i]
            i+=1   
            continue
    return new_list
def lower(list):
    new_list=''
    i=0
    for i in range(len(list)):
        if list[i] in list_up:
            new_index = list_up.index(list[i])
            new_list=new_list + list_low[new_index]
            i+=1
            continue
        else:
            new_list = new_list + list[i]
            i+=1   
            continue
    return new_list
def changer(list, value1,value2,all_number):
    new_list = ''
    i=0
    number = 0
    for i in range(len(list)):
        if list[i] == value1:
            while int(number) < int(all_number):
                new_list = new_list + value2
                i+=1
                number +=1
                break
            else:
                new_list = new_list + list[i]
                i+=1   
                continue
        else:
            new_list = new_list + list[i]
            i+=1   
            continue
    return new_list
def questioner():
    z=input('делаем еще чего? (y/n):')
    return z
def one_up(list):
    new_list = ''
    i = 0
    for i in range(len(list)):
        if list[i] in list_low:
            if i == 0:
                new_index = list_low.index(list[0])
                new_list=new_list + list_up[new_index]
                i+=1
                continue
            new_list = new_list + list[i]
            i+=1   
            continue
    return new_list
def new_word_up(list):
    new_list = ''
    i = 0
    for i in range(len(list)):
        if list[i] in list_low:
            if i == 0:
                new_index = list_low.index(list[0])
                new_list=new_list + list_up[new_index]
                i+=1
                continue
            elif list[i] == ' ':
                new_list = new_list + list[i]
                new_index = list_low.index(list[i+1])
                new_list=new_list + list_up[new_index]
                i+=1
            new_list = new_list + list[i]
            i+=1   
            continue
    return new_list
def elem_merge(list):
    new_list = ''
    i = 0
    for i in range(len(list)):
        if list[i] in list_low:
            if list[i] == " ":
                i+=1
                continue
            new_list = new_list + list[i]
            i+=1   
            continue
    return new_list

while  question == 'y' :
    change = input(text)
    if change == '1':
        print(upper(list_add))   
    if change == '2':
        print(lower(list_add))
    if change == '3':
        print(changer(list_add, input('что меняем:'), input('на что меняем:'), int(input('сколько раз:'))))
    if change == '4':
        print(one_up(list_add))
    if change == '5':
        print(new_word_up(list_add))
    if change == '6':
        print(elem_merge(list_add))
    if change == '7':
        print ('Goodbye!')
        break
    if 1>int(change) or int(change)>7:
        print ('Нет такого значения!!! попробуйте еще раз:')
        continue
    question = questioner() 
else:
    print ('Goodbye!')
    exit