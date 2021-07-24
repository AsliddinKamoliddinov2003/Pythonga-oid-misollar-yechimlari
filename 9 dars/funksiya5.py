def max_juftlik(*sonlar):
    max1=-float('inf')
    max2=-float('inf')
    for son in sonlar:
        if max1<son:
            max1=son
    for son in sonlar:
        if max2<son and son != max1:
            max2=son
    return (max1,max2)


print(max_juftlik(4,5,2,4,8,90,-6))