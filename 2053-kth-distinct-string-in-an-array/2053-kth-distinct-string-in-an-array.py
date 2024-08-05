class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        for c in arr:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        for c in arr:
            if c in freq:
                if freq[c]==1:
                    k-=1
                if k==0:
                    return c
        else:
            return ""

            
            