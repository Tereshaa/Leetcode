class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        c1=0
        c2=0
        count=0
        while c1<m and c2<n:
            if arr1[count]>arr2[c2]:
                for i in range(m+n-1,count,-1):
                    arr1[i]=arr1[i-1]
                arr1[count]=arr2[c2]
                c2=c2+1
                count=count+1
            else:
                count=count+1
                c1=c1+1
        while c2<n:
            for i in range(m+n-1,count,-1):
                arr1[i]=arr1[i-1]
            arr1[count]=arr2[c2]
            c2=c2+1
            count=count+1
      
 