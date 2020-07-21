class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board==[] or board==[[]]:
            return board
        def DFS(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='O':
                return
            board[i][j]='T'
            DFS(i+1,j)
            DFS(i,j+1)
            DFS(i-1,j)
            DFS(i,j-1)
        
                
        
        for i in range(len(board)):
            if board[i][0]:
                DFS(i,0)
            if board[i][len(board[0])-1]:
                DFS(i,len(board[0])-1)
        
        for j in range(len(board[0])):
            if board[0][j]:
                DFS(0,j)
            if board[len(board)-1][j]:
                DFS(len(board)-1,j)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
                    
            
