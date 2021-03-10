# Python3 program to find the longest path in a matrix
# with given constraints

n = 3


def find4direction(mat,i,j,dp):
    #basic condition return
    # already visited then return
    u,v,w,x = -1,-1,-1,-1
    if (j < n-1 and mat[i][j] +1 == mat[i][j+1]):
        u = 1 + find4direction(mat, i, j+1,dp)

    if (j > 0 and mat[i][j]+1 == mat[i][j-1]):
        v = 1+ find4direction(mat,i,j-1,dp)

    if (i < n - 1 and mat[i][j] + 1 == mat[i+1][j]):
        w = 1 + find4direction(mat, i+1, j, dp)

    if (i > 0 and mat[i][j] + 1 == mat[i-1][j]):
        x = 1 + find4direction(mat, i-1, j, dp)
    dp[i][j] =  max(x, max(v, max(u, max(w, 1))))
    return dp[i][j]


# Returns length of the longest path beginning with any cell
def finLongestOverAll(mat):
    result =1
    dp = [[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if dp[i][j]==-1:
                find4direction(mat,i,j,dp)
                result = max(dp[i][j], result)

    result = max



# Driver program
mat = [[1, 2, 9],
       [5, 3, 8],
       [4, 6, 7]]
print("Length of the longest path is ", finLongestOverAll(mat))