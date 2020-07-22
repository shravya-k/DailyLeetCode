class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat=[[1 for i in range(m)] for j in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if 0<=(i-1)<n and 0<=(j-1)<m:
                    mat[i][j]=mat[i-1][j]+mat[i][j-1]
                elif 0<=(i-1)<n:
                    mat[i][j]=mat[i-1][j]
                elif 0<=(j-1)<m:
                    mat[i][j]=mat[i][j-1]
                
                
                
        
