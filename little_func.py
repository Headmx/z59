import string
def sum_recursive(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_recursive(list[1:]) 
    
print (sum_recursive([11,2,12,8,2]))

def level_rec(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * level_rec(x,y-1)

print (level_rec(2,5))

def sum_number_rec (number):
    number = str(number)
    if len(number) == 1:
        return number[0]
    else:
        return int(number[0])+int(sum_number_rec(number[1:]))

print(sum_number_rec(input('write number:')))

def negatives_rec(string1):
    count = 0
    if string1 == []:
        return 0    
    if string1[0]<0:
        count = count +1
    return count + negatives_rec(string1[1:])
    
print (negatives_rec([-5,-5,2,33,-7,0,-9,123,798,-88]))

def is_prime (number):
    for i in range(2,int(delitel**0,2) +1):
        if number%i == 0:
            return False
        return True

def in_prime_rec (number, delitel):
    if number == 2 or delitel >= number**0.5:
        return True
    if number % 2 == 0:
        return False
    if number % delitel == 0:
        return False
    return in_prime_rec (number, delitel+2)

print (in_prime_rec(997,5))



