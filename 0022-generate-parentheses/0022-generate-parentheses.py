class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        
        def function(open,close):
            if open==close==n:
                res.append("".join(stack))
            if open<n:
                stack.append("(")
                function(open+1,close)
                stack.pop()
            if close<open:
                stack.append(")")
                function(open,close+1)
                stack.pop()
                
        function(0,0)
        return res