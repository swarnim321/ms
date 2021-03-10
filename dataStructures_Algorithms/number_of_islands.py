from collections import deque


def dfs(mat):
    count=0
    for i in range(row):
        for j in range(col):
            if mat[i][j]==1:
                count+=1
                ishelperdfs(i,j,mat)
    print(count)

def ishelperdfs(x,y,mat):
    if x>row or x<0 or y>col or y<0:
        return
    mat[x][y]=2
    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
        newx,newy=x+dx,y+dy
        ishelperdfs(newx,newy,mat)


def bfs(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0
    q = deque

    for i in range(row):

        for j in range(col):

            if grid[i][j] == "1":
                count += 1
                q.append([i,j])
                print(count)
                while q:
                    x, y = q.popleft()
                    print(x,y)
                    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        newx, newy = x + dx, y + dy
                        if newx<=row and newx>=0 and newy<=col and newy>=0 and grid[newx][newy]==1:
                            grid[newx][newy] = 2
                            q.append(newx, newy)
    print (count)

mat=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
row=len(mat)
col=len(mat[0])
bfs(mat)
