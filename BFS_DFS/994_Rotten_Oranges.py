class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def DFS(q):
            while q:
                (i,j,cost) = q.pop(0)
                d1=[-1,1,0,0]
                d2=[0,0,-1,1]
                for d in range(4):
                    if (i+d1[d]<0) or (i+d1[d]>=len(grid)) or (j+d2[d]<0) or (j+d2[d]>=len(grid[0])) or (grid[i+d1[d]][j+d2[d]]!=1):
                        continue
                    grid[i+d1[d]][j+d2[d]]=2
                    q.append((i+d1[d],j+d2[d],cost+1))
            return cost
        
        
        
        q=[]
        cost=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
        
        print(q)
        
                    
        for i in grid:
            if 1 in i:
                return -1
        return cost
        
                        
                
                
                
