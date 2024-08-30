class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals=defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i+j].append(nums[i][j])
        res=[]
        for key in diagonals.keys():
            res.extend(reversed(diagonals[key]))
        return res
        