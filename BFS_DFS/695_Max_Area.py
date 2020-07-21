class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def DFS(i,j):
            q=[]
            q.append((i,j))
            d1=[-1,1,0,0]
            d2=[0,0,-1,1]
            cost=1
            grid[i][j]=2
            while q:
                (i,j)=q.pop()
                for d in range(4):
                    if i+d1[d]<0 or j+d2[d]<0 or i+d1[d]>=len(grid) or j+d2[d]>=len(grid[0]) or grid[i+d1[d]][j+d2[d]]!=1:                 
                        continue
                    else:
                        q.append((i+d1[d],j+d2[d]))
                        grid[i+d1[d]][j+d2[d]]=2
                        #print(i,j,'parent')
                        #print(['ch',i+d1[d]],[j+d2[d]])
                        cost+=1
            #print('cost',cost)
            return (cost)
            
            
        
        
        mcnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    mcnt=max(mcnt,DFS(i,j))
        return mcnt
        
        
        
