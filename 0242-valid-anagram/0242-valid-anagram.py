class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #optimal
        if len(s)!=len(t):
            return False
        count_s={}
        count_t={}
        for i in range(len(s)):
            count_s[s[i]]=1+count_s.get(s[i],0)
            count_t[t[i]]=1+count_t.get(t[i],0)
        
        return count_s==count_t
        #brute force
#         def remove_non_alphanumeric(s: str) -> str:
#             return ''.join(c.lower() for c in s if c.isalnum())
        
#         def sort_string(s: str) -> str:
#             return ''.join(sorted(remove_non_alphanumeric(s)))
        
#         return sort_string(s) == sort_string(t)

