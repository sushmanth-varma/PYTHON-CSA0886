def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 - obstacleGrid[0][0]
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0: dp[i][j] += dp[i-1][j]
                if j > 0: dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]
print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles([[0, 1], [0, 0]]))


#####
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    for i in range(1, m): grid[i][0] += grid[i-1][0]
    for j in range(1, n): grid[0][j] += grid[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[-1][-1]
print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])) 
print(minPathSum([[1, 2, 3], [4, 5, 6]]))  


######
def simplifyPath(path):
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack: stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)
print(simplifyPath("/home/"))  
print(simplifyPath("/home//foo/"))
#####
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[i + j for j in range(n + 1)] for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    return dp[-1][-1]
print(minDistance("horse", "ros")) 
print(minDistance("intention", "execution"))

######
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero, col_zero = set(), set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0

# Test cases
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(matrix1)
print(matrix1)  

matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix2)
print(matrix2)  
