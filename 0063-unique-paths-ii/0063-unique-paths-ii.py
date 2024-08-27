class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1:
            return 0
        dp=[[-1 for _ in range(cols)] for _ in range(rows) ]
        for i in range(rows):
            for j in range(cols):
                if i>=0 and j>=0 and obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    fup=dp[i-1][j] if i>0 else 0
                    fleft=dp[i][j-1] if j>0 else 0
                    dp[i][j]=fup+fleft
        return dp[rows-1][cols-1]
        