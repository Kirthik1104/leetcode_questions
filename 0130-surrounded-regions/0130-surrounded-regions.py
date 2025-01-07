from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Problem
        -------
        1) Problem is to convert 0(region) or number of 0's (region) surrounded by x all 4 side to X
        2) If 0's are to be found in either 4 borders and any connected 0's around them retain them and dont convert it, because it is not covered by x on all 4 sides

        Note: 1) Goal is to only convert 0's with x on all 4 side (up, down, left, right)
              2) If 0 is to be found at borders then it cant be converted because it is not covered by x on all 4 sides. 
              3) So we only have to convert the required ones and keep the border 0's as is

        Solution
        --------
        1) Use two loops to access top row, bottom row, left column, right column

        2) Convert or tag the border 0's with T and start a DFS from T's co-ordinate and traverse in all 4 direction and convert all the connected 0's with T (why?--> Because Border 0's cant be region because it is not surrounded by X on all 4 sides) 

        3) After all the 0's are converted to T (0's who does not satisfy the region and surround condition)

        4) Run a nested loop, convert 0 to to X, convert T to 0
        """

        rows=len(board)
        columns=len(board[0])

        # Usign BFS
        # def bfs(x, y):
        #     board[x][y]="T"

        #     queue=deque([(x,y)])

        #     directions=[(0,1),(1,0),(-1,0),(0,-1)]

        #     while queue:
        #         left,right=queue.popleft()
        #         # print(left, right)
            

        #         for direction in directions:
        #             newx = left + direction[0]
        #             newy = right + direction[1]

        #             if 0<=newx<rows and 0<=newy<columns and board[newx][newy]=="O":
        #                 board[newx][newy]="T"
        #                 queue.append((newx, newy))


        """
        1) Using recursion with the help of dfs
        """
        def dfs(x, y):
            # Base case when we should return from a call
            if (x<0 or x>=rows or y<0 or y>=columns or board[x][y]!="O"):
                print(x,y)
                return

            board[x][y]="T"

            dfs(x+1,y)      
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for i in range(rows):
            if board[i][0]=="O":
                dfs(i, 0)
            if board[i][columns-1]=="O":
                dfs(i, columns-1)

        for j in range(columns):
            if board[rows-1][j]=="O":
                dfs(rows-1, j)
            if board[0][j]=="O":
                dfs(0, j)
    



        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
    
        return board