print ('Калькулятор приветсвует Вас!')
question = 'y'
while question == 'y' :
    number1 = float(input(' '))
    operation = input(' ')
    while True:
        number2 = float (input(' '))
        if operation == '/' and number2 == 0:
            print ('на ноль делить нельзя!')
            break
        elif operation != '+' and operation != '-' and operation != '*' and operation != '/':
            print ('Этого делать мы не умеем пока, используйте */-+')
            break  
        elif operation == '-':
            temporary = number1 - number2
        elif operation == '+':
            temporary = number1 + number2
        elif operation == '/':
            temporary = number1 / number2
        elif operation == '*':
            temporary = number1 * number2
        operation = input ('')
        if operation == '=':
            print (temporary)
            break
        else:
            number1 = temporary
            continue    
    question = input ('продолжаем y/n ? ')
    if question == 'y':
        continue
    else:
        print ('до свидания')
        break    

   