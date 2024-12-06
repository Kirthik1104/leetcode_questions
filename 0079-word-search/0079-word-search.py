class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
ime Complexity:
\U0001d442(\U0001d440⋅\U0001d441⋅4\U0001d43f)

M,N: Grid dimensions.

4\U0001d43f: Each cell has up to 4 neighbors, and \U0001d43f is the word length.
        """
        
        rows=len(board)
        columns=len(board[0])
        visited=set()

        #Edge case : 1 char

        if rows == 1 and columns ==1:
            return board[0][0]==word[:]

        def dfs(x, y, index):
            if index==len(word):
                return True
            
            if (x<0 or y<0 or x>=rows or y>=columns or board[x][y]!=word[index] or (x,y) in visited):
                return False
            
            visited.add((x,y))

            res = (dfs(x+1, y, index+1) or
                   dfs(x-1, y, index+1) or 
                   dfs(x, y+1, index+1) or
                   dfs(x, y-1, index+1))
            
            visited.remove((x,y))

            return res

        for row in range(rows):
            for col in range(columns):
                if board[row][col]==word[0]:
                    if dfs(row, col, 0):
                        return True
        return False