list_up='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
list_low='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
list = ()
text = '''
\n1. увеличить регистр
\n2. уменьшить регистр
\n3. заменить символ в строке
\n4. сделать первую букву заглавной
\n5. разбить строку пробелами
\n6. соединить все элементы в строке
\n7. заменить элемент в строке
\n8. выход
'''
list_add=input('Введите строку:')
change = input(text)
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

if change == '1':
    print(upper(list_add))   
if change == '2':
    print(lower(list_add))
if change == '3':
    print(changer(list_add, input('что меняем:'), input('на что меняем:'), int(input('сколько раз:'))))
