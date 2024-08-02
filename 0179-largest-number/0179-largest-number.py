class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
        def compare(x,y):
            if x+y>y+x:
                return -1
            elif x+y<y+x:
                return 1
            else:
                return 0
            
        nums.sort(key=cmp_to_key(compare))
        res= "".join(nums)
        return '0' if res[0] == '0' else res
        