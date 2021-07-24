n=int(input('n = '))
oxirgi_raqam=0
yig=0
while n>0:
    oxirgi_raqam=n%10
    yig+=oxirgi_raqam
    print(oxirgi_raqam, end=" ")
    n//=10

print(" ")
print(yig)