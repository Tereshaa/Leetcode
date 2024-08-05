class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap=[]
        for numberOfBoxes, unitsPerBox in boxTypes:
            heapq.heappush(heap,(- unitsPerBox,numberOfBoxes))
        
        boxes=0
        while heap and truckSize>0:
            unitsPerBox,numberOfBoxes=heapq.heappop(heap)
            if numberOfBoxes<=truckSize:
                boxes+= numberOfBoxes*( -unitsPerBox)
                truckSize -=numberOfBoxes
            else:
                boxes+= -unitsPerBox*truckSize
                truckSize=0
        return boxes
         
    
   