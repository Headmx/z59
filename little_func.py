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

# пока не понял как сделать 
def negatives_rec(list):
    count = 0
    if len(list) == 1:
        if int(list[0]) < 0:
            count = count +1
            return count
        else:
            return count
    else:
        return count + negatives_rec([list[1:]])
    
#print (negatives_rec([1,-5,2,33,-7,0,-9,123,798,-88]))






