class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        
        for course,preq in prerequisites:
            premap[course].append(preq)
        
        order=[]
        visit=set()
        cycle=set()
        
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for pre in premap[node]:
                if not dfs(pre):
                    return False
            cycle.remove(node)
            visit.add(node)
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
            
        
            
        