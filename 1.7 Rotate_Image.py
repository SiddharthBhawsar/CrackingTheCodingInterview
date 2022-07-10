a=[[1,2,3],[4,5,6],[7,8,9]]
emp=np.zeros(3,3)
for i in range(3):
    for j in range(3):
        emp[j][i]=a[2-i][j]
      
print (emp)

