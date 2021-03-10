def anti_diagonal(mat):
    m=len(mat)
    n=len(mat[0])
    for col in range(m):
        startcol=col
        startrow=0
        while startcol>=0 and startrow<m:

            print(mat[startrow][startcol], end=" ")
            startrow+=1
            startcol-=1

        print()

    for i in range(1,n):
        startrow=i
        startcol=n-1
        while startrow<n and startcol>=0:
            print(mat[startrow][startcol], end=" ")
            startrow += 1
            startcol -= 1
        print()

def diagonal(mat):
    m = len(mat)
    n = len(mat[0])

    for i in range(m,0,-1):
        startrow=0
        startcol=i
        while startrow>=0 and startcol<n:
            #print("index ", startrow,startcol)
            print(mat[startrow][startcol], end=" ")
            startrow += 1
            startcol += 1
        print()

    m = len(mat)
    n = len(mat[0])
    for i in range(n):
            startrow = i
            startcol =0
            while startrow< n and startcol<n:
                print(mat[startrow][startcol], end=" ")
                startrow+=1
                startcol+=1
            print()





mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

anti_diagonal(mat)
print("    ")
diagonal(mat)