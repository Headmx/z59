#сделал чтобы работал, когда старт больше стопа, а шаг положительный (будет шаг отнимать), 
# и если старт меньше стопа, а шаг отрицательный (будет шаг отнимать)
def my_range(*args):
    start = 0
    stop = None
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:    
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args [0]
        stop = args [1]
        step = args [2]
    i = start
    num = []
    if i<stop and step>0:    
        while i<stop:
            num.append(i)
            i+=step
    elif i>stop and step>0:
        while i>stop:
            num.append(i)
            i-=step
    elif i>stop and step<0:
        while i>stop:
            num.append(i)
            i+=step
    elif i<stop and step<0:
        while i<stop:
            num.append(i)
            i-=step
    return num
#пример
print (my_range(2,23,-2))
