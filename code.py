class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def checkIfSurroundedByX(i,j,board,vis):
            # Base case: if the position is out of bounds or already visited, return False
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
                return False
            # If the current position contains 'X', it is surrounded
            if board[i][j] == 'X':
                return True
            # If the position has already been visited, return True to avoid redundant checks
            if vis[i][j] == True:
                return True
            # Mark the position as visited
            vis[i][j] = True
            # Recursively check the neighbors in all four directions
            ans = checkIfSurroundedByX(i-1, j, board, vis) 
            ans = ans and checkIfSurroundedByX(i+1, j, board, vis) 
            ans = ans and checkIfSurroundedByX(i, j-1, board, vis) 
            ans = ans and checkIfSurroundedByX(i, j+1, board, vis)
            return ans
        
        def markXtheComponent(i,j,board):
            # Base case: if the current position contains 'X', do nothing
            if board[i][j] == 'X':
                return
            # Mark the current position as 'X'
            board[i][j] = 'X'
            # Recursively mark the neighbors in all four directions
            markXtheComponent(i-1, j, board)
            markXtheComponent(i+1, j, board)
            markXtheComponent(i, j-1, board)
            markXtheComponent(i, j+1, board)
        
        # Iterate through each cell in the given board.
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                # For each 'O' cell, check if the connected component starting from that cell is surrounded by 'X' using the checkIfSurroundedByX function.
                if board[i][j]=='O':
                    vis = [[False]*len(board[0]) for _ in range(0,len(board))]
                    # If the component is surrounded, mark the entire component to 'X' using the markXtheComponent function.
                    if checkIfSurroundedByX(i,j,board,vis):
                        markXtheComponent(i,j,board)
