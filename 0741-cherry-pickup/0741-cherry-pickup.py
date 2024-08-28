class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]  
        def helper(r1,c1,c2,n):
            r2=r1+c1-c2
            if(r1>=n or r2>=n or c1>=n or c2>=n or grid[r1][c1]==-1 or grid[r2][c2]==-1):
                return float("-inf")
            if dp[r1][c1][c2]!=-1:
                return dp[r1][c1][c2]
            if(r1==n-1 and c1==n-1):
                return grid[r1][c1]
            ans=grid[r1][c1]
            if r1!=r2:
                ans+=grid[r2][c2]
            temp=max(helper(r1,c1+1,c2+1,n),helper(r1+1,c1,c2+1,n),helper(r1,c1+1,c2,n),helper(r1+1,c1,c2,n))
            ans+=temp
            dp[r1][c1][c2]=ans
            return ans
        return max(0,helper(0,0,0,n))

       