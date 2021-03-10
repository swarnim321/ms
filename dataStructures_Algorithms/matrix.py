row=int(input("enter the number of columns"))
col=int(input("enter the number of rows"))

mat1=[[]for j in range(col)]
print(mat1)
for i in range(row):
    for j in range(col):
        mat1[j].append(int(input("enter the entries column wise")))

row2=int(input("enter the number of columns"))
col2=int(input("enter the number of rows"))

mat2=[[]for j in range(col2)]

for i in range(row2):
    for j in range(col2):
        mat2[j].append(int(input("enter the entries column wise")))

print(mat1)
print(mat2)

result=[[0 for x in range (len(mat1))]for y in range(len(mat2[0]))]
for i in range(len(mat1)):
    for j in range (len(mat2[0])):
        for k in range(len(mat2)):

            result[i][j]+=mat1[i][k]*mat2[k][j]
print(result)





