class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        if not grid:
            return
        
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                return
            grid[r][c]="*"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][cols-1]==1:
                dfs(i,cols-1)
                
        for i in range(cols):
            if grid[0][i]==1:
                dfs(0,i)
            if grid[rows-1][i]==1:
                dfs(rows-1,i)
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                   
                    count+=1
        return count
                
        