class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count=defaultdict(int)
        for n1,n2 in zip(target,arr):
            count[n1]+=1
            count[n2]-=1
        for n in count:
            if count[n]!=0:
                return False
        return True
        
        