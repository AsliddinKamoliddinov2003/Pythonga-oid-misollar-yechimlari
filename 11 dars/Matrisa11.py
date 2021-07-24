M=[
[1 ,51, 3, 5],
[7, 7, 9, 19],
[21,17,11,13],
[13,27,15,29]
]

i=0
while i<len(M[0]):
    if i%2==0:
        for j in range(len(M)):
            print(M[i][j])
    else:
        for j in range(len(M)-1,-1,-1):
            print(M[i][j])
    i+=1

