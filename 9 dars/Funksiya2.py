def func2(*number):
    _sum=0
    t=0
    for i in number:
        _sum += i
        t+=1
    return(_sum,t)
    
print(func2(1,2,3,4,5))    




