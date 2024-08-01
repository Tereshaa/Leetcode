class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for s in details:
            age=s[11]+s[12]
            if int(age)>60:
                res+=1
        return res
        