print ('Калькулятор приветсвует Вас!')
a = 1
while a == 1 :
    number1 = float(input('введите 1 число: '))
    number2 = float (input('введите 2 число: '))
    operation = input('что будем делать(+/-*)? ')
    if operation == '/' and number2 == 0:
        print ('на ноль делить нельзя!')
    elif operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print ('Этого делать мы не умеем пока, используйте */-+')
        continue  
    elif operation == '-':
        print (number1 - number2)
    elif operation == '+':
        print (number1 + number2)
    elif operation == '/':
        print (number1 / number2)
    elif operation == '*':
        print (number1 * number2)
    question = input ('продолжаем y/n ? ')
    if question == 'y':
        continue
    else:
        print ('до свидания')
        break    
else:
    print ('что-то не то')
   