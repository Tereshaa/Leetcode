class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        
        for courses,preq in prerequisites:
            premap[courses].append(preq)
            
        visited=set()
        def dfs(node):
            if node in visited:
                return False
            if premap[node]==[]:
                return True
            
            visited.add(node)
            for pre in premap[node]:
                if not dfs(pre):
                    return False
            
            
            visited.remove(node)
            premap[node]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        