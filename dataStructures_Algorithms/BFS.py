from _collections import  deque
def BFS(matrix, i, j, x, y):
    visited = False * matrix
    q = deque
    q.append([i, j, 0])
    visited[i][j] = True
    while q:
        a, b, dist = q.pop()
        if a == x and b == y:
            return dist
        for m in range(4):
            newX, newY = a + m, b + m

            if isValid(matrix, visited, newX, newY):
                visited[newX][newY] = True
                q.append([newX, newY, dist + 1])


def isValid(matrix, visted, i, j):
    if (matrix[i][j] == 1 and visted[i][j] == False and i > 0 and j > 0 and i < len(matrix) and j < len(matrix[0])):
        return True