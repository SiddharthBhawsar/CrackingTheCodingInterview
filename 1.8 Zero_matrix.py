def x(a):
    m=len(a)
    n=len(a[0])
    rows=set()
    col=set()
    for i in range(m):
        for j in range(n):
            if (a[i][j]==0):
                rows.add(i)
                col.add(j)
    for i in (rows):
        for j in range(n):
            a[i][j]=0
    for j in (col):
        for i in range(m):
            a[i][j]=0
    print(a)
    return a            
    
a=x([[1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25]])
print (a)
