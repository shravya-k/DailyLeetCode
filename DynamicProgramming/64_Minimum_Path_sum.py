class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((0<=i-1<len(grid)) and (0<=j<len(grid[0]))) and ((0<=i<len(grid)) and (0<=j-1<len(grid[0]))):
                    grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
                 
                if ((0<=i-1<len(grid)) and (0<=j<len(grid[0]))) and (not ((0<=i<len(grid)) and (0<=j-1<len(grid[0])))):
                    grid[i][j]=grid[i][j]+ grid[i-1][j]
                    
                if  (not (((0<=i-1<len(grid)) and (0<=j<len(grid[0]))))) and ((0<=i<len(grid)) and (0<=j-1<len(grid[0]))):
                    grid[i][j]= grid[i][j]+ grid[i][j-1]
                
        if len(grid)-1 >=0 and len(grid[0])-1 >=0:
            return(grid[len(grid)-1][len(grid[0])-1])
        else:
            return 0
                
                
                 
        
