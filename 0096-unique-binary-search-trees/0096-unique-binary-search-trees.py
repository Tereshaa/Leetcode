class Solution:
    def numTrees(self, n: int) -> int:
        numtree=[1]*(n+1)
        #0 nodes - 1 tree
        #1 nodes - 1 tree
        for i in range(2,n+1):
            total=0
            for root in range(1,i+1):
                left=root-1
                right=i-root
                total+=numtree[left]*numtree[right]
            numtree[i]=total
        return numtree[n]
            
        