class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removepair(pair,score):
            nonlocal s
            
            result=0
            stack=[]
            for c in s:
                if c==pair[1] and stack and stack[-1]==pair[0]:
                    stack.pop()
                    result=result+score
                else:
                    stack.append(c)
            s="".join(stack)
            return result
        
        res=0
        pair="ab" if x>y else "ba"
        res=res+ removepair(pair,max(x,y))
        res=res+removepair(pair[::-1],min(x,y))
        return res