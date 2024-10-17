class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=collections.defaultdict(list) #a->[b,a/b]
        for i,eq in enumerate(equations):
            a,b=eq
            graph[a].append((b,values[i]))
            graph[b].append((a,1/values[i]))
        
        def bfs(src,target):
            if src not in graph or target not in graph:
                return -1
            q=deque([(src,1)])
            visit=set()
        
            while q:
                n,w=q.popleft()
                if n==target:
                    return w
                for nei,weight in graph[n]:
                            if nei not in visit:
                                q.append([nei,w*weight])
                                visit.add(nei)
            return -1
        return [bfs(q[0],q[1]) for q in queries]
            
        
   