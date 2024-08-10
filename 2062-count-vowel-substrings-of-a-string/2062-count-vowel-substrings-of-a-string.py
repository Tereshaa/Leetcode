class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=set('aeiou')
        count=0
        start=0
        while start<len(word):
            if word[start] not in vowels: 
                start+=1
                continue
            end=start
            seen_vowels=set()
            while end<len(word) and word[end] in vowels:
                seen_vowels.add(word[end])
                if len(seen_vowels)==5:
                    count+=1
                end+=1
            start+=1
        return count
            
