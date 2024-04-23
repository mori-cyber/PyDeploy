def justforfun():
    yield 1
    yield 2
    yield 3
    

for value in justforfun():
    print(value)

def Sqare():
    i=1

    while True:
        yield i*i # this is for run the functuion and contenue that but return run function without countenue that. 
        i+=1

for num in Sqare():
    print(num)

    if num>100:
        break