class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        stk = []
        numIsl = 0
        for k in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[k][j] == '1':
                    grid = dfs(k,j, grid)
                    numIsl += 1
        return numIsl

def dfs(r,c, grid):
    nr = len(grid)
    nc = len(grid[0])
        
    if (r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == "0"):
        return
    
    grid[r][c] = '0'
    dfs(r-1, c, grid)
    dfs(r+1, c, grid)
    dfs(r, c-1, grid)
    dfs(r, c+1, grid)
    return grid