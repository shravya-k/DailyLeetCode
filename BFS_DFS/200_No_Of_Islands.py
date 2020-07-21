class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.cost=0
        def DFS(i,j):
            q=[]
            d1=[-1,1,0,0]
            d2=[0,0,-1,1]
            q.append((i,j))
            grid[i][j]='2'
            while q:
                (i,j)=q.pop()
                for d in range(4):
                    if (i+d1[d] < 0) or j+d2[d] < 0 or i+d1[d]>=len(grid) or j+d2[d]>=len(grid[0]) or grid[i+d1[d]][j+d2[d]]=='0' or grid[i+d1[d]][j+d2[d]]=='2':
                        continue
                    q.append((i+d1[d],j+d2[d]))
                    grid[i+d1[d]][j+d2[d]]='2'
            
            self.cost+=1
            print(grid)
                    
                    
                    
            
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    DFS(i,j)
        return self.cost
        
        
        
