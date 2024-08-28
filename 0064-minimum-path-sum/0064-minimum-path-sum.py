class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    fup=grid[i][j]
                    if i>0:
                        fup+=dp[i-1][j]
                    else:
                        fup+=float("inf")
                    fleft=grid[i][j]
                    if j>0:
                        fleft+=dp[i][j-1]
                    else:
                        fleft+=float("inf")
    
                    dp[i][j]=min(fup,fleft)
        return dp[rows-1][cols-1]