class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize !=0:
            return False
        
        count={}
        for n in hand:
            count[n]=1+count.get(n,0)
        
        minh=list(count.keys())
        heapq.heapify(minh)
        
        while minh:
            first=minh[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i]==0:
                    if i!=minh[0]:
                        return False
                    heapq.heappop(minh)
        return True

       