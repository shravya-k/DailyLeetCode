class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] or grid[-1][-1]:
            return -1
        if len(grid)==0 or len(grid)==1:
            return len(grid)
        q=[]
        q.append((0,0,1))
        grid[0][0]=1
        d1=[-1,1,0,0,-1,-1,1,1]
        d2=[0,0,-1,1,-1,1,-1,1]
        
        while q:
            (i,j,cost)=q.pop(0)
            
            for d in range((8)):
                if i==len(grid)-1 and j==len(grid[0])-1:
                    return cost
                if i+d1[d]<0 or i+d1[d]>=len(grid) or j+d2[d]<0 or j+d2[d]>=len(grid[0]) or grid[i+d1[d]][j+d2[d]]==1:
                    continue
                
                grid[i+d1[d]][j+d2[d]]=1
                q.append((i+d1[d],j+d2[d],cost+1))
                
      
        return -1            
        
