class Solution:
    import collections
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dis={j:float('inf') for j in range(1,N+1)}
        graph=collections.defaultdict(list)
        
        for src,dsn,cost, in times:
            graph[src].append([dsn,cost])
        
        def DFS(node,cost):
            if dis[node]<cost:
                return
            dis[node]=cost
            for nei,c in graph[node]:
                DFS(nei,cost+c)
                
        
            
        DFS(K,0)
        print(dis)         
        return -1 if max(dis.values())==float('inf') else max(dis.values())
    
    
    
