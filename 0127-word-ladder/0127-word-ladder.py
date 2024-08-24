class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list=set(wordList)
        if endWord not in word_list:
            return 0
        queue=deque([(beginWord,1)])
        
        while queue:
            word,length=queue.popleft()
            if word==endWord:
                return length
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word=word[:i]+char+word[i+1:]
                    if next_word in word_list:
                        queue.append((next_word,length+1))
                        word_list.remove(next_word)
        return 0
        
            

       