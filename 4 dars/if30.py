x=int(input("x = "))
if (x>9 and x<100 and x%2==0):
    print(f" 2 xonali juft son ") 
elif (x>0 and x<10 and x%2==0):
    print(f'1 xonali juft son')
elif (x>0 and x<10 and x%2==1):
    print(f'1 xonali toq son')
elif (x>9 and x<100 and x%2==1):
    print(f"2 xonali toq son")
elif (x<=100 and x<1000 and x%2==0):
    print(f"3 xonali juft son")
elif (x<=100 and x<1000 and x%2==1):
    print(f"3 xonali toq son")
elif x==0:
    print(f"son nolga teng")