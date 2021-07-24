m=[[1,2,3,5,3],[4,5,6,8,6],[7,8,9,2,1]]

row_index=len(m)-1
col_index=0

while 0<=row_index and col_index<len(m[0]):
    for row in m[:row_index+1]:
        print(row[col_index], end=' ')
    col_index+=1

    for e in m[row_index][col_index:]:
        print(e, end=' ')
    row_index+=1