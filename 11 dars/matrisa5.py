m=4
n=3
q=2

matrix=[]
first_row=[]
for i in range(m):
    son = int(input('son = '))
    first_row.append(son)
matrix.append(first_row)

for i in range(n-1):
    temp2=[]
    for j in range(len(first_row)):
        temp2.append(first_row[j]+q)

    matrix.append(temp2)
    first_row=temp2
print(matrix)