class Solution(object):
    def sortJumbled(self, mapping, nums):
        pairs=[]
        for i,n in enumerate(nums):
            mapped_no=0
            base=1
            if n==0:
                mapped_no=mapping[n]
            while n>0:
                digit =n%10
                n=n//10
                mapped_no += base *mapping[digit]
                base *=10
            pairs.append((mapped_no,i))
        pairs.sort()
        return [nums[p[1]] for p in pairs]
            
        
            

        