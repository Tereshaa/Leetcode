class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total_sum=sum(cardPoints)
        if n==k:
            return total_sum
        window=n-k
        window_sum=sum(cardPoints[:window])
        current_sum=window_sum
        
        for i in range(window,n):
            current_sum+=cardPoints[i]-cardPoints[i-window]
            window_sum=min(current_sum,window_sum)
        return total_sum-window_sum
        