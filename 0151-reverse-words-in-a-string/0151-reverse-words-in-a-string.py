class Solution:
    def reverseWords(self, s: str) -> str:
        str=s.split()
        reversed=str[::-1]
        return " ".join(reversed)
        