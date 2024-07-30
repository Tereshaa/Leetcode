class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right=0
        for c in s:
            if c=='a':
                a_right +=1
           
            
        b_left=0
        res=len(s)
        for c in s:
            if c=="a":
                a_right -=1
            deletions = b_left+a_right
            res=min(res,deletions)
            if c=="b":
                b_left +=1
        return res
    