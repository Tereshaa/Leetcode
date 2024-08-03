class Solution:
    def frequencySort(self, s: str) -> str:
        frequency={}
        for c in s:
            if c in frequency:
                frequency[c]+=1
            else:
                frequency[c]=1
        max_freq=max(frequency.values())
        buckets=[[] for _ in range(max_freq+1)]
        
        for c,freq in frequency.items():
            buckets[freq].append(c)
        
        res=[]
        for freq in range(max_freq,0,-1):
            for char in buckets[freq]:
                res.append(char*freq)
        return "".join(res)
 
        
      
        