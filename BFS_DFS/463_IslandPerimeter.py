class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
            
        self.cost=0 
        
        q=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    d1=[-1,1,0,0]
                    d2=[0,0,-1,1]
                    o=0
                    for d in range(4):
                        if (i+d1[d])<0 or (j+d2[d])<0 or (i+d1[d])>=len(grid) or (j+d2[d])>=len(grid[0]):
                            continue
                        else:
                            if grid[i+d1[d]][j+d2[d]]==1:
                                o+=1
                    self.cost+=(4-o)
                    
        return self.cost            
                    
         
        
