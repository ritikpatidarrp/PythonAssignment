class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def checkIfSurroundedByX(i,j,board,vis):
            if i<0 or j<0 or i==len(board) or j==len(board[0]):
                return False
            if board[i][j]=='X':
                return True
            if vis[i][j]==True:
                return True
            vis[i][j] = True
            ans = checkIfSurroundedByX(i-1,j,board,vis) 
            ans = ans and checkIfSurroundedByX(i+1,j,board,vis) 
            ans = ans and checkIfSurroundedByX(i,j-1,board,vis) 
            ans = ans and checkIfSurroundedByX(i,j+1,board,vis)
            return ans
        
        def markXtheComponent(i,j,board):
            if board[i][j]=='X':
                return
            board[i][j] = 'X'
            markXtheComponent(i-1,j,board)
            markXtheComponent(i+1,j,board)
            markXtheComponent(i,j-1,board)
            markXtheComponent(i,j+1,board)
        
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j]=='O':
                    vis = [[False]*len(board[0]) for _ in range(0,len(board))]
                    # if the component is surrounded by X then mark whole component to X
                    if checkIfSurroundedByX(i,j,board,vis):
                        markXtheComponent(i,j,board)
        


        
