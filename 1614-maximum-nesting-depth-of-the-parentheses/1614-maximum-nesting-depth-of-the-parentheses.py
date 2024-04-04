class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxi = 0
        for i in s:
            if i=='(':
                count=count+1
                maxi=max(maxi,count)
            elif i==')':
                count=count-1
        return maxi
                