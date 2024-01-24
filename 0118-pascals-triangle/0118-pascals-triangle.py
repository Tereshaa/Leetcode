class Solution:
    
    @staticmethod
    def ncr(n,r):
        com=1
        for i in range(r):
            com=com*(n-i)
            com=com//(i+1)
        return com
    
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        ans=[]
        for i in range(n):
            temp=[]
            for j in range(i+1):
                temp.append(self.ncr(i,j))
            ans.append(temp)
        return ans
        