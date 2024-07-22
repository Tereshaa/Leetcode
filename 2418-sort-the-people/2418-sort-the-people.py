class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap={}
        for h,n in zip(heights,names):
            hashmap[h]=n

        res=[]
        for h in reversed(sorted(heights)):
            res.append(hashmap[h])
        return res
            
        