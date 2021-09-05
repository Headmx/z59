print ('Непонятная программа приветствует Вас!')
list1 = input('введите список:')
while 1 : 
    operation = input('Выберите действие, которые вы хотите выолнить (0,1,2,3,4,5,6,7) \n0. выйти из программы \n1. добавить значение в список  \n2. замена значения в строке \n3. сделать все буквы в строке заглавными \n4. сделать все буквы строчными \n5. сделать первую букву заглавной  \n6. вывеси строку на экран \n7. посчитать количество символов в строке \n:')
    if  operation.isdigit() and '0'<=operation<='7':
        if operation == '0':
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue  
        elif operation == '1':
            list2 =input('введите значение:')
            list1 = list1+list2
            print (list1)
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue  
        elif operation == '2':
            a = input('введите какое значение хотите заменить:')
            b = input ('на какое значение хотите заменить:')
            list3 = list1.replace(a,b)
            list1=list3
            print(list1)
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue  
        elif operation == '3':
            list4=list1.upper()
            list1=list4
            print(list1)
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue  
        elif operation == '4':
            list5=list1.lower()
            list1=list5
            print(list1)
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue  
        elif operation == '5':
            list6 = list1.capitalize()
            list1=list6
            print (list6)
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue
        elif operation == '6':
            print (list1)
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue
        elif operation == '7':
            print(len(list1))
            question = input('вы желаете выйти ? (y/n)')
            if question == 'y':
                print('До свидания.')
                break
            elif question == 'n':
                continue
    else:
        print ('НЕККОРЕКТНОЕ ЗНАЧЕНИЕ, ВВОДИТЕ ЦИФРЫ ОТ 0 ДО 6')
        continue
     
