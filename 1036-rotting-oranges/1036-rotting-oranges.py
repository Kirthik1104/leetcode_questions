from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        queue=deque([])
        fresh_oranges=0
        times=0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col]==2:
                    queue.append((row, col))
                elif grid[row][col]==1:
                    fresh_oranges+=1
    
        if fresh_oranges==0:
            return 0
    

        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            current_time=False
            levels=len(queue)

            for level in range(levels):
                xaxis, yaxis = queue.popleft()
                for direction in directions:
                    newx = xaxis + direction[0]
                    newy = yaxis + direction[1]

                    if (0<=newx<rows and 0<=newy<columns and grid[newx][newy]==1):
                        grid[newx][newy]=2
                        current_time=True
                        fresh_oranges-=1
                        queue.append((newx, newy))

            if current_time:
                times+=1
        

        return times if fresh_oranges==0 else -1

        






























        # rows= len(grid)
        # columns=len(grid[0])
        # times=0
        # fresh_oranges=0
        # queue=deque()
        # for row in range(rows):
        #     for column in range(columns):
        #         if grid[row][column]==2:
        #             queue.append((row, column))
        #         elif grid[row][column]==1:
        #             fresh_oranges+=1
        
        # if fresh_oranges==0:
        #     return 0
                    
            
        # directions=[(0,1), (1,0), (0,-1), (-1,0)]
        # while queue:
        #     length=len(queue)
        #     current_time=False
            
        #     for length in range(length):
        #         row, col = queue.popleft()
        #         for direction in directions:
        #             new_row= row + direction[0]
        #             new_col= col + direction[1]
                    
        #             if (0<=new_row<rows and 0<=new_col<columns and grid[new_row][new_col]==1):
        #                 grid[new_row][new_col]=2
        #                 queue.append((new_row, new_col))
        #                 current_time=True
        #                 fresh_oranges-=1
            
        #     if current_time:
        #         times+=1

            
        # return times if fresh_oranges==0 else -1