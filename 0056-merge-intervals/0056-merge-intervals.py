class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        merged=[]
        for i in range(n):
            if not merged or intervals[i][0]>merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1]=max(intervals[i][1],merged[-1][1])
        return merged
        
            
        