class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        low=0
        high=row-1

        while low<=high:
            mid=(low+high)//2
            
            if target> matrix[mid][-1]:
                low=mid+1
            elif target<matrix[mid][0]:
                high=mid-1
            else:
                break
        if not (low<=high):
            return False
        mid=(low+high)//2
        l=0
        r=col-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[mid][m]:
                l=m+1
            elif target<matrix[mid][m]:
                r=m-1
            else:
                return True
        return False
                
            
            
 
